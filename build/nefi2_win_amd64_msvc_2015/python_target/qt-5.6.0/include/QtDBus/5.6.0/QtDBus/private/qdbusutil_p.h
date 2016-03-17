/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Copyright (C) 2015 Intel Corporation.
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

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of the QLibrary class.  This header file may change from
// version to version without notice, or even be removed.
//
// We mean it.
//

#ifndef QDBUSUTIL_P_H
#define QDBUSUTIL_P_H

#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

#include <QtDBus/qdbusmacros.h>
#include <QtDBus/qdbuserror.h>

#include "qdbus_symbols_p.h"

#ifndef QT_NO_DBUS

QT_BEGIN_NAMESPACE

namespace QDBusUtil
{
    Q_DBUS_EXPORT bool isValidInterfaceName(const QString &ifaceName);

    Q_DBUS_EXPORT bool isValidUniqueConnectionName(const QString &busName);

    Q_DBUS_EXPORT bool isValidBusName(const QString &busName);

    Q_DBUS_EXPORT bool isValidMemberName(const QString &memberName);

    Q_DBUS_EXPORT bool isValidErrorName(const QString &errorName);

    Q_DBUS_EXPORT bool isValidPartOfObjectPath(const QString &path);

    Q_DBUS_EXPORT bool isValidObjectPath(const QString &path);

    Q_DBUS_EXPORT bool isValidFixedType(int c);

    Q_DBUS_EXPORT bool isValidBasicType(int c);

    Q_DBUS_EXPORT bool isValidSignature(const QString &signature);

    Q_DBUS_EXPORT bool isValidSingleSignature(const QString &signature);

    Q_DBUS_EXPORT QString argumentToString(const QVariant &variant);

    enum AllowEmptyFlag {
        EmptyAllowed,
        EmptyNotAllowed
    };

    inline bool checkInterfaceName(const QString &name, AllowEmptyFlag empty, QDBusError *error)
    {
        if (name.isEmpty()) {
            if (empty == EmptyAllowed) return true;
            *error = QDBusError(QDBusError::InvalidInterface, QLatin1String("Interface name cannot be empty"));
            return false;
        }
        if (isValidInterfaceName(name)) return true;
        *error = QDBusError(QDBusError::InvalidInterface, QString::fromLatin1("Invalid interface class: %1").arg(name));
        return false;
    }

    inline bool checkBusName(const QString &name, AllowEmptyFlag empty, QDBusError *error)
    {
        if (name.isEmpty()) {
            if (empty == EmptyAllowed) return true;
            *error = QDBusError(QDBusError::InvalidService, QLatin1String("Service name cannot be empty"));
            return false;
        }
        if (isValidBusName(name)) return true;
        *error = QDBusError(QDBusError::InvalidService, QString::fromLatin1("Invalid service name: %1").arg(name));
        return false;
    }

    inline bool checkObjectPath(const QString &path, AllowEmptyFlag empty, QDBusError *error)
    {
        if (path.isEmpty()) {
            if (empty == EmptyAllowed) return true;
            *error = QDBusError(QDBusError::InvalidObjectPath, QLatin1String("Object path cannot be empty"));
            return false;
        }
        if (isValidObjectPath(path)) return true;
        *error = QDBusError(QDBusError::InvalidObjectPath, QString::fromLatin1("Invalid object path: %1").arg(path));
        return false;
    }

    inline bool checkMemberName(const QString &name, AllowEmptyFlag empty, QDBusError *error, const char *nameType = 0)
    {
        if (!nameType) nameType = "member";
        if (name.isEmpty()) {
            if (empty == EmptyAllowed) return true;
            *error = QDBusError(QDBusError::InvalidMember, QLatin1String(nameType) + QLatin1String(" name cannot be empty"));
            return false;
        }
        if (isValidMemberName(name)) return true;
        *error = QDBusError(QDBusError::InvalidMember, QString::fromLatin1("Invalid %1 name: %2")
                            .arg(QString::fromLatin1(nameType), name));
        return false;
    }

    inline bool checkErrorName(const QString &name, AllowEmptyFlag empty, QDBusError *error)
    {
        if (name.isEmpty()) {
            if (empty == EmptyAllowed) return true;
            *error = QDBusError(QDBusError::InvalidInterface, QLatin1String("Error name cannot be empty"));
            return false;
        }
        if (isValidErrorName(name)) return true;
        *error = QDBusError(QDBusError::InvalidInterface, QString::fromLatin1("Invalid error name: %1").arg(name));
        return false;
    }

    inline QString dbusService()
    { return QStringLiteral(DBUS_SERVICE_DBUS); }
    inline QString dbusPath()
    { return QStringLiteral(DBUS_PATH_DBUS); }
    inline QString dbusInterface()
    {
        // it's the same string, but just be sure
        Q_ASSERT(dbusService() == QLatin1String(DBUS_INTERFACE_DBUS));
        return dbusService();
    }
    inline QString dbusInterfaceProperties()
    { return QStringLiteral(DBUS_INTERFACE_PROPERTIES); }
    inline QString dbusInterfaceIntrospectable()
    { return QStringLiteral(DBUS_INTERFACE_INTROSPECTABLE); }
    inline QString nameOwnerChanged()
    { return QStringLiteral("NameOwnerChanged"); }
    inline QString disconnectedErrorMessage()
    { return QStringLiteral("Not connected to D-Bus server"); }
}

QT_END_NAMESPACE

#endif // QT_NO_DBUS
#endif
