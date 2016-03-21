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

#ifndef QQUICKTABBAR_P_H
#define QQUICKTABBAR_P_H

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

#include <QtLabsTemplates/private/qquickcontainer_p.h>

QT_BEGIN_NAMESPACE

class QQuickTabBarPrivate;

class Q_LABSTEMPLATES_EXPORT QQuickTabBar : public QQuickContainer
{
    Q_OBJECT

public:
    explicit QQuickTabBar(QQuickItem *parent = Q_NULLPTR);

protected:
    void updatePolish() Q_DECL_OVERRIDE;
    void componentComplete() Q_DECL_OVERRIDE;
    void geometryChanged(const QRectF &newGeometry, const QRectF &oldGeometry) Q_DECL_OVERRIDE;
    bool isContent(QQuickItem *item) const Q_DECL_OVERRIDE;
    void itemAdded(int index, QQuickItem *item) Q_DECL_OVERRIDE;
    void itemRemoved(int index, QQuickItem *item) Q_DECL_OVERRIDE;

#ifndef QT_NO_ACCESSIBILITY
    QAccessible::Role accessibleRole() const Q_DECL_OVERRIDE;
#endif

private:
    Q_DISABLE_COPY(QQuickTabBar)
    Q_DECLARE_PRIVATE(QQuickTabBar)
};

QT_END_NAMESPACE

QML_DECLARE_TYPE(QQuickTabBar)

#endif // QQUICKTABBAR_P_H
