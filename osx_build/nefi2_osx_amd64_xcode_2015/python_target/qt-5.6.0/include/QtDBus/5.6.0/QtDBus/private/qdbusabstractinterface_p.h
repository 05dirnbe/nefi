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
// This file is not part of the public API.  This header file may
// change from version to version without notice, or even be
// removed.
//
// We mean it.
//
//

#ifndef QDBUSABSTRACTINTERFACE_P_H
#define QDBUSABSTRACTINTERFACE_P_H

#include <qdbusabstractinterface.h>
#include <qdbusconnection.h>
#include <qdbuserror.h>
#include "qdbusconnection_p.h"
#include "private/qobject_p.h"

#define ANNOTATION_NO_WAIT      "org.freedesktop.DBus.Method.NoReply"

#ifndef QT_NO_DBUS

QT_BEGIN_NAMESPACE

class QDBusAbstractInterfacePrivate : public QObjectPrivate
{
public:
    Q_DECLARE_PUBLIC(QDBusAbstractInterface)

    mutable QDBusConnection connection; // mutable because we want to make calls from const functions
    QString service;
    QString currentOwner;
    QString path;
    QString interface;
    mutable QDBusError lastError;
    int timeout;

    // this is set during creation and never changed
    // it can't be const because QDBusInterfacePrivate has one more check
    bool isValid;

    QDBusAbstractInterfacePrivate(const QString &serv, const QString &p,
                                  const QString &iface, const QDBusConnection& con, bool dynamic);
    virtual ~QDBusAbstractInterfacePrivate() { }
    void initOwnerTracking();
    bool canMakeCalls() const;

    // these functions do not check if the property is valid
    bool property(const QMetaProperty &mp, void *returnValuePtr) const;
    bool setProperty(const QMetaProperty &mp, const QVariant &value);

    // return conn's d pointer
    inline QDBusConnectionPrivate *connectionPrivate() const
    { return QDBusConnectionPrivate::d(connection); }

    void _q_serviceOwnerChanged(const QString &name, const QString &oldOwner, const QString &newOwner);

    static void finishDisconnectNotify(QDBusAbstractInterface *iface, int signalId);
};

QT_END_NAMESPACE

#endif // QT_NO_DBUS
#endif
