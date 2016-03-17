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

#ifndef QSCROLLERPROPERTIES_H
#define QSCROLLERPROPERTIES_H

#include <QtCore/QScopedPointer>
#include <QtCore/QMetaType>
#include <QtCore/QVariant>

QT_BEGIN_NAMESPACE


class QScroller;
class QScrollerPrivate;
class QScrollerPropertiesPrivate;

class Q_WIDGETS_EXPORT QScrollerProperties
{
public:
    QScrollerProperties();
    QScrollerProperties(const QScrollerProperties &sp);
    QScrollerProperties &operator=(const QScrollerProperties &sp);
    virtual ~QScrollerProperties();

    bool operator==(const QScrollerProperties &sp) const;
    bool operator!=(const QScrollerProperties &sp) const;

    static void setDefaultScrollerProperties(const QScrollerProperties &sp);
    static void unsetDefaultScrollerProperties();

    enum OvershootPolicy
    {
        OvershootWhenScrollable,
        OvershootAlwaysOff,
        OvershootAlwaysOn
    };

    enum FrameRates {
        Standard,
        Fps60,
        Fps30,
        Fps20
    };

    enum ScrollMetric
    {
        MousePressEventDelay,                    // qreal [s]
        DragStartDistance,                       // qreal [m]
        DragVelocitySmoothingFactor,             // qreal [0..1/s]  (complex calculation involving time) v = v_new* DASF + v_old * (1-DASF)
        AxisLockThreshold,                       // qreal [0..1] atan(|min(dx,dy)|/|max(dx,dy)|)

        ScrollingCurve,                          // QEasingCurve
        DecelerationFactor,                      // slope of the curve

        MinimumVelocity,                         // qreal [m/s]
        MaximumVelocity,                         // qreal [m/s]
        MaximumClickThroughVelocity,             // qreal [m/s]

        AcceleratingFlickMaximumTime,            // qreal [s]
        AcceleratingFlickSpeedupFactor,          // qreal [1..]

        SnapPositionRatio,                       // qreal [0..1]
        SnapTime,                                // qreal [s]

        OvershootDragResistanceFactor,           // qreal [0..1]
        OvershootDragDistanceFactor,             // qreal [0..1]
        OvershootScrollDistanceFactor,           // qreal [0..1]
        OvershootScrollTime,                     // qreal [s]

        HorizontalOvershootPolicy,               // enum OvershootPolicy
        VerticalOvershootPolicy,                 // enum OvershootPolicy
        FrameRate,                               // enum FrameRates

        ScrollMetricCount
    };

    QVariant scrollMetric(ScrollMetric metric) const;
    void setScrollMetric(ScrollMetric metric, const QVariant &value);

protected:
    QScopedPointer<QScrollerPropertiesPrivate> d;

private:
    QScrollerProperties(QScrollerPropertiesPrivate &dd);

    friend class QScrollerPropertiesPrivate;
    friend class QScroller;
    friend class QScrollerPrivate;
};

QT_END_NAMESPACE

Q_DECLARE_METATYPE(QScrollerProperties::OvershootPolicy)
Q_DECLARE_METATYPE(QScrollerProperties::FrameRates)

#endif // QSCROLLERPROPERTIES_H
