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

#ifndef QT3DRENDER_QCOLORMASK_H
#define QT3DRENDER_QCOLORMASK_H

#include <Qt3DRender/qrenderstate.h>

QT_BEGIN_NAMESPACE

namespace Qt3DRender {

class QColorMaskPrivate;

class QT3DRENDERSHARED_EXPORT QColorMask : public QRenderState
{
    Q_OBJECT
    Q_PROPERTY(bool red READ isRed WRITE setRed NOTIFY redChanged)
    Q_PROPERTY(bool green READ isGreen WRITE setGreen NOTIFY greenChanged)
    Q_PROPERTY(bool blue READ isBlue WRITE setBlue NOTIFY blueChanged)
    Q_PROPERTY(bool alpha READ isAlpha WRITE setAlpha NOTIFY alphaChanged)

public:
    explicit QColorMask(Qt3DCore::QNode *parent = Q_NULLPTR);
    ~QColorMask();

    bool isRed() const;
    bool isGreen() const;
    bool isBlue() const;
    bool isAlpha() const;

public Q_SLOTS:
    void setRed(bool red);
    void setGreen(bool green);
    void setBlue(bool blue);
    void setAlpha(bool alpha);

Q_SIGNALS:
    void redChanged(bool red);
    void greenChanged(bool green);
    void blueChanged(bool blue);
    void alphaChanged(bool alpha);

protected:
    void copy(const Qt3DCore::QNode *ref) Q_DECL_FINAL;

private:
    Q_DECLARE_PRIVATE(QColorMask)
    QT3D_CLONEABLE(QColorMask)
};

} // namespace Qt3DRender

QT_END_NAMESPACE

#endif // QT3DRENDER_QCOLORMASK_H
