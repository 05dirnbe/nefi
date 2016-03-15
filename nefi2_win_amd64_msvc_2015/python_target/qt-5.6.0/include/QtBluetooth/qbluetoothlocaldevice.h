/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtBluetooth module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL21$
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
** General Public License version 2.1 or version 3 as published by the Free
** Software Foundation and appearing in the file LICENSE.LGPLv21 and
** LICENSE.LGPLv3 included in the packaging of this file. Please review the
** following information to ensure the GNU Lesser General Public License
** requirements will be met: https://www.gnu.org/licenses/lgpl.html and
** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** As a special exception, The Qt Company gives you certain additional
** rights. These rights are described in The Qt Company LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QBLUETOOTHLOCALDEVICE_H
#define QBLUETOOTHLOCALDEVICE_H

#include <QtBluetooth/qbluetoothglobal.h>

#include <QtCore/QObject>
#include <QtCore/QList>
#include <QtCore/QString>

#include <QtBluetooth/QBluetoothHostInfo>

QT_BEGIN_NAMESPACE

class QBluetoothLocalDevicePrivate;

class Q_BLUETOOTH_EXPORT QBluetoothLocalDevice : public QObject
{
    Q_OBJECT

public:
    enum Pairing {
        Unpaired,
        Paired,
        AuthorizedPaired
    };
    Q_ENUM(Pairing)

    enum HostMode {
        HostPoweredOff,
        HostConnectable,
        HostDiscoverable,
        HostDiscoverableLimitedInquiry
    };
    Q_ENUM(HostMode)

    enum Error {
        NoError,
        PairingError,
        UnknownError = 100
    };
    Q_ENUM(Error)

    QBluetoothLocalDevice(QObject *parent = 0);
    explicit QBluetoothLocalDevice(const QBluetoothAddress &address, QObject *parent = 0);
    virtual ~QBluetoothLocalDevice();

    bool isValid() const;

    void requestPairing(const QBluetoothAddress &address, Pairing pairing);
    Pairing pairingStatus(const QBluetoothAddress &address) const;

    void setHostMode(QBluetoothLocalDevice::HostMode mode);
    HostMode hostMode() const;
    QList<QBluetoothAddress> connectedDevices() const;

    void powerOn();

    QString name() const;
    QBluetoothAddress address() const;

    static QList<QBluetoothHostInfo> allDevices();

public Q_SLOTS:
    void pairingConfirmation(bool confirmation);

Q_SIGNALS:
    void hostModeStateChanged(QBluetoothLocalDevice::HostMode state);
    void deviceConnected(const QBluetoothAddress &address);
    void deviceDisconnected(const QBluetoothAddress &address);
    void pairingFinished(const QBluetoothAddress &address, QBluetoothLocalDevice::Pairing pairing);

    void pairingDisplayPinCode(const QBluetoothAddress &address, QString pin);
    void pairingDisplayConfirmation(const QBluetoothAddress &address, QString pin);
    void error(QBluetoothLocalDevice::Error error);

private:
    Q_DECLARE_PRIVATE(QBluetoothLocalDevice)
    QBluetoothLocalDevicePrivate *d_ptr;
};

QT_END_NAMESPACE

Q_DECLARE_METATYPE(QBluetoothLocalDevice::Pairing)
Q_DECLARE_METATYPE(QBluetoothLocalDevice::HostMode)
Q_DECLARE_METATYPE(QBluetoothLocalDevice::Error)

#endif // QBLUETOOTHLOCALDEVICE_H
