/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtCore module of the Qt Toolkit.
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

#ifndef QEVENTLOOP_H
#define QEVENTLOOP_H

#include <QtCore/qobject.h>

QT_BEGIN_NAMESPACE


class QEventLoopPrivate;

class Q_CORE_EXPORT QEventLoop : public QObject
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QEventLoop)

public:
    explicit QEventLoop(QObject *parent = Q_NULLPTR);
    ~QEventLoop();

    enum ProcessEventsFlag {
        AllEvents = 0x00,
        ExcludeUserInputEvents = 0x01,
        ExcludeSocketNotifiers = 0x02,
        WaitForMoreEvents = 0x04,
        X11ExcludeTimers = 0x08,
        EventLoopExec = 0x20,
        DialogExec = 0x40
    };
    Q_DECLARE_FLAGS(ProcessEventsFlags, ProcessEventsFlag)

    bool processEvents(ProcessEventsFlags flags = AllEvents);
    void processEvents(ProcessEventsFlags flags, int maximumTime);

    int exec(ProcessEventsFlags flags = AllEvents);
    void exit(int returnCode = 0);
    bool isRunning() const;

    void wakeUp();

    bool event(QEvent *event) Q_DECL_OVERRIDE;

public Q_SLOTS:
    void quit();
};

Q_DECLARE_OPERATORS_FOR_FLAGS(QEventLoop::ProcessEventsFlags)


class QEventLoopLockerPrivate;

class Q_CORE_EXPORT QEventLoopLocker
{
public:
    QEventLoopLocker();
    explicit QEventLoopLocker(QEventLoop *loop);
    explicit QEventLoopLocker(QThread *thread);
    ~QEventLoopLocker();

private:
    Q_DISABLE_COPY(QEventLoopLocker)
    QEventLoopLockerPrivate *d_ptr;
};

QT_END_NAMESPACE

#endif // QEVENTLOOP_H
