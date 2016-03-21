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

#ifndef QT3DRENDER_QDEPTHTEST_H
#define QT3DRENDER_QDEPTHTEST_H

#include <Qt3DRender/qrenderstate.h>

QT_BEGIN_NAMESPACE

namespace Qt3DRender {

class QDepthTestPrivate;

class QT3DRENDERSHARED_EXPORT QDepthTest : public QRenderState
{
    Q_OBJECT
    Q_PROPERTY(DepthFunc func READ func WRITE setFunc NOTIFY funcChanged)
public:

    enum DepthFunc {
        Never = 0x0200,
        Always = 0x0207,
        Less = 0x0201,
        LessOrEqual = 0x0203,
        Equal = 0x0202,
        GreaterOrEqual = 0x0206,
        Greater = 0x0204,
        NotEqual = 0x0205
    };
    Q_ENUM(DepthFunc)

    explicit QDepthTest(Qt3DCore::QNode *parent = 0);
    ~QDepthTest();

    DepthFunc func() const;

public Q_SLOTS:
    void setFunc(DepthFunc func);

Q_SIGNALS:
    void funcChanged(DepthFunc func);

protected:
    void copy(const Qt3DCore::QNode *ref) Q_DECL_OVERRIDE;

private:
    Q_DECLARE_PRIVATE(QDepthTest)
    QT3D_CLONEABLE(QDepthTest)
};

} // namespace Qt3DRender

QT_END_NAMESPACE

#endif // QT3DRENDER_QDEPTHTEST_H
