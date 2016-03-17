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

#ifndef QT3DRENDER_QCYLINDERMESH_H
#define QT3DRENDER_QCYLINDERMESH_H

#include <Qt3DRender/qt3drender_global.h>
#include <Qt3DRender/qgeometryrenderer.h>

QT_BEGIN_NAMESPACE


namespace Qt3DRender {

class QT3DRENDERSHARED_EXPORT QCylinderMesh : public QGeometryRenderer
{
    Q_OBJECT
    Q_PROPERTY(int rings READ rings WRITE setRings NOTIFY ringsChanged)
    Q_PROPERTY(int slices READ slices WRITE setSlices NOTIFY slicesChanged)
    Q_PROPERTY(float radius READ radius WRITE setRadius NOTIFY radiusChanged)
    Q_PROPERTY(float length READ length WRITE setLength NOTIFY lengthChanged)
public:
    explicit QCylinderMesh(Qt3DCore::QNode *parent = 0);
    ~QCylinderMesh();

    int rings() const;
    int slices() const;
    float radius() const;
    float length() const;

public Q_SLOTS:
    void setRings(int rings);
    void setSlices(int slices);
    void setRadius(float radius);
    void setLength(float length);

Q_SIGNALS:
    void radiusChanged(float radius);
    void ringsChanged(int rings);
    void slicesChanged(int slices);
    void lengthChanged(float length);

private:
    // As this is a default provided geometry renderer, no one should be able
    // to modify the QGeometryRenderer's properties

    void setInstanceCount(int instanceCount);
    void setPrimitiveCount(int primitiveCount);
    void setBaseVertex(int baseVertex);
    void setBaseInstance(int baseInstance);
    void setRestartIndex(int index);
    void setPrimitiveRestart(bool enabled);
    void setGeometry(QGeometry *geometry);
    void setPrimitiveType(PrimitiveType primitiveType);
};

} // namespace Qt3DRender

QT_END_NAMESPACE

#endif // QT3DRENDER_QCYLINDERMESH_H
