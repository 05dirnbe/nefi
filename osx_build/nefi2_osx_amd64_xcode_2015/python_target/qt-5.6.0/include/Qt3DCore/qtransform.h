/****************************************************************************
**
** Copyright (C) 2014 Klaralvdalens Datakonsult AB (KDAB).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the Qt3D module of the Qt Toolkit.
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

#ifndef QT3DCORE_QTRANSFORM_H
#define QT3DCORE_QTRANSFORM_H

#include <Qt3DCore/qcomponent.h>

#include <QtGui/qmatrix4x4.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qvector3d.h>

QT_BEGIN_NAMESPACE

namespace Qt3DCore {

class QTransformPrivate;
class QT3DCORESHARED_EXPORT QTransform : public QComponent
{
    Q_OBJECT
    Q_PROPERTY(QMatrix4x4 matrix READ matrix WRITE setMatrix NOTIFY matrixChanged)
    Q_PROPERTY(float scale READ scale WRITE setScale NOTIFY scaleChanged)
    Q_PROPERTY(QVector3D scale3D READ scale3D WRITE setScale3D NOTIFY scale3DChanged)
    Q_PROPERTY(QQuaternion rotation READ rotation WRITE setRotation NOTIFY rotationChanged)
    Q_PROPERTY(float rotationX READ rotationX WRITE setRotationX NOTIFY rotationXChanged)
    Q_PROPERTY(float rotationY READ rotationY WRITE setRotationY NOTIFY rotationYChanged)
    Q_PROPERTY(float rotationZ READ rotationZ WRITE setRotationZ NOTIFY rotationZChanged)
    Q_PROPERTY(QVector3D translation READ translation WRITE setTranslation NOTIFY translationChanged)

public:
    explicit QTransform(QNode *parent = 0);
    ~QTransform();

    float scale() const;
    QVector3D scale3D() const;
    QQuaternion rotation() const;
    QVector3D translation() const;

    Q_INVOKABLE static QQuaternion fromAxisAndAngle(const QVector3D &axis, float angle);
    Q_INVOKABLE static QQuaternion fromAxisAndAngle(float x, float y, float z, float angle);

    Q_INVOKABLE static QQuaternion fromAxesAndAngles(const QVector3D &axis1, float angle1,
                                                     const QVector3D &axis2, float angle2);
    Q_INVOKABLE static QQuaternion fromAxesAndAngles(const QVector3D &axis1, float angle1,
                                                     const QVector3D &axis2, float angle2,
                                                     const QVector3D &axis3, float angle3);

    Q_INVOKABLE static QQuaternion fromEulerAngles(const QVector3D &eulerAngles);
    Q_INVOKABLE static QQuaternion fromEulerAngles(float pitch, float yaw, float roll);

    Q_INVOKABLE static QMatrix4x4 rotateAround(const QVector3D &point, float angle, const QVector3D &axis);

    QMatrix4x4 matrix() const;

    float rotationX() const;
    float rotationY() const;
    float rotationZ() const;

public Q_SLOTS:
    void setScale(float scale);
    void setScale3D(const QVector3D &scale);
    void setRotation(const QQuaternion &rotation);
    void setTranslation(const QVector3D &translation);
    void setMatrix(const QMatrix4x4 &matrix);

    void setRotationX(float rotationX);
    void setRotationY(float rotationY);
    void setRotationZ(float rotationZ);

Q_SIGNALS:
    void scaleChanged(float scale);
    void scale3DChanged(const QVector3D &scale);
    void rotationChanged(const QQuaternion &rotation);
    void rotationXChanged(float rotationX);
    void rotationYChanged(float rotationY);
    void rotationZChanged(float rotationZ);
    void translationChanged(const QVector3D &translation);
    void matrixChanged(const QMatrix4x4 &matrix);

protected:
    QTransform(QTransformPrivate &dd, QNode *parent = 0);
    void copy(const QNode *ref) Q_DECL_OVERRIDE;

private:
    Q_DECLARE_PRIVATE(QTransform)
    QT3D_CLONEABLE(QTransform)
};

} // namespace Qt3DCore

QT_END_NAMESPACE

#endif // QT3DCORE_QTRANSFORM_H
