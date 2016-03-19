/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtGui module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL21$
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
** General Public License version 2.1 or version 3 as published by the Free
** Software Foundation and appearing in the file LICENSE.LGPLv21 and
** LICENSE.LGPLv3 included in the packaging of this file. Please review the
** following information to ensure the GNU Lesser General Public License
** requirements will be met: https://www.gnu.org/licenses/lgpl.html and
** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** As a special exception, The Qt Company gives you certain additional
** rights. These rights are described in The Qt Company LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QOPENGLPAINTDEVICE_H
#define QOPENGLPAINTDEVICE_H

#include <QtCore/qglobal.h>

#ifndef QT_NO_OPENGL

#include <QtGui/qpaintdevice.h>
#include <QtGui/qopengl.h>
#include <QtGui/qopenglcontext.h>

QT_BEGIN_NAMESPACE

class QOpenGLPaintDevicePrivate;

class Q_GUI_EXPORT QOpenGLPaintDevice : public QPaintDevice
{
    Q_DECLARE_PRIVATE(QOpenGLPaintDevice)
public:
    QOpenGLPaintDevice();
    explicit QOpenGLPaintDevice(const QSize &size);
    QOpenGLPaintDevice(int width, int height);
    virtual ~QOpenGLPaintDevice();

    int devType() const { return QInternal::OpenGL; }
    QPaintEngine *paintEngine() const;

    QOpenGLContext *context() const;
    QSize size() const;
    void setSize(const QSize &size);
    void setDevicePixelRatio(qreal devicePixelRatio);

    qreal dotsPerMeterX() const;
    qreal dotsPerMeterY() const;

    void setDotsPerMeterX(qreal);
    void setDotsPerMeterY(qreal);

    void setPaintFlipped(bool flipped);
    bool paintFlipped() const;

    virtual void ensureActiveTarget();

protected:
    QOpenGLPaintDevice(QOpenGLPaintDevicePrivate &dd);
    int metric(QPaintDevice::PaintDeviceMetric metric) const;

    Q_DISABLE_COPY(QOpenGLPaintDevice)
    QScopedPointer<QOpenGLPaintDevicePrivate> d_ptr;
};

QT_END_NAMESPACE

#endif // QT_NO_OPENGL

#endif // QOPENGLPAINTDEVICE_H
