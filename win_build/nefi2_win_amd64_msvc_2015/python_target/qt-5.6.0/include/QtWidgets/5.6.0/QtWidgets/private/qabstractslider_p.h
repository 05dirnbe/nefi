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

#ifndef QABSTRACTSLIDER_P_H
#define QABSTRACTSLIDER_P_H

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

#include "QtCore/qbasictimer.h"
#include "QtCore/qelapsedtimer.h"
#include "private/qwidget_p.h"
#include "qstyle.h"

QT_BEGIN_NAMESPACE

class QAbstractSliderPrivate : public QWidgetPrivate
{
    Q_DECLARE_PUBLIC(QAbstractSlider)
public:
    QAbstractSliderPrivate();
    ~QAbstractSliderPrivate();

    void setSteps(int single, int page);

    int minimum, maximum, pageStep, value, position, pressValue;

    /**
     * Call effectiveSingleStep() when changing the slider value.
     */
    int singleStep;

    float offset_accumulated;
    uint tracking : 1;
    uint blocktracking :1;
    uint pressed : 1;
    uint invertedAppearance : 1;
    uint invertedControls : 1;
    Qt::Orientation orientation;

    QBasicTimer repeatActionTimer;
    int repeatActionTime;
    QAbstractSlider::SliderAction repeatAction;

#ifdef QT_KEYPAD_NAVIGATION
    int origValue;

    /**
     */
    bool isAutoRepeating;

    /**
     * When we're auto repeating, we multiply singleStep with this value to
     * get our effective step.
     */
    qreal repeatMultiplier;

    /**
     * The time of when the first auto repeating key press event occurs.
     */
    QElapsedTimer firstRepeat;

#endif

    inline int effectiveSingleStep() const
    {
        return singleStep
#ifdef QT_KEYPAD_NAVIGATION
        * repeatMultiplier
#endif
        ;
    }

    virtual int bound(int val) const { return qMax(minimum, qMin(maximum, val)); }
    inline int overflowSafeAdd(int add) const
    {
        int newValue = value + add;
        if (add > 0 && newValue < value)
            newValue = maximum;
        else if (add < 0 && newValue > value)
            newValue = minimum;
        return newValue;
    }
    inline void setAdjustedSliderPosition(int position)
    {
        Q_Q(QAbstractSlider);
        if (q->style()->styleHint(QStyle::SH_Slider_StopMouseOverSlider, 0, q)) {
            if ((position > pressValue - 2 * pageStep) && (position < pressValue + 2 * pageStep)) {
                repeatAction = QAbstractSlider::SliderNoAction;
                q->setSliderPosition(pressValue);
                return;
            }
        }
        q->triggerAction(repeatAction);
    }
    bool scrollByDelta(Qt::Orientation orientation, Qt::KeyboardModifiers modifiers, int delta);
};

QT_END_NAMESPACE

#endif // QABSTRACTSLIDER_P_H
