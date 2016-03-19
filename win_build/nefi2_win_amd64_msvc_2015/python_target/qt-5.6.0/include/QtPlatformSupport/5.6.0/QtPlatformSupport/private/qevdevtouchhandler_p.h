/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the plugins module of the Qt Toolkit.
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

#ifndef QEVDEVTOUCHHANDLER_P_H
#define QEVDEVTOUCHHANDLER_P_H

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

#include <QObject>
#include <QString>
#include <QList>
#include <QThread>
#include <QtCore/private/qthread_p.h>
#include <qpa/qwindowsysteminterface.h>

#if !defined(QT_NO_MTDEV)
struct mtdev;
#endif

QT_BEGIN_NAMESPACE

class QSocketNotifier;
class QEvdevTouchScreenData;

class QEvdevTouchScreenHandler : public QObject
{
    Q_OBJECT

public:
    explicit QEvdevTouchScreenHandler(const QString &device, const QString &spec = QString(), QObject *parent = Q_NULLPTR);
    ~QEvdevTouchScreenHandler();

    QTouchDevice *touchDevice() const;

private slots:
    void readData();

private:
    void registerTouchDevice();
    void unregisterTouchDevice();

    QSocketNotifier *m_notify;
    int m_fd;
    QEvdevTouchScreenData *d;
    QTouchDevice *m_device;
#if !defined(QT_NO_MTDEV)
    mtdev *m_mtdev;
#endif
};

class QEvdevTouchScreenHandlerThread : public QDaemonThread
{
    Q_OBJECT
public:
    explicit QEvdevTouchScreenHandlerThread(const QString &device, const QString &spec, QObject *parent = Q_NULLPTR);
    ~QEvdevTouchScreenHandlerThread();
    void run() Q_DECL_OVERRIDE;

    bool isTouchDeviceRegistered() const;

signals:
    void touchDeviceRegistered();

private:
    Q_INVOKABLE void notifyTouchDeviceRegistered();

    QString m_device;
    QString m_spec;
    QEvdevTouchScreenHandler *m_handler;
    bool m_touchDeviceRegistered;
};

QT_END_NAMESPACE

#endif // QEVDEVTOUCH_P_H
