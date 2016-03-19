/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the plugins of the Qt Toolkit.
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

#ifndef QWINDOWSWINDOWFUNCTIONS_H
#define QWINDOWSWINDOWFUNCTIONS_H

#include <QtCore/QByteArray>
#include <QtGui/QGuiApplication>

QT_BEGIN_NAMESPACE

class QWindow;

class QWindowsWindowFunctions {
public:
    enum TouchWindowTouchType {
        NormalTouch   = 0x00000000,
        FineTouch     = 0x00000001,
        WantPalmTouch = 0x00000002
    };

    Q_DECLARE_FLAGS(TouchWindowTouchTypes, TouchWindowTouchType)

    typedef void (*SetTouchWindowTouchType)(QWindow *window, QWindowsWindowFunctions::TouchWindowTouchTypes touchType);
    static const QByteArray setTouchWindowTouchTypeIdentifier() { return QByteArrayLiteral("WindowsSetTouchWindowTouchType"); }

    static void setTouchWindowTouchType(QWindow *window, TouchWindowTouchTypes type)
    {
        SetTouchWindowTouchType func = reinterpret_cast<SetTouchWindowTouchType>(QGuiApplication::platformFunction(setTouchWindowTouchTypeIdentifier()));
        if (func)
            func(window, type);
    }

    typedef void (*SetHasBorderInFullScreen)(QWindow *window, bool border);
    static const QByteArray setHasBorderInFullScreenIdentifier() { return QByteArrayLiteral("WindowsSetHasBorderInFullScreen"); }
    static void setHasBorderInFullScreen(QWindow *window, bool border)
    {
        SetHasBorderInFullScreen func = reinterpret_cast<SetHasBorderInFullScreen>(QGuiApplication::platformFunction(setHasBorderInFullScreenIdentifier()));
        if (func)
            func(window, border);
    }
};

Q_DECLARE_OPERATORS_FOR_FLAGS(QWindowsWindowFunctions::TouchWindowTouchTypes)

QT_END_NAMESPACE

#endif // QWINDOWSWINDOWFUNCTIONS_H
