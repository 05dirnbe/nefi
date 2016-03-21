/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the test suite of the Qt Toolkit.
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

#ifndef QUICKTESTEVENT_P_H
#define QUICKTESTEVENT_P_H

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

#include <QtQuickTest/quicktestglobal.h>
#include <QtCore/qobject.h>
#include <QtGui/QWindow>
QT_BEGIN_NAMESPACE

class Q_QUICK_TEST_EXPORT QuickTestEvent : public QObject
{
    Q_OBJECT
public:
    QuickTestEvent(QObject *parent = 0);
    ~QuickTestEvent();

public Q_SLOTS:
    bool keyPress(int key, int modifiers, int delay);
    bool keyRelease(int key, int modifiers, int delay);
    bool keyClick(int key, int modifiers, int delay);

    bool keyPressChar(const QString &character, int modifiers, int delay);
    bool keyReleaseChar(const QString &character, int modifiers, int delay);
    bool keyClickChar(const QString &character, int modifiers, int delay);

    bool mousePress(QObject *item, qreal x, qreal y, int button,
                    int modifiers, int delay);
    bool mouseRelease(QObject *item, qreal x, qreal y, int button,
                      int modifiers, int delay);
    bool mouseClick(QObject *item, qreal x, qreal y, int button,
                    int modifiers, int delay);
    bool mouseDoubleClick(QObject *item, qreal x, qreal y, int button,
                          int modifiers, int delay);
    bool mouseDoubleClickSequence(QObject *item, qreal x, qreal y, int button,
                          int modifiers, int delay);
    bool mouseMove(QObject *item, qreal x, qreal y, int delay, int buttons);

#ifndef QT_NO_WHEELEVENT
    bool mouseWheel(QObject *item, qreal x, qreal y, int buttons,
               int modifiers, int xDelta, int yDelta, int delay);
#endif

private:
    QWindow *eventWindow(QObject *item = 0);
    QWindow *activeWindow();
};

QT_END_NAMESPACE

#endif
