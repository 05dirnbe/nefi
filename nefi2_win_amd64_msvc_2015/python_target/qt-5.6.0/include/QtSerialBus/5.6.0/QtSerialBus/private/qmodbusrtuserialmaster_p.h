/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtSerialBus module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL3$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see http://www.qt.io/terms-conditions. For further
** information use the contact form at http://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or later as published by the Free
** Software Foundation and appearing in the file LICENSE.GPL included in
** the packaging of this file. Please review the following information to
** ensure the GNU General Public License version 2.0 requirements will be
** met: http://www.gnu.org/licenses/gpl-2.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QMODBUSSERIALMASTER_P_H
#define QMODBUSSERIALMASTER_P_H

#include <QtCore/qloggingcategory.h>
#include <QtCore/qmath.h>
#include <QtCore/qpointer.h>
#include <QtCore/qqueue.h>
#include <QtCore/qtimer.h>
#include <QtSerialBus/qmodbusrtuserialmaster.h>
#include <QtSerialPort/qserialport.h>

#include <private/qmodbusadu_p.h>
#include <private/qmodbusclient_p.h>

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API. It exists purely as an
// implementation detail. This header file may change from version to
// version without notice, or even be removed.
//
// We mean it.
//

QT_BEGIN_NAMESPACE

Q_DECLARE_LOGGING_CATEGORY(QT_MODBUS)
Q_DECLARE_LOGGING_CATEGORY(QT_MODBUS_LOW)

class QModbusRtuSerialMasterPrivate : public QModbusClientPrivate
{
    Q_DECLARE_PUBLIC(QModbusRtuSerialMaster)
    enum State {
        Idle,
        Schedule,
        Send,
        Receive,
    } m_state = Idle;

public:
    void setupSerialPort()
    {
        Q_Q(QModbusRtuSerialMaster);

        m_sendTimer.setSingleShot(true);
        QObject::connect(&m_sendTimer, &QTimer::timeout, q, [this]() { processQueue(); });

        m_responseTimer.setSingleShot(true);
        QObject::connect(&m_responseTimer, &QTimer::timeout, q, [this]() { processQueue(); });

        m_serialPort = new QSerialPort(q);
        QObject::connect(m_serialPort, &QSerialPort::readyRead, q, [this]() {
            responseBuffer += m_serialPort->read(m_serialPort->bytesAvailable());
            qCDebug(QT_MODBUS_LOW) << "(RTU client) Response buffer:" << responseBuffer.toHex();

            if (responseBuffer.size() < 2) {
                qCDebug(QT_MODBUS) << "(RTU client) Modbus ADU not complete";
                return;
            }

            const QModbusSerialAdu tmpAdu(QModbusSerialAdu::Rtu, responseBuffer);
            const QModbusResponse tmpPdu = tmpAdu.pdu();
            int pduSizeWithoutFcode = QModbusResponse::calculateDataSize(tmpPdu, tmpPdu.data());
            if (pduSizeWithoutFcode < 0) {
                // wait for more data
                qCDebug(QT_MODBUS) << "(RTU client) Cannot calculate PDU size for function code:"
                                   << tmpPdu.functionCode() << ", delaying pending frame";
                return;
            }

            // server address byte + function code byte + PDU size + 2 bytes CRC
            const int aduSize = 2 + pduSizeWithoutFcode + 2;
            if (tmpAdu.rawSize() < aduSize) {
                qCDebug(QT_MODBUS) << "(RTU client) Incomplete ADU received, ignoring";
                return;
            }

            const QModbusSerialAdu adu(QModbusSerialAdu::Rtu, responseBuffer.left(aduSize));
            responseBuffer.remove(0, aduSize);

            qCDebug(QT_MODBUS)<< "(RTU client) Received ADU:" << adu.rawData().toHex();
            if (QT_MODBUS().isDebugEnabled() && !responseBuffer.isEmpty())
                qCDebug(QT_MODBUS_LOW) << "(RTU client) Pending buffer:" << responseBuffer.toHex();

            // check CRC
            if (!adu.matchingChecksum()) {
                qCWarning(QT_MODBUS) << "(RTU client) Discarding response with wrong CRC, received:"
                                     << adu.checksum<quint16>() << ", calculated CRC:"
                                     << QModbusSerialAdu::calculateCRC(adu.data(), adu.size());
                return;
            }

            const QModbusResponse response = adu.pdu();
            if (!canMatchRequestAndResponse(response, adu.serverAddress())) {
                qCWarning(QT_MODBUS) << "(RTU client) Cannot match response with open request, "
                    "ignoring";
                return;
            }

            m_sendTimer.stop();
            m_responseTimer.stop();
            processQueueElement(response, m_current);

            m_state = Schedule; // reschedule, even if empty
            m_serialPort->clear(QSerialPort::AllDirections);
            QTimer::singleShot(m_timeoutThreeDotFiveMs, [this]() { processQueue(); });
        });

        using TypeId = void (QSerialPort::*)(QSerialPort::SerialPortError);
        QObject::connect(m_serialPort, static_cast<TypeId>(&QSerialPort::error),
                         [this](QSerialPort::SerialPortError error) {
            if (error == QSerialPort::NoError)
                return;

            qCDebug(QT_MODBUS) << "(RTU server) QSerialPort error:" << error
                               << (m_serialPort ? m_serialPort->errorString() : QString());

            Q_Q(QModbusRtuSerialMaster);

            switch (error) {
            case QSerialPort::DeviceNotFoundError:
                q->setError(QModbusDevice::tr("Referenced serial device does not exist."),
                            QModbusDevice::ConnectionError);
                break;
            case QSerialPort::PermissionError:
                q->setError(QModbusDevice::tr("Cannot open serial device due to permissions."),
                            QModbusDevice::ConnectionError);
                break;
            case QSerialPort::OpenError:
            case QSerialPort::NotOpenError:
                q->setError(QModbusDevice::tr("Cannot open serial device."),
                            QModbusDevice::ConnectionError);
                break;
            case QSerialPort::WriteError:
                q->setError(QModbusDevice::tr("Write error."), QModbusDevice::WriteError);
                break;
            case QSerialPort::ReadError:
                q->setError(QModbusDevice::tr("Read error."), QModbusDevice::ReadError);
                break;
            case QSerialPort::ResourceError:
                q->setError(QModbusDevice::tr("Resource error."), QModbusDevice::ConnectionError);
                break;
            case QSerialPort::UnsupportedOperationError:
                q->setError(QModbusDevice::tr("Device operation is not supported error."),
                            QModbusDevice::ConfigurationError);
                break;
            case QSerialPort::TimeoutError:
                q->setError(QModbusDevice::tr("Timeout error."), QModbusDevice::TimeoutError);
                break;
            case QSerialPort::UnknownError:
                q->setError(QModbusDevice::tr("Unknown error."), QModbusDevice::UnknownError);
                break;
            default:
                qCDebug(QT_MODBUS) << "(RTU server) Unhandled QSerialPort error" << error;
                break;
            }
        });

        QObject::connect(m_serialPort, &QSerialPort::bytesWritten, q, [this](qint64 bytes) {
            m_current.bytesWritten += bytes;
        });

        QObject::connect(m_serialPort, &QSerialPort::aboutToClose, q, [this]() {
            Q_Q(QModbusRtuSerialMaster);
            if (q->state() != QModbusDevice::ClosingState)
                q->close();
        });
    }

