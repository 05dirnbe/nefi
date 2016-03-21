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

#ifndef QDBUSSERVICEWATCHER_H
#define QDBUSSERVICEWATCHER_H

#include <QtCore/qobject.h>
#include <QtDBus/qdbusmacros.h>

#if !defined(QT_NO_DBUS) && !defined(QT_NO_QOBJECT)

QT_BEGIN_NAMESPACE


class QDBusConnection;

class QDBusServiceWatcherPrivate;
class Q_DBUS_EXPORT QDBusServiceWatcher: public QObject
{
    Q_OBJECT
    Q_PROPERTY(QStringList watchedServices READ watchedServices WRITE setWatchedServices)
    Q_PROPERTY(WatchMode watchMode READ watchMode WRITE setWatchMode)
public:
    enum WatchModeFlag {
        WatchForRegistration = 0x01,
        WatchForUnregistration = 0x02,
        WatchForOwnerChange = 0x03
    };
    Q_DECLARE_FLAGS(WatchMode, WatchModeFlag)

    explicit QDBusServiceWatcher(QObject *parent = Q_NULLPTR);
    QDBusServiceWatcher(const QString &service, const QDBusConnection &connection,
                        WatchMode watchMode = WatchForOwnerChange, QObject *parent = Q_NULLPTR);
    ~QDBusServiceWatcher();

    QStringList watchedServices() const;
    void setWatchedServices(const QStringList &services);
    void addWatchedService(const QString &newService);
    bool removeWatchedService(const QString &service);

    WatchMode watchMode() const;
    void setWatchMode(WatchMode mode);

    QDBusConnection connection() const;
    void setConnection(const QDBusConnection &connection);

Q_SIGNALS:
    void serviceRegistered(const QString &service);
    void serviceUnregistered(const QString &service);
    void serviceOwnerChanged(const QString &service, const QString &oldOwner, const QString &newOwner);

private:
    Q_PRIVATE_SLOT(d_func(), void _q_serviceOwnerChanged(QString,QString,QString))
    Q_DISABLE_COPY(QDBusServiceWatcher)
    Q_DECLARE_PRIVATE(QDBusServiceWatcher)
};

Q_DECLARE_OPERATORS_FOR_FLAGS(QDBusServiceWatcher::WatchMode)

QT_END_NAMESPACE

#endif // QT_NO_DBUS || QT_NO_QOBJECT
#endif // QDBUSSERVICEWATCHER_H
