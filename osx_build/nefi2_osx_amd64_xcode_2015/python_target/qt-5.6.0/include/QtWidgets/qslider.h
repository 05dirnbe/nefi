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

#ifndef QSLIDER_H
#define QSLIDER_H

#include <QtWidgets/qabstractslider.h>

QT_BEGIN_NAMESPACE


#ifndef QT_NO_SLIDER

class QSliderPrivate;
class QStyleOptionSlider;
class Q_WIDGETS_EXPORT QSlider : public QAbstractSlider
{
    Q_OBJECT

    Q_PROPERTY(TickPosition tickPosition READ tickPosition WRITE setTickPosition)
    Q_PROPERTY(int tickInterval READ tickInterval WRITE setTickInterval)

public:
    enum TickPosition {
        NoTicks = 0,
        TicksAbove = 1,
        TicksLeft = TicksAbove,
        TicksBelow = 2,
        TicksRight = TicksBelow,
        TicksBothSides = 3
    };
    Q_ENUM(TickPosition)

    explicit QSlider(QWidget *parent = Q_NULLPTR);
    explicit QSlider(Qt::Orientation orientation, QWidget *parent = Q_NULLPTR);

    ~QSlider();

    QSize sizeHint() const Q_DECL_OVERRIDE;
    QSize minimumSizeHint() const Q_DECL_OVERRIDE;

    void setTickPosition(TickPosition position);
    TickPosition tickPosition() const;

    void setTickInterval(int ti);
    int tickInterval() const;

    bool event(QEvent *event) Q_DECL_OVERRIDE;

protected:
    void paintEvent(QPaintEvent *ev) Q_DECL_OVERRIDE;
    void mousePressEvent(QMouseEvent *ev) Q_DECL_OVERRIDE;
    void mouseReleaseEvent(QMouseEvent *ev) Q_DECL_OVERRIDE;
    void mouseMoveEvent(QMouseEvent *ev) Q_DECL_OVERRIDE;
    void initStyleOption(QStyleOptionSlider *option) const;


private:
    friend Q_WIDGETS_EXPORT QStyleOptionSlider qt_qsliderStyleOption(QSlider *slider);

    Q_DISABLE_COPY(QSlider)
    Q_DECLARE_PRIVATE(QSlider)
};

#endif // QT_NO_SLIDER

QT_END_NAMESPACE

#endif // QSLIDER_H
