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

#ifndef QPLATFORMOPENGLCONTEXT_H
#define QPLATFORMOPENGLCONTEXT_H

//
//  W A R N I N G
//  -------------
//
// This file is part of the QPA API and is not meant to be used
// in applications. Usage of this API may make your code
// source and binary incompatible with future versions of Qt.
//

#include <QtCore/qnamespace.h>

#ifndef QT_NO_OPENGL

#include <QtGui/qsurfaceformat.h>
#include <QtGui/qwindow.h>
#include <QtGui/qopengl.h>

QT_BEGIN_NAMESPACE


class QPlatformOpenGLContextPrivate;

class Q_GUI_EXPORT QPlatformOpenGLContext
{
    Q_DECLARE_PRIVATE(QPlatformOpenGLContext)
public:
    QPlatformOpenGLContext();
    virtual ~QPlatformOpenGLContext();

    virtual void initialize();

    virtual QSurfaceFormat format() const = 0;

    virtual void swapBuffers(QPlatformSurface *surface) = 0;

    virtual GLuint defaultFramebufferObject(QPlatformSurface *surface) const;

    virtual bool makeCurrent(QPlatformSurface *surface) = 0;
    virtual void doneCurrent() = 0;

    virtual bool isSharing() const { return false; }
    virtual bool isValid() const { return true; }

    virtual QFunctionPointer getProcAddress(const QByteArray &procName) = 0;

    QOpenGLContext *context() const;

    static bool parseOpenGLVersion(const QByteArray &versionString, int &major, int &minor);

private:
    friend class QOpenGLContext;

    QScopedPointer<QPlatformOpenGLContextPrivate> d_ptr;

    void setContext(QOpenGLContext *context);

    Q_DISABLE_COPY(QPlatformOpenGLContext)
};

QT_END_NAMESPACE

#endif // QT_NO_OPENGL

#endif // QPLATFORMOPENGLCONTEXT_H
