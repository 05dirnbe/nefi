/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtWidgets module of the Qt Toolkit.
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

#ifndef QOPENGLWIDGET_H
#define QOPENGLWIDGET_H

#include <QtCore/qglobal.h>

#ifndef QT_NO_OPENGL

#include <QtWidgets/QWidget>
#include <QtGui/QSurfaceFormat>
#include <QtGui/qopengl.h>

QT_BEGIN_NAMESPACE

class QOpenGLWidgetPrivate;

class Q_WIDGETS_EXPORT QOpenGLWidget : public QWidget
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QOpenGLWidget)

public:
    enum UpdateBehavior {
        NoPartialUpdate,
        PartialUpdate
    };

    explicit QOpenGLWidget(QWidget* parent = Q_NULLPTR, Qt::WindowFlags f = Qt::WindowFlags());
    ~QOpenGLWidget();

    void setUpdateBehavior(UpdateBehavior updateBehavior);
    UpdateBehavior updateBehavior() const;

    void setFormat(const QSurfaceFormat &format);
    QSurfaceFormat format() const;

    bool isValid() const;

    void makeCurrent();
    void doneCurrent();

    QOpenGLContext *context() const;
    GLuint defaultFramebufferObject() const;

    QImage grabFramebuffer();

Q_SIGNALS:
    void aboutToCompose();
    void frameSwapped();
    void aboutToResize();
    void resized();

protected:
    virtual void initializeGL();
    virtual void resizeGL(int w, int h);
    virtual void paintGL();

    void paintEvent(QPaintEvent *e) Q_DECL_OVERRIDE;
    void resizeEvent(QResizeEvent *e) Q_DECL_OVERRIDE;
    bool event(QEvent *e) Q_DECL_OVERRIDE;

    int metric(QPaintDevice::PaintDeviceMetric metric) const Q_DECL_OVERRIDE;
    QPaintDevice *redirected(QPoint *p) const Q_DECL_OVERRIDE;
    QPaintEngine *paintEngine() const Q_DECL_OVERRIDE;

private:
    Q_DISABLE_COPY(QOpenGLWidget)
};

QT_END_NAMESPACE

#endif // QT_NO_OPENGL

#endif // QOPENGLWIDGET_H
