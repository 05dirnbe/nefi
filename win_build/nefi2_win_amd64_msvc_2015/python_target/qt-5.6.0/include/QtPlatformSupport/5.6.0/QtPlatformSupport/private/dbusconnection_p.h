/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtGui module of the Qt Toolkit.
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


#ifndef DBUSCONNECTION_H
#define DBUSCONNECTION_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists purely as an
// implementation detail.  This header file may change from version to
// version without notice, or even be removed.
//
// We mean it.
//

#include <QtCore/QString>
#include <QtDBus/QDBusConnection>
#include <QtDBus/QDBusVariant>

QT_BEGIN_NAMESPACE

class QDBusServiceWatcher;

class DBusConnection : public QObject
{
    Q_OBJECT

public:
    DBusConnection(QObject *parent = 0);
    QDBusConnection connection() const;
    bool isEnabled() const { return m_enabled; }

Q_SIGNALS:
    // Emitted when the global accessibility status changes to enabled
    void enabledChanged(bool enabled);

private Q_SLOTS:
    QString getAddressFromXCB();
    void serviceRegistered();
    void serviceUnregistered();
    void connectA11yBus(const QString &address);

    void dbusError(const QDBusError &error);

private:
    QString getAccessibilityBusAddress() const;

    QDBusServiceWatcher *dbusWatcher;
    QDBusConnection m_a11yConnection;
    bool m_enabled;
};

QT_END_NAMESPACE

#endif // DBUSCONNECTION_H
