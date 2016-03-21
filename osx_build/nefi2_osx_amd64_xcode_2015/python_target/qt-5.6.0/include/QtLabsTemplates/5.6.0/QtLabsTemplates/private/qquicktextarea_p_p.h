/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the Qt Labs Templates module of the Qt Toolkit.
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

#ifndef QQUICKTEXTAREA_P_P_H
#define QQUICKTEXTAREA_P_P_H

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

#include <QtQuick/private/qquicktextedit_p_p.h>
#include <QtLabsTemplates/private/qquickpressandholdhelper_p.h>

#include "qquicktextarea_p.h"

#ifndef QT_NO_ACCESSIBILITY
#include <QtGui/qaccessible.h>
#endif

QT_BEGIN_NAMESPACE

class QQuickAccessibleAttached;

class QQuickTextAreaPrivate : public QQuickTextEditPrivate
#ifndef QT_NO_ACCESSIBILITY
    , public QAccessible::ActivationObserver
#endif
{
    Q_DECLARE_PUBLIC(QQuickTextArea)

public:
    QQuickTextAreaPrivate();
    ~QQuickTextAreaPrivate();

    static QQuickTextAreaPrivate *get(QQuickTextArea *item) {
        return static_cast<QQuickTextAreaPrivate *>(QObjectPrivate::get(item)); }

    void resizeBackground();
    void resolveFont();

    qreal getImplicitWidth() const Q_DECL_OVERRIDE;
    qreal getImplicitHeight() const Q_DECL_OVERRIDE;

    void implicitWidthChanged() Q_DECL_OVERRIDE;
    void implicitHeightChanged() Q_DECL_OVERRIDE;

    void _q_readOnlyChanged(bool isReadOnly);

#ifndef QT_NO_ACCESSIBILITY
    void accessibilityActiveChanged(bool active) Q_DECL_OVERRIDE;
    QAccessible::Role accessibleRole() const Q_DECL_OVERRIDE;
#endif

    QQuickItem *background;
    QString placeholder;
    Qt::FocusReason focusReason;
    QQuickPressAndHoldHelper pressAndHoldHelper;
    QQuickAccessibleAttached *accessibleAttached;
};

QT_END_NAMESPACE

#endif // QQUICKTEXTAREA_P_P_H
