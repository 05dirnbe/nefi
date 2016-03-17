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

#ifndef QDBUSMESSAGE_P_H
#define QDBUSMESSAGE_P_H

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

#include <qatomic.h>
#include <qstring.h>
#include <qdbusmessage.h>
#include <qdbusconnection.h>

struct DBusMessage;

#ifndef QT_NO_DBUS

QT_BEGIN_NAMESPACE

class QDBusConnectionPrivate;

class QDBusMessagePrivate
{
public:
    QDBusMessagePrivate();
    ~QDBusMessagePrivate();

    QList<QVariant> arguments;

    // the following parameters are "const": they are not changed after the constructors
    // the parametersValidated member below controls whether they've been validated already
    QString service, path, interface, name, message, signature;

    DBusMessage *msg;
    DBusMessage *reply;
    mutable QDBusMessage *localReply;
    QAtomicInt ref;
    QDBusMessage::MessageType type;

    mutable uint delayedReply : 1;
    uint localMessage : 1;
    mutable uint parametersValidated : 1;
    uint autoStartService : 1;

    static void setParametersValidated(QDBusMessage &msg, bool enable)
    { msg.d_ptr->parametersValidated = enable; }

    static DBusMessage *toDBusMessage(const QDBusMessage &message, QDBusConnection::ConnectionCapabilities capabilities,
                                      QDBusError *error);
    static QDBusMessage fromDBusMessage(DBusMessage *dmsg, QDBusConnection::ConnectionCapabilities capabilities);

    static bool isLocal(const QDBusMessage &msg);
    static QDBusMessage makeLocal(const QDBusConnectionPrivate &conn,
                                  const QDBusMessage &asSent);
    static QDBusMessage makeLocalReply(const QDBusConnectionPrivate &conn,
                                       const QDBusMessage &asSent);
};

QT_END_NAMESPACE

#endif // QT_NO_DBUS
#endif
