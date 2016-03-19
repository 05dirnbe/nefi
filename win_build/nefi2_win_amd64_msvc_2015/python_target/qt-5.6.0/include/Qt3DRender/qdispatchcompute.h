/****************************************************************************
**
** Copyright (C) 2015 Klaralvdalens Datakonsult AB (KDAB).
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

#ifndef QT3DRENDER_QDISPATCHCOMPUTE_H
#define QT3DRENDER_QDISPATCHCOMPUTE_H

#include <Qt3DRender/qt3drender_global.h>
#include <Qt3DRender/qframegraphnode.h>

QT_BEGIN_NAMESPACE

namespace Qt3DRender {

class QDispatchComputePrivate;

class QT3DRENDERSHARED_EXPORT QDispatchCompute : public QFrameGraphNode
{
    Q_OBJECT
    Q_PROPERTY(int workGroupX READ workGroupX WRITE setWorkGroupX NOTIFY workGroupXChanged)
    Q_PROPERTY(int workGroupY READ workGroupY WRITE setWorkGroupY NOTIFY workGroupYChanged)
    Q_PROPERTY(int workGroupZ READ workGroupZ WRITE setWorkGroupZ NOTIFY workGroupZChanged)
public:
    explicit QDispatchCompute(Qt3DCore::QNode *parent = Q_NULLPTR);
    ~QDispatchCompute();

    int workGroupX() const;
    int workGroupY() const;
    int workGroupZ() const;

    void setWorkGroupX(int workGroupX);
    void setWorkGroupY(int workGroupY);
    void setWorkGroupZ(int workGroupZ);

Q_SIGNALS:
    void workGroupXChanged();
    void workGroupYChanged();
    void workGroupZChanged();

    // QNode interface
protected:
    void copy(const Qt3DCore::QNode *ref) Q_DECL_OVERRIDE;

private:
    QT3D_CLONEABLE(QDispatchCompute)
    Q_DECLARE_PRIVATE(QDispatchCompute)
};

} // Qt3DRender

QT_END_NAMESPACE

#endif // QT3DRENDER_QDISPATCHCOMPUTE_H
