/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtWidgets module of the Qt Toolkit.
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

#ifndef QGRAPHICSLINEARLAYOUT_H
#define QGRAPHICSLINEARLAYOUT_H

#include <QtWidgets/qgraphicsitem.h>
#include <QtWidgets/qgraphicslayout.h>

QT_BEGIN_NAMESPACE


#if !defined(QT_NO_GRAPHICSVIEW)

class QGraphicsLinearLayoutPrivate;

class Q_WIDGETS_EXPORT QGraphicsLinearLayout : public QGraphicsLayout
{
public:
    QGraphicsLinearLayout(QGraphicsLayoutItem *parent = Q_NULLPTR);
    QGraphicsLinearLayout(Qt::Orientation orientation, QGraphicsLayoutItem *parent = Q_NULLPTR);
    virtual ~QGraphicsLinearLayout();

    void setOrientation(Qt::Orientation orientation);
    Qt::Orientation orientation() const;

    inline void addItem(QGraphicsLayoutItem *item) { insertItem(-1, item); }
    inline void addStretch(int stretch = 1) { insertStretch(-1, stretch); }

    void insertItem(int index, QGraphicsLayoutItem *item);
    void insertStretch(int index, int stretch = 1);

    void removeItem(QGraphicsLayoutItem *item);
    void removeAt(int index) Q_DECL_OVERRIDE;

    void setSpacing(qreal spacing);
    qreal spacing() const;
    void setItemSpacing(int index, qreal spacing);
    qreal itemSpacing(int index) const;

    void setStretchFactor(QGraphicsLayoutItem *item, int stretch);
    int stretchFactor(QGraphicsLayoutItem *item) const;

    void setAlignment(QGraphicsLayoutItem *item, Qt::Alignment alignment);
    Qt::Alignment alignment(QGraphicsLayoutItem *item) const;

    void setGeometry(const QRectF &rect) Q_DECL_OVERRIDE;

    int count() const Q_DECL_OVERRIDE;
    QGraphicsLayoutItem *itemAt(int index) const Q_DECL_OVERRIDE;

    void invalidate() Q_DECL_OVERRIDE;
    QSizeF sizeHint(Qt::SizeHint which, const QSizeF &constraint = QSizeF()) const Q_DECL_OVERRIDE;

#if 0 // ###
    Q5SizePolicy::ControlTypes controlTypes(LayoutSide side) const;
#endif

    void dump(int indent = 0) const;

protected:
#if 0
    QSize contentsSizeHint(Qt::SizeHint which, const QSize &constraint = QSize()) const;
#endif

private:
    Q_DISABLE_COPY(QGraphicsLinearLayout)
    Q_DECLARE_PRIVATE(QGraphicsLinearLayout)
};

#endif

QT_END_NAMESPACE

#endif

