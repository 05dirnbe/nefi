/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the Qt Quick Controls module of the Qt Toolkit.
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

import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Controls.Private 1.0

Loader {
    property Item control
    property Item input
    property Item cursorHandle
    property Item selectionHandle
    property Flickable flickable
    property Component defaultMenu: item && item.defaultMenu ? item.defaultMenu : null
    property QtObject menuInstance: null
    property MouseArea mouseArea
    property QtObject style: __style

    Connections {
        target: control
        onMenuChanged: {
            if (menuInstance !== null) {
                menuInstance.destroy()
                menuInstance = null
            }
        }
    }

    function getMenuInstance()
    {
        // Lazy load menu when first requested
        if (!menuInstance && control.menu) {
            menuInstance = control.menu.createObject(input);
        }
        return menuInstance;
    }

    function syncStyle() {
        if (!style)
            return;

        if (style.__editMenu)
            sourceComponent = style.__editMenu;
        else {
            // todo: get ios/android/base menus from style as well
            source = (Qt.resolvedUrl(Qt.platform.os === "ios" ? "EditMenu_ios.qml"
                : Qt.platform.os === "android" ? "" : "EditMenu_base.qml"));
        }
    }
    onStyleChanged: syncStyle();
    Component.onCompleted: syncStyle();
}
