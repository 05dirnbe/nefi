/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtQuick module of the Qt Toolkit.
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

#ifndef QQUICKIMAGEPROVIDER_H
#define QQUICKIMAGEPROVIDER_H

#include <QtQuick/qtquickglobal.h>
#include <QtGui/qimage.h>
#include <QtGui/qpixmap.h>
#include <QtQml/qqmlengine.h>

QT_BEGIN_NAMESPACE


class QQuickImageProviderPrivate;
class QQuickAsyncImageProviderPrivate;
class QSGTexture;
class QQuickWindow;

class Q_QUICK_EXPORT QQuickTextureFactory : public QObject
{
public:
    QQuickTextureFactory();
    virtual ~QQuickTextureFactory();

    virtual QSGTexture *createTexture(QQuickWindow *window) const = 0;
    virtual QSize textureSize() const = 0;
    virtual int textureByteCount() const = 0;
    virtual QImage image() const;

    static QQuickTextureFactory *textureFactoryForImage(const QImage &image);
};

class Q_QUICK_EXPORT QQuickImageResponse : public QObject
{
Q_OBJECT
public:
    QQuickImageResponse();
    virtual ~QQuickImageResponse();

    virtual QQuickTextureFactory *textureFactory() const = 0;
    virtual QString errorString() const;

public Q_SLOTS:
    virtual void cancel();

Q_SIGNALS:
    void finished();
};

class Q_QUICK_EXPORT QQuickImageProvider : public QQmlImageProviderBase
{
public:
    QQuickImageProvider(ImageType type, Flags flags = 0);
    virtual ~QQuickImageProvider();

    ImageType imageType() const;
    Flags flags() const;

#if QT_VERSION >= QT_VERSION_CHECK(6,0,0)
    virtual QImage requestImage(const QString &id, QSize *size, const QSize& requestedSize, bool requestedAutoTransform);
    virtual QPixmap requestPixmap(const QString &id, QSize *size, const QSize& requestedSize, bool requestedAutoTransform);
    virtual QQuickTextureFactory *requestTexture(const QString &id, QSize *size, const QSize &requestedSize, bool requestedAutoTransform);
#else
    virtual QImage requestImage(const QString &id, QSize *size, const QSize& requestedSize);
    virtual QPixmap requestPixmap(const QString &id, QSize *size, const QSize& requestedSize);
    virtual QQuickTextureFactory *requestTexture(const QString &id, QSize *size, const QSize &requestedSize);
#endif

private:
    QQuickImageProviderPrivate *d;
};

class Q_QUICK_EXPORT QQuickAsyncImageProvider : public QQuickImageProvider
{
public:
    QQuickAsyncImageProvider();
    virtual ~QQuickAsyncImageProvider();

    virtual QQuickImageResponse *requestImageResponse(const QString &id, const QSize &requestedSize) = 0;

private:
    QQuickAsyncImageProviderPrivate *d;
};

QT_END_NAMESPACE

#endif // QQUICKIMAGEPROVIDER_H
