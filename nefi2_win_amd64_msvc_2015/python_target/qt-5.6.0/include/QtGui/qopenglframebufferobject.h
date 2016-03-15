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

#ifndef QOPENGLFRAMEBUFFEROBJECT_H
#define QOPENGLFRAMEBUFFEROBJECT_H

#include <QtCore/qglobal.h>

#ifndef QT_NO_OPENGL

#include <QtGui/qopengl.h>
#include <QtGui/qpaintdevice.h>

#include <QtCore/qscopedpointer.h>

QT_BEGIN_NAMESPACE


class QOpenGLFramebufferObjectPrivate;
class QOpenGLFramebufferObjectFormat;

class Q_GUI_EXPORT QOpenGLFramebufferObject
{
    Q_DECLARE_PRIVATE(QOpenGLFramebufferObject)
public:
    enum Attachment {
        NoAttachment,
        CombinedDepthStencil,
        Depth
    };

    explicit QOpenGLFramebufferObject(const QSize &size, GLenum target = GL_TEXTURE_2D);
    QOpenGLFramebufferObject(int width, int height, GLenum target = GL_TEXTURE_2D);

    QOpenGLFramebufferObject(const QSize &size, Attachment attachment,
                         GLenum target = GL_TEXTURE_2D, GLenum internalFormat = 0);
    QOpenGLFramebufferObject(int width, int height, Attachment attachment,
                         GLenum target = GL_TEXTURE_2D, GLenum internalFormat = 0);

    QOpenGLFramebufferObject(const QSize &size, const QOpenGLFramebufferObjectFormat &format);
    QOpenGLFramebufferObject(int width, int height, const QOpenGLFramebufferObjectFormat &format);

    virtual ~QOpenGLFramebufferObject();

    void addColorAttachment(const QSize &size, GLenum internalFormat = 0);
    void addColorAttachment(int width, int height, GLenum internalFormat = 0);

    QOpenGLFramebufferObjectFormat format() const;

    bool isValid() const;
    bool isBound() const;
    bool bind();
    bool release();

    int width() const { return size().width(); }
    int height() const { return size().height(); }

    GLuint texture() const;
    QVector<GLuint> textures() const;

    GLuint takeTexture();
    GLuint takeTexture(int colorAttachmentIndex);

    QSize size() const;
    QVector<QSize> sizes() const;

    QImage toImage() const;
    QImage toImage(bool flipped) const;
    QImage toImage(bool flipped, int colorAttachmentIndex) const;

    Attachment attachment() const;
    void setAttachment(Attachment attachment);

    GLuint handle() const;

    static bool bindDefault();

    static bool hasOpenGLFramebufferObjects();

    static bool hasOpenGLFramebufferBlit();
    static void blitFramebuffer(QOpenGLFramebufferObject *target, const QRect &targetRect,
                                QOpenGLFramebufferObject *source, const QRect &sourceRect,
                                GLbitfield buffers,
                                GLenum filter,
                                int readColorAttachmentIndex,
                                int drawColorAttachmentIndex);
    static void blitFramebuffer(QOpenGLFramebufferObject *target, const QRect &targetRect,
                                QOpenGLFramebufferObject *source, const QRect &sourceRect,
                                GLbitfield buffers = GL_COLOR_BUFFER_BIT,
                                GLenum filter = GL_NEAREST);
    static void blitFramebuffer(QOpenGLFramebufferObject *target,
                                QOpenGLFramebufferObject *source,
                                GLbitfield buffers = GL_COLOR_BUFFER_BIT,
                                GLenum filter = GL_NEAREST);

private:
    Q_DISABLE_COPY(QOpenGLFramebufferObject)
    QScopedPointer<QOpenGLFramebufferObjectPrivate> d_ptr;
    friend class QOpenGLPaintDevice;
    friend class QOpenGLFBOGLPaintDevice;
};

class QOpenGLFramebufferObjectFormatPrivate;
class Q_GUI_EXPORT QOpenGLFramebufferObjectFormat
{
public:
    QOpenGLFramebufferObjectFormat();
    QOpenGLFramebufferObjectFormat(const QOpenGLFramebufferObjectFormat &other);
    QOpenGLFramebufferObjectFormat &operator=(const QOpenGLFramebufferObjectFormat &other);
    ~QOpenGLFramebufferObjectFormat();

    void setSamples(int samples);
    int samples() const;

    void setMipmap(bool enabled);
    bool mipmap() const;

    void setAttachment(QOpenGLFramebufferObject::Attachment attachment);
    QOpenGLFramebufferObject::Attachment attachment() const;

    void setTextureTarget(GLenum target);
    GLenum textureTarget() const;

    void setInternalTextureFormat(GLenum internalTextureFormat);
    GLenum internalTextureFormat() const;

    bool operator==(const QOpenGLFramebufferObjectFormat& other) const;
    bool operator!=(const QOpenGLFramebufferObjectFormat& other) const;

private:
    QOpenGLFramebufferObjectFormatPrivate *d;

    void detach();
};

QT_END_NAMESPACE

#endif // QT_NO_OPENGL

#endif // QOPENGLFRAMEBUFFEROBJECT_H
