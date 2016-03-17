/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Copyright (C) 2012 Klaralvdalens Datakonsult AB, a KDAB Group company, info@kdab.com, author Christoph Schleifenbaum <christoph.schleifenbaum@kdab.com>
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

#ifndef QPLATFORMSYSTEMTRAYICON_H
#define QPLATFORMSYSTEMTRAYICON_H

#include "QtCore/qobject.h"

#ifndef QT_NO_SYSTEMTRAYICON

QT_BEGIN_NAMESPACE

class QPlatformMenu;
class QIcon;
class QString;
class QRect;

class Q_GUI_EXPORT QPlatformSystemTrayIcon : public QObject
{
    Q_OBJECT
public:
    enum ActivationReason {
        Unknown,
        Context,
        DoubleClick,
        Trigger,
        MiddleClick
    };
    Q_ENUM(ActivationReason)

    enum MessageIcon { NoIcon, Information, Warning, Critical };
    Q_ENUM(MessageIcon)

    QPlatformSystemTrayIcon();
    ~QPlatformSystemTrayIcon();

    virtual void init() = 0;
    virtual void cleanup() = 0;
    virtual void updateIcon(const QIcon &icon) = 0;
    virtual void updateToolTip(const QString &tooltip) = 0;
    virtual void updateMenu(QPlatformMenu *menu) = 0;
    virtual QRect geometry() const = 0;
    virtual void showMessage(const QString &title, const QString &msg,
                             const QIcon &icon, MessageIcon iconType, int msecs) = 0;

    virtual bool isSystemTrayAvailable() const = 0;
    virtual bool supportsMessages() const = 0;

    virtual QPlatformMenu *createMenu() const;

Q_SIGNALS:
    void activated(QPlatformSystemTrayIcon::ActivationReason reason);
    void messageClicked();
};

QT_END_NAMESPACE

#endif // QT_NO_SYSTEMTRAYICON

#endif // QSYSTEMTRAYICON_P_H
