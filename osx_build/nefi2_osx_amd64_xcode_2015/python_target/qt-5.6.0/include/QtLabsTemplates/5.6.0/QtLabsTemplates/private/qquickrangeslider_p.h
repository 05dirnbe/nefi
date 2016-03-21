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

#ifndef QQUICKRANGESLIDER_H
#define QQUICKRANGESLIDER_H

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

#include <QtLabsTemplates/private/qquickcontrol_p.h>

QT_BEGIN_NAMESPACE

class QQuickRangeSliderPrivate;
class QQuickRangeSliderNode;

class Q_LABSTEMPLATES_EXPORT QQuickRangeSlider : public QQuickControl
{
    Q_OBJECT
    Q_PROPERTY(qreal from READ from WRITE setFrom NOTIFY fromChanged FINAL)
    Q_PROPERTY(qreal to READ to WRITE setTo NOTIFY toChanged FINAL)
    Q_PROPERTY(QQuickRangeSliderNode *first READ first CONSTANT)
    Q_PROPERTY(QQuickRangeSliderNode *second READ second CONSTANT)
    Q_PROPERTY(qreal stepSize READ stepSize WRITE setStepSize NOTIFY stepSizeChanged FINAL)
    Q_PROPERTY(SnapMode snapMode READ snapMode WRITE setSnapMode NOTIFY snapModeChanged FINAL)
    Q_PROPERTY(Qt::Orientation orientation READ orientation WRITE setOrientation NOTIFY orientationChanged FINAL)
    Q_PROPERTY(QQuickItem *track READ track WRITE setTrack NOTIFY trackChanged FINAL)

public:
    explicit QQuickRangeSlider(QQuickItem *parent = Q_NULLPTR);

    qreal from() const;
    void setFrom(qreal from);

    qreal to() const;
    void setTo(qreal to);

    QQuickRangeSliderNode *first() const;
    QQuickRangeSliderNode *second() const;

    qreal stepSize() const;
    void setStepSize(qreal step);

    enum SnapMode {
        NoSnap,
        SnapAlways,
        SnapOnRelease
    };
    Q_ENUM(SnapMode)

    SnapMode snapMode() const;
    void setSnapMode(SnapMode mode);

    Qt::Orientation orientation() const;
    void setOrientation(Qt::Orientation orientation);

    QQuickItem *track() const;
    void setTrack(QQuickItem *track);

    Q_INVOKABLE void setValues(qreal firstValue, qreal secondValue);

Q_SIGNALS:
    void fromChanged();
    void toChanged();
    void stepSizeChanged();
    void snapModeChanged();
    void orientationChanged();
    void trackChanged();

protected:
    void keyPressEvent(QKeyEvent *event) Q_DECL_OVERRIDE;
    void keyReleaseEvent(QKeyEvent *event) Q_DECL_OVERRIDE;
    void mousePressEvent(QMouseEvent *event) Q_DECL_OVERRIDE;
    void mouseMoveEvent(QMouseEvent *event) Q_DECL_OVERRIDE;
    void mouseReleaseEvent(QMouseEvent *event) Q_DECL_OVERRIDE;
    void mouseUngrabEvent() Q_DECL_OVERRIDE;
    void mirrorChange() Q_DECL_OVERRIDE;
    void componentComplete() Q_DECL_OVERRIDE;

#ifndef QT_NO_ACCESSIBILITY
    QAccessible::Role accessibleRole() const Q_DECL_OVERRIDE;
#endif

private:
    friend class QQuickRangeSliderNode;

    Q_DISABLE_COPY(QQuickRangeSlider)
    Q_DECLARE_PRIVATE(QQuickRangeSlider)
};

class QQuickRangeSliderNodePrivate;

class Q_LABSTEMPLATES_EXPORT QQuickRangeSliderNode : public QObject
{
    Q_OBJECT
    Q_PROPERTY(qreal value READ value WRITE setValue NOTIFY valueChanged FINAL)
    Q_PROPERTY(qreal position READ position NOTIFY positionChanged FINAL)
    Q_PROPERTY(qreal visualPosition READ visualPosition NOTIFY visualPositionChanged FINAL)
    Q_PROPERTY(QQuickItem *handle READ handle WRITE setHandle NOTIFY handleChanged FINAL)
    Q_PROPERTY(bool pressed READ isPressed WRITE setPressed NOTIFY pressedChanged FINAL)

public:
    explicit QQuickRangeSliderNode(qreal value, QQuickRangeSlider *slider);
    ~QQuickRangeSliderNode();

    qreal value() const;
    void setValue(qreal value);

    qreal position() const;
    qreal visualPosition() const;

    QQuickItem *handle() const;
    void setHandle(QQuickItem *handle);

    bool isPressed() const;
    void setPressed(bool pressed);

public Q_SLOTS:
    void increase();
    void decrease();

Q_SIGNALS:
    void valueChanged();
    void positionChanged();
    void visualPositionChanged();
    void handleChanged();
    void pressedChanged();

private:
    Q_DISABLE_COPY(QQuickRangeSliderNode)
    Q_DECLARE_PRIVATE(QQuickRangeSliderNode)
};

QT_END_NAMESPACE

QML_DECLARE_TYPE(QQuickRangeSlider)

#endif // QQUICKRANGESLIDER_H
