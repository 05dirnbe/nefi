/****************************************************************************
**
** Copyright (C) 2014 Klaralvdalens Datakonsult AB (KDAB).
** Copyright (C) 2015 The Qt Company Ltd and/or its subsidiary(-ies).
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

#ifndef QT3DRENDER_QRENDERPASS_H
#define QT3DRENDER_QRENDERPASS_H

#include <Qt3DRender/qt3drender_global.h>

#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/qrenderstate.h>
#include <Qt3DRender/qannotation.h>

#include <QHash>
#include <QList>

QT_BEGIN_NAMESPACE

namespace Qt3DRender {

class QParameter;
class QRenderState;
class QParameterMapping;
typedef QList<QParameter*> ParameterList;

class QRenderPassPrivate;

class QT3DRENDERSHARED_EXPORT QRenderPass : public Qt3DCore::QNode
{
    Q_OBJECT
    Q_PROPERTY(Qt3DRender::QShaderProgram *shaderProgram READ shaderProgram WRITE setShaderProgram NOTIFY shaderProgramChanged)

public:
    explicit QRenderPass(Qt3DCore::QNode *parent = 0);
    ~QRenderPass();

    QString glslNameForParameter(QString paramName) const;

    ParameterList attributes() const;
    ParameterList uniforms() const;

    QShaderProgram *shaderProgram() const;

    void addAnnotation(QAnnotation *criterion);
    void removeAnnotation(QAnnotation *criterion);
    QList<QAnnotation *> annotations() const;

    void addBinding(QParameterMapping *binding);
    void removeBinding(QParameterMapping *binding);
    QList<QParameterMapping *> bindings() const;

    void addRenderState(QRenderState *state);
    void removeRenderState(QRenderState *state);
    QList<QRenderState *> renderStates() const;

    void addParameter(QParameter *p);
    void removeParameter(QParameter *p);
    QList<QParameter *> parameters() const;

public Q_SLOTS:
    void setShaderProgram(QShaderProgram *shaderProgram);

Q_SIGNALS:
    void shaderProgramChanged(QShaderProgram *shaderProgram);

protected:
    QRenderPass(QRenderPassPrivate &dd, Qt3DCore::QNode *parent = 0);
    void copy(const Qt3DCore::QNode *ref) Q_DECL_OVERRIDE;

private:
    Q_DECLARE_PRIVATE(QRenderPass)
    QT3D_CLONEABLE(QRenderPass)
};

}

QT_END_NAMESPACE

#endif // QT3DRENDER_QRENDERPASS_H
