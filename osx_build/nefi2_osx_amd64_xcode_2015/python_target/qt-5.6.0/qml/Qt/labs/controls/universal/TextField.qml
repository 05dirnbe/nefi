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

T.TextField {
    id: control

    implicitWidth: Math.max(contentWidth + leftPadding + rightPadding,
                            background ? background.implicitWidth : 0,
                            placeholder.implicitWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(contentHeight + topPadding + bottomPadding,
                             background ? background.implicitHeight : 0,
                             placeholder.implicitHeight + topPadding + bottomPadding)

    // TextControlThemePadding + 2 (border)
    topPadding: 5
    leftPadding: 12
    rightPadding: 8
    bottomPadding: 7

    Universal.theme: activeFocus ? Universal.Light : undefined

    color: !enabled ? Universal.chromeDisabledLowColor :
            activeFocus ? Universal.chromeBlackHighColor : Universal.baseHighColor
    selectionColor: Universal.accent
    selectedTextColor: Universal.chromeWhiteColor
    verticalAlignment: TextInput.AlignVCenter
    renderType: Text.NativeRendering

    Text {
        id: placeholder
        x: control.leftPadding
        y: control.topPadding
        width: control.width - (control.leftPadding + control.rightPadding)
        height: control.height - (control.topPadding + control.bottomPadding)

        text: control.placeholderText
        font: control.font
        color: !control.enabled ? control.Universal.chromeDisabledLowColor :
                control.activeFocus ? control.Universal.chromeBlackMediumLowColor : control.Universal.baseMediumColor
        visible: !control.displayText && (!control.activeFocus || control.horizontalAlignment !== Qt.AlignHCenter)
        horizontalAlignment: control.horizontalAlignment
        verticalAlignment: control.verticalAlignment
        renderType: Text.NativeRendering
        elide: Text.ElideRight
    }

    //! [background]
    background: Rectangle {
        implicitWidth: 60 // TextControlThemeMinWidth - 4 (border)
        implicitHeight: 28 // TextControlThemeMinHeight - 4 (border)

        border.width: 2 // TextControlBorderThemeThickness
        border.color: !control.enabled ? control.Universal.baseLowColor :
                       control.activeFocus ? control.Universal.accent : control.Universal.chromeDisabledLowColor
        color: control.enabled ? control.Universal.altHighColor : control.Universal.baseLowColor
    }
    //! [background]
}
