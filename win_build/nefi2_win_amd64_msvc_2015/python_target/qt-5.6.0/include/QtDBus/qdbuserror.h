/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtDBus module of the Qt Toolkit.
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

#ifndef QDBUSERROR_H
#define QDBUSERROR_H

#include <QtDBus/qdbusmacros.h>
#include <QtCore/qstring.h>

#ifndef QT_NO_DBUS

struct DBusError;

QT_BEGIN_NAMESPACE


class QDBusMessage;

class Q_DBUS_EXPORT QDBusError
{
public:
    enum ErrorType {
        NoError = 0,
        Other = 1,
        Failed,
        NoMemory,
        ServiceUnknown,
        NoReply,
        BadAddress,
        NotSupported,
        LimitsExceeded,
        AccessDenied,
        NoServer,
        Timeout,
        NoNetwork,
        AddressInUse,
        Disconnected,
        InvalidArgs,
        UnknownMethod,
        TimedOut,
        InvalidSignature,
        UnknownInterface,
        UnknownObject,
        UnknownProperty,
        PropertyReadOnly,
        InternalError,
        InvalidService,
        InvalidObjectPath,
        InvalidInterface,
        InvalidMember,

#ifndef Q_QDOC
        // don't use this one!
        LastErrorType = InvalidMember
#endif
    };

    QDBusError();
#ifndef QT_BOOTSTRAPPED
    explicit QDBusError(const DBusError *error);
    /*implicit*/ QDBusError(const QDBusMessage& msg);
#endif
    QDBusError(ErrorType error, const QString &message);
    QDBusError(const QDBusError &other);
#ifdef Q_COMPILER_RVALUE_REFS
    QDBusError(QDBusError &&other) Q_DECL_NOTHROW
        : code(other.code), msg(std::move(other.msg)), nm(std::move(other.nm)), unused(other.unused)
    { other.unused = Q_NULLPTR; }
    QDBusError &operator=(QDBusError &&other) Q_DECL_NOTHROW { swap(other); return *this; }
#endif
    QDBusError &operator=(const QDBusError &other);
#ifndef QT_BOOTSTRAPPED
    QDBusError &operator=(const QDBusMessage &msg);
#endif

    void swap(QDBusError &other) Q_DECL_NOTHROW
    {
        qSwap(code,   other.code);
        qSwap(msg,    other.msg);
        qSwap(nm,     other.nm);
        qSwap(unused, other.unused);
    }

    ErrorType type() const;
    QString name() const;
    QString message() const;
    bool isValid() const;

    static QString errorString(ErrorType error);

private:
    ErrorType code;
    QString msg;
    QString nm;
    void *unused;
};
Q_DECLARE_SHARED_NOT_MOVABLE_UNTIL_QT6(QDBusError)

#ifndef QT_NO_DEBUG_STREAM
Q_DBUS_EXPORT QDebug operator<<(QDebug, const QDBusError &);
#endif

QT_END_NAMESPACE

Q_DECLARE_METATYPE(QDBusError)

#endif // QT_NO_DBUS
#endif