    void updateSerialPortConnectionInfo() {
        if (m_serialPort) {
            m_serialPort->setPortName(m_comPort);
            m_serialPort->setParity(m_parity);
            m_serialPort->setBaudRate(m_baudRate);
            m_serialPort->setDataBits(m_dataBits);
            m_serialPort->setStopBits(m_stopBits);

            // According to the Modbus specification, in RTU mode message frames
            // are separated by a silent interval of at least 3.5 character times.
            // Calculate the timeout if we are less than 19200 baud, use a fixed
            // timeout for everything equal or greater than 19200 baud.
            if (m_baudRate < 19200) {
                // Example: 9600 baud, 11 bit per packet -> 872 char/sec
                // so: 1000 ms / 872 char = 1.147 ms/char * 3.5 character
                // Always round up because the spec requests at least 3.5 char.
                m_timeoutThreeDotFiveMs = qCeil(3500. / (qreal(m_baudRate) / 11.));
            } else {
                // The spec recommends a timeout value of 1.750 msec. Without such
                // precise single-shot timers use a approximated value of 1.750 msec.
                m_timeoutThreeDotFiveMs = 2;
            }
        }
    }

    void scheduleNextRequest() {
        m_state = Schedule;
        m_serialPort->clear(QSerialPort::AllDirections);
        QTimer::singleShot(m_timeoutThreeDotFiveMs, [this]() { processQueue(); });
    }

