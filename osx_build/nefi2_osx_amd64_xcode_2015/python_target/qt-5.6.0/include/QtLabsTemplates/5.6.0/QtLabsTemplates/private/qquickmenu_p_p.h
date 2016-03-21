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

#ifndef QQUICKMENU_P_P_H
#define QQUICKMENU_P_P_H

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

#include <QtCore/qvector.h>
#include <QtCore/qpointer.h>
#include <QtQuick/private/qquickitemchangelistener_p.h>

#include <QtLabsTemplates/private/qquickpopup_p_p.h>

QT_BEGIN_NAMESPACE

class QQmlObjectModel;

class Q_LABSTEMPLATES_EXPORT QQuickMenuPrivate : public QQuickPopupPrivate, public QQuickItemChangeListener
{
    Q_DECLARE_PUBLIC(QQuickMenu)

public:
    QQuickMenuPrivate();

    QQuickItem *itemAt(int index) const;
    void insertItem(int index, QQuickItem *item);
    void moveItem(int from, int to);
    void removeItem(int index, QQuickItem *item);

    void resizeItem(QQuickItem *item);
    void resizeItems();

    void itemChildAdded(QQuickItem *item, QQuickItem *child) Q_DECL_OVERRIDE;
    void itemSiblingOrderChanged(QQuickItem *item) Q_DECL_OVERRIDE;
    void itemParentChanged(QQuickItem *item, QQuickItem *parent) Q_DECL_OVERRIDE;
    void itemDestroyed(QQuickItem *item) Q_DECL_OVERRIDE;
    void itemGeometryChanged(QQuickItem *, const QRectF &newGeometry, const QRectF &oldGeometry) Q_DECL_OVERRIDE;

    void onItemPressed();
    void onItemActiveFocusChanged();
    void onMenuVisibleChanged();
    void maybeUnsetDummyFocusOnTab();

    static void contentData_append(QQmlListProperty<QObject> *prop, QObject *obj);
    static int contentData_count(QQmlListProperty<QObject> *prop);
    static QObject *contentData_at(QQmlListProperty<QObject> *prop, int index);
    static void contentData_clear(QQmlListProperty<QObject> *prop);

    QVector<QObject *> contentData;
    QQmlObjectModel *contentModel;
    QPointer<QQuickItem> dummyFocusItem;
    bool ignoreActiveFocusChanges;
    QString title;
};

QT_END_NAMESPACE

#endif // QQUICKMENU_P_P_H

