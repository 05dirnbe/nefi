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
import Qt.labs.controls.universal 1.0

T.ItemDelegate {
    id: control

    implicitWidth: Math.max(background ? background.implicitWidth : 0,
                            (label ? label.implicitWidth : 0) +
                            (indicator ? indicator.implicitWidth : 0) +
                            (label && indicator ? spacing : 0) + leftPadding + rightPadding)
    implicitHeight: Math.max(background ? background.implicitHeight : 0,
                             Math.max(label ? label.implicitHeight : 0,
                                      indicator ? indicator.implicitHeight : 0) + topPadding + bottomPadding)
    baselineOffset: label ? label.y + label.baselineOffset : 0

    spacing: 12

    topPadding: 11
    leftPadding: 12
    rightPadding: 12
    bottomPadding: 13

    //! [indicator]
    indicator: Image {
        x: text ? (control.mirrored ? control.width - width - control.rightPadding : control.leftPadding) : control.leftPadding + (control.availableWidth - width) / 2
        y: control.topPadding + (control.availableHeight - height) / 2

        visible: control.checked
        source: !control.checkable ? "" : "image://universal/checkmark/" + (!control.enabled ? control.Universal.baseLowColor : control.pressed ? control.Universal.baseHighColor : control.Universal.baseMediumHighColor)
    }
    //! [indicator]

    //! [label]
    label: Text {
        x: control.mirrored || !control.checkable ? control.leftPadding : (indicator.x + indicator.width + control.spacing)
        y: control.topPadding
        width: control.availableWidth - (control.checkable ? indicator.width + control.spacing : 0)
        height: control.availableHeight

        text: control.text
        font: control.font
        elide: Text.ElideRight
        visible: control.text
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        renderType: Text.NativeRendering

        color: !control.enabled ? control.Universal.baseLowColor : control.Universal.baseHighColor
    }
    //! [label]

    //! [background]
    background: Rectangle {
        visible: control.pressed || control.highlighted || control.activeFocus
        color: control.pressed ? control.Universal.listMediumColor : control.Universal.altMediumLowColor
        Rectangle {
            width: parent.width
            height: parent.height
            visible: control.activeFocus || control.highlighted
            color: control.Universal.accent
            opacity: control.Universal.theme === Universal.Light ? 0.4 : 0.6
        }

    }
    //! [background]
}
