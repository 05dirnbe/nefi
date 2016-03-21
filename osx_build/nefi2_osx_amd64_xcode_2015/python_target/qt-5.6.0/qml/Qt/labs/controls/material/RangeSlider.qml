/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the Qt Labs Controls module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL3$
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
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or later as published by the Free
** Software Foundation and appearing in the file LICENSE.GPL included in
** the packaging of this file. Please review the following information to
** ensure the GNU General Public License version 2.0 requirements will be
** met: http://www.gnu.org/licenses/gpl-2.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick 2.6
import Qt.labs.templates 1.0 as T
import Qt.labs.controls.material 1.0

T.RangeSlider {
    id: control

    implicitWidth: Math.max(background ? background.implicitWidth : 0,
        Math.max(track ? track.implicitWidth : 0,
            first.handle ? first.handle.implicitWidth : 0,
                second.handle ? second.handle.implicitWidth : 0) + leftPadding + rightPadding)
    implicitHeight: Math.max(background ? background.implicitHeight : 0,
        Math.max(track ? track.implicitHeight : 0,
            first.handle ? first.handle.implicitHeight : 0,
                second.handle ? second.handle.implicitHeight : 0) + topPadding + bottomPadding)

    padding: 6

    //! [firstHandle]
    first.handle: SliderHandle {
        x: control.leftPadding + (horizontal ? control.first.visualPosition * (control.availableWidth - width) : (control.availableWidth - width) / 2)
        y: control.topPadding + (horizontal ? (control.availableHeight - height) / 2 : control.first.visualPosition * (control.availableHeight - height))
        value: first.value
        handleHasFocus: activeFocus
        handlePressed: first.pressed
    }
    //! [firstHandle]

    //! [secondHandle]
    second.handle: SliderHandle {
        x: control.leftPadding + (horizontal ? control.second.visualPosition * (control.availableWidth - width) : (control.availableWidth - width) / 2)
        y: control.topPadding + (horizontal ? (control.availableHeight - height) / 2 : control.second.visualPosition * (control.availableHeight - height))
        value: second.value
        handleHasFocus: activeFocus
        handlePressed: second.pressed
    }
    //! [secondHandle]

    //! [track]
    track: Rectangle {
        x: control.leftPadding + (horizontal ? 0 : (control.availableWidth - width) / 2)
        y: control.topPadding + (horizontal ? (control.availableHeight - height) / 2 : 0)
        implicitWidth: horizontal ? 200 : 1
        implicitHeight: horizontal ? 1 : 200
        width: horizontal ? control.availableWidth : implicitWidth
        height: horizontal ? implicitHeight : control.availableHeight
        color: control.Material.primaryTextColor
        scale: horizontal && control.mirrored ? -1 : 1

        readonly property bool horizontal: control.orientation === Qt.Horizontal

        Rectangle {
            x: parent.horizontal ? control.first.position * parent.width : -1
            y: parent.horizontal ? -1 : control.second.visualPosition * parent.height + 3
            width: parent.horizontal ? control.second.position * parent.width - control.first.position * parent.width - 3 : 3
            height: parent.horizontal ? 3 : control.second.position * parent.height - control.first.position * parent.height - 3

            color: control.Material.accentColor
        }
    }
    //! [track]
}
