/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtNetwork module of the Qt Toolkit.
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

#ifndef QHTTPMULTIPART_P_H
#define QHTTPMULTIPART_P_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of the Network Access API.  This header file may change from
// version to version without notice, or even be removed.
//
// We mean it.
//

#include "QtCore/qshareddata.h"
#include "qnetworkrequest_p.h" // for deriving QHttpPartPrivate from QNetworkHeadersPrivate
#include "private/qobject_p.h"

QT_BEGIN_NAMESPACE


class QHttpPartPrivate: public QSharedData, public QNetworkHeadersPrivate
{
public:
    inline QHttpPartPrivate() : bodyDevice(0), headerCreated(false), readPointer(0)
    {
    }
    ~QHttpPartPrivate()
    {
    }


    QHttpPartPrivate(const QHttpPartPrivate &other)
        : QSharedData(other), QNetworkHeadersPrivate(other), body(other.body),
        header(other.header), headerCreated(other.headerCreated), readPointer(other.readPointer)
    {
        bodyDevice = other.bodyDevice;
    }

    inline bool operator==(const QHttpPartPrivate &other) const
    {
        return rawHeaders == other.rawHeaders && body == other.body &&
                bodyDevice == other.bodyDevice && readPointer == other.readPointer;
    }

    void setBodyDevice(QIODevice *device) {
        bodyDevice = device;
        readPointer = 0;
    }
    void setBody(const QByteArray &newBody) {
        body = newBody;
        readPointer = 0;
    }

    // QIODevice-style methods called by QHttpMultiPartIODevice (but this class is
    // not a QIODevice):
    qint64 bytesAvailable() const;
    qint64 readData(char *data, qint64 maxSize);
    qint64 size() const;
    bool reset();

    QByteArray body;
    QIODevice *bodyDevice;

private:
    void checkHeaderCreated() const;

    mutable QByteArray header;
    mutable bool headerCreated;
    qint64 readPointer;
};



class QHttpMultiPartPrivate;

class Q_AUTOTEST_EXPORT QHttpMultiPartIODevice : public QIODevice
{
public:
    QHttpMultiPartIODevice(QHttpMultiPartPrivate *parentMultiPart) :
            QIODevice(), multiPart(parentMultiPart), readPointer(0), deviceSize(-1) {
    }

    ~QHttpMultiPartIODevice() {
    }

    virtual bool atEnd() const Q_DECL_OVERRIDE {
        return readPointer == size();
    }

    virtual qint64 bytesAvailable() const Q_DECL_OVERRIDE {
        return size() - readPointer;
    }

    virtual void close() Q_DECL_OVERRIDE {
        readPointer = 0;
        partOffsets.clear();
        deviceSize = -1;
        QIODevice::close();
    }

    virtual qint64 bytesToWrite() const Q_DECL_OVERRIDE {
        return 0;
    }

    virtual qint64 size() const Q_DECL_OVERRIDE;
    virtual bool isSequential() const Q_DECL_OVERRIDE;
    virtual bool reset() Q_DECL_OVERRIDE;
    virtual qint64 readData(char *data, qint64 maxSize) Q_DECL_OVERRIDE;
    virtual qint64 writeData(const char *data, qint64 maxSize) Q_DECL_OVERRIDE;

    QHttpMultiPartPrivate *multiPart;
    qint64 readPointer;
    mutable QList<qint64> partOffsets;
    mutable qint64 deviceSize;
};



class QHttpMultiPartPrivate: public QObjectPrivate
{
public:

    QHttpMultiPartPrivate();

    ~QHttpMultiPartPrivate()
    {
        delete device;
    }

    QList<QHttpPart> parts;
    QByteArray boundary;
    QHttpMultiPart::ContentType contentType;
    QHttpMultiPartIODevice *device;

};

QT_END_NAMESPACE


#endif // QHTTPMULTIPART_P_H
