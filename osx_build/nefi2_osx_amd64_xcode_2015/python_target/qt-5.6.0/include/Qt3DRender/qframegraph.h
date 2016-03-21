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

#ifndef QT3DRENDER_QFRAMEGRAPH_H
#define QT3DRENDER_QFRAMEGRAPH_H

#include <Qt3DRender/qt3drender_global.h>
#include <Qt3DCore/qcomponent.h>

QT_BEGIN_NAMESPACE

namespace Qt3DRender {

class QFrameGraphPrivate;
class QFrameGraphNode;

class QT3DRENDERSHARED_EXPORT QFrameGraph : public Qt3DCore::QComponent
{
    Q_OBJECT
    // Note : The full namespace has to be used to define the property
    // otherwise this results in an error "cannot assign object to property"
    Q_PROPERTY(Qt3DRender::QFrameGraphNode *activeFrameGraph READ activeFrameGraph WRITE setActiveFrameGraph NOTIFY activeFrameGraphChanged)
    Q_CLASSINFO("DefaultProperty", "activeFrameGraph")

public:
    explicit QFrameGraph(Qt3DCore::QNode *parent = 0);
    ~QFrameGraph();

    QFrameGraphNode *activeFrameGraph() const;

public Q_SLOTS:
    void setActiveFrameGraph(QFrameGraphNode *activeFrameGraph);

Q_SIGNALS:
    void activeFrameGraphChanged(QFrameGraphNode *activeFrameGraph);

protected:
    QFrameGraph(QFrameGraphPrivate &dd, Qt3DCore::QNode *parent = 0);
    void copy(const Qt3DCore::QNode *ref) Q_DECL_OVERRIDE;

private:
    Q_DECLARE_PRIVATE(QFrameGraph)
    QT3D_CLONEABLE(QFrameGraph)
};

} // namespace Qt3DRender

QT_END_NAMESPACE

#endif // QT3DRENDER_QFRAMEGRAPH_H
