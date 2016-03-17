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

#ifndef QT3DRENDER_RENDER_QNORMALDIFFUSEMAPMATERIAL_H
#define QT3DRENDER_RENDER_QNORMALDIFFUSEMAPMATERIAL_H

#include <Qt3DRender/qmaterial.h>
#include <QColor>

QT_BEGIN_NAMESPACE

namespace Qt3DRender {

class QAbstractTextureProvider;
class QNormalDiffuseMapMaterialPrivate;

class QT3DRENDERSHARED_EXPORT QNormalDiffuseMapMaterial : public QMaterial
{
    Q_OBJECT
    Q_PROPERTY(QColor ambient READ ambient WRITE setAmbient NOTIFY ambientChanged)
    Q_PROPERTY(QColor specular READ specular WRITE setSpecular NOTIFY specularChanged)
    Q_PROPERTY(Qt3DRender::QAbstractTextureProvider *diffuse READ diffuse WRITE setDiffuse NOTIFY diffuseChanged)
    Q_PROPERTY(Qt3DRender::QAbstractTextureProvider *normal READ normal WRITE setNormal NOTIFY normalChanged)
    Q_PROPERTY(float shininess READ shininess WRITE setShininess NOTIFY shininessChanged)
    Q_PROPERTY(float textureScale READ textureScale WRITE setTextureScale NOTIFY textureScaleChanged)

public:
    explicit QNormalDiffuseMapMaterial(Qt3DCore::QNode *parent = 0);
    ~QNormalDiffuseMapMaterial();

    QColor ambient() const;
    QColor specular() const;
    QAbstractTextureProvider *diffuse() const;
    QAbstractTextureProvider *normal() const;
    float shininess() const;
    float textureScale() const;

public Q_SLOTS:
    void setAmbient(const QColor &ambient);
    void setSpecular(const QColor &specular);
    void setDiffuse(QAbstractTextureProvider *diffuse);
    void setNormal(QAbstractTextureProvider *normal);
    void setShininess(float shininess);
    void setTextureScale(float textureScale);

Q_SIGNALS:
    void ambientChanged(const QColor &ambient);
    void diffuseChanged(QAbstractTextureProvider *diffuse);
    void normalChanged(QAbstractTextureProvider *normal);
    void specularChanged(const QColor &specular);
    void shininessChanged(float shininess);
    void textureScaleChanged(float textureScale);

protected:
    QNormalDiffuseMapMaterial(QNormalDiffuseMapMaterialPrivate &dd, Qt3DCore::QNode *parent = 0);

private:
    Q_DECLARE_PRIVATE(QNormalDiffuseMapMaterial)
};

} // namespace Qt3DRender

QT_END_NAMESPACE

#endif // QNORMALDIFFUSEMAPMATERIAL_H