    QModbusReply *enqueueRequest(const QModbusRequest &request, int serverAddress,
        const QModbusDataUnit &unit, QModbusReply::ReplyType type) Q_DECL_OVERRIDE
    {
        Q_Q(QModbusRtuSerialMaster);

        QModbusReply *reply = new QModbusReply(type, serverAddress, q);
        QueueElement element(reply, request, unit, m_numberOfRetries + 1);
        element.adu = QModbusSerialAdu::create(QModbusSerialAdu::Rtu, serverAddress, request);
        m_queue.enqueue(element);

        if (m_state == Idle)
            scheduleNextRequest();
        return reply;
    }

    void processQueue()
    {
        Q_ASSERT_X(!m_sendTimer.isActive(), "processQueue", "send timer active");
        Q_ASSERT_X(!m_responseTimer.isActive(), "processQueue", "response timer active");

        auto writeAdu = [this]() {
            responseBuffer.clear();
            m_current.bytesWritten = 0;
            m_current.numberOfRetries--;
            m_serialPort->write(m_current.adu);
            // Example: 9600 baud, 11 bit per packet -> 872 char/sec
            // so: 1000 ms / 872 char = 1.147 ms/char * 3.5 character
            m_sendTimer.start((1000. / (qreal(m_baudRate) / 11.)) * m_current.adu.size());

            qCDebug(QT_MODBUS) << "(RTU client) Sent Serial PDU:" << m_current.requestPdu;
            qCDebug(QT_MODBUS_LOW).noquote() << "(RTU client) Sent Serial ADU: 0x" + m_current.adu
                .toHex();
        };

        switch (m_state) {
        case Schedule:
            m_current = QueueElement();
            if (!m_queue.isEmpty()) {
                m_current = m_queue.dequeue();
                if (m_current.reply) {
                    m_state = Send;
                    QTimer::singleShot(0, [writeAdu]() { writeAdu(); });
                } else {
                    QTimer::singleShot(0, [this]() { processQueue(); });
                }
            } else {
                m_state = Idle;
            }
            break;

        case Send:
            // send timeout will always happen
            if (m_current.reply.isNull()) {
                scheduleNextRequest();
            } else if (m_current.bytesWritten < m_current.adu.size()) {
                qCDebug(QT_MODBUS) << "(RTU client) Send failed:" << m_current.requestPdu;

                if (m_current.numberOfRetries <= 0) {
                    if (m_current.reply) {
                        m_current.reply->setError(QModbusDevice::TimeoutError,
                            QModbusClient::tr("Request timeout."));
                    }
                    scheduleNextRequest();
                } else {
                    m_serialPort->clear(QSerialPort::AllDirections);
                    QTimer::singleShot(m_timeoutThreeDotFiveMs, [writeAdu]() { writeAdu(); });
                }
            } else {
                qCDebug(QT_MODBUS) << "(RTU client) Send successful:" << m_current.requestPdu;
                m_state = Receive;
                m_responseTimer.start(m_responseTimeoutDuration);
            }
            break;

        case Receive:
            // receive timeout will only happen after successful send
            qCDebug(QT_MODBUS) << "(RTU client) Receive timeout:" << m_current.requestPdu;
            if (m_current.reply.isNull()) {
                scheduleNextRequest();
            } else if (m_current.numberOfRetries <= 0) {
                if (m_current.reply) {
                    m_current.reply->setError(QModbusDevice::TimeoutError,
                        QModbusClient::tr("Response timeout."));
                }
                scheduleNextRequest();
            } else {
                m_state = Send;
                m_serialPort->clear(QSerialPort::AllDirections);
                QTimer::singleShot(m_timeoutThreeDotFiveMs, [this, writeAdu]() { writeAdu(); });
            }
            break;

        case Idle:
        default:
            Q_ASSERT_X(false, "processQueue", QByteArray("unexpected state: ").append(m_state));
            break;
        }
    }

    bool canMatchRequestAndResponse(const QModbusResponse &response, int sendingServer) const
    {
        if (m_current.reply.isNull())
            return false;   // reply deleted
        if (m_current.reply->serverAddress() != sendingServer)
            return false;   // server mismatch
        if (m_current.requestPdu.functionCode() != response.functionCode())
            return false;   // request for different function code
        return true;
    }

    bool isOpen() const Q_DECL_OVERRIDE
    {
        if (m_serialPort)
            return m_serialPort->isOpen();
        return false;
    }

    QTimer m_sendTimer;
    QTimer m_responseTimer;

    QueueElement m_current;
    QByteArray responseBuffer;

    QQueue<QueueElement> m_queue;
    QSerialPort *m_serialPort = Q_NULLPTR;

    int m_timeoutThreeDotFiveMs = 2; // A approximated value of 1.750 msec.
};

QT_END_NAMESPACE

#endif // QMODBUSSERIALMASTER_P_H
