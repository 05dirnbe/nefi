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

#ifndef QT3DRENDER_QFRAMEGRAPHNODE_H
#define QT3DRENDER_QFRAMEGRAPHNODE_H

#include <Qt3DCore/qnode.h>
#include <Qt3DRender/qt3drender_global.h>
#include <QObject>

QT_BEGIN_NAMESPACE

namespace Qt3DRender {

class QFrameGraphNodePrivate;

class QT3DRENDERSHARED_EXPORT QFrameGraphNode : public Qt3DCore::QNode
{
    Q_OBJECT
    Q_PROPERTY(bool enabled READ isEnabled WRITE setEnabled NOTIFY enabledChanged)
public:
    explicit QFrameGraphNode(Qt3DCore::QNode *parent = 0);
    ~QFrameGraphNode();

    QFrameGraphNode *parentFrameGraphNode() const;

    bool isEnabled() const;

public Q_SLOTS:
    void setEnabled(bool enabled);

protected:
    QFrameGraphNode(QFrameGraphNodePrivate &dd, Qt3DCore::QNode *parent = 0);

Q_SIGNALS:
    void enabledChanged(bool enabled);

private:
    Q_DECLARE_PRIVATE(QFrameGraphNode)
};

} // namespace Qt3DRender

QT_END_NAMESPACE

#endif // QT3DRENDER_QFRAMEGRAPHNODE_H
