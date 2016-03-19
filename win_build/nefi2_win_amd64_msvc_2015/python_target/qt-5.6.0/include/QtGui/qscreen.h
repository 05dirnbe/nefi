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

#ifndef QSCREEN_H
#define QSCREEN_H

#include <QtCore/QList>
#include <QtCore/QObject>
#include <QtCore/QRect>
#include <QtCore/QSize>
#include <QtCore/QSizeF>

#include <QtGui/QTransform>

#include <QtCore/qnamespace.h>

QT_BEGIN_NAMESPACE


class QPlatformScreen;
class QScreenPrivate;
class QWindow;
class QRect;
class QPixmap;
#ifndef QT_NO_DEBUG_STREAM
class QDebug;
#endif

class Q_GUI_EXPORT QScreen : public QObject
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QScreen)

    Q_PROPERTY(QString name READ name CONSTANT)
    Q_PROPERTY(int depth READ depth CONSTANT)
    Q_PROPERTY(QSize size READ size NOTIFY geometryChanged)
    Q_PROPERTY(QSize availableSize READ availableSize NOTIFY availableGeometryChanged)
    Q_PROPERTY(QSize virtualSize READ virtualSize NOTIFY virtualGeometryChanged)
    Q_PROPERTY(QSize availableVirtualSize READ availableVirtualSize NOTIFY virtualGeometryChanged)
    Q_PROPERTY(QRect geometry READ geometry NOTIFY geometryChanged)
    Q_PROPERTY(QRect availableGeometry READ availableGeometry NOTIFY availableGeometryChanged)
    Q_PROPERTY(QRect virtualGeometry READ virtualGeometry NOTIFY virtualGeometryChanged)
    Q_PROPERTY(QRect availableVirtualGeometry READ availableVirtualGeometry NOTIFY virtualGeometryChanged)
    Q_PROPERTY(QSizeF physicalSize READ physicalSize NOTIFY physicalSizeChanged)
    Q_PROPERTY(qreal physicalDotsPerInchX READ physicalDotsPerInchX NOTIFY physicalDotsPerInchChanged)
    Q_PROPERTY(qreal physicalDotsPerInchY READ physicalDotsPerInchY NOTIFY physicalDotsPerInchChanged)
    Q_PROPERTY(qreal physicalDotsPerInch READ physicalDotsPerInch NOTIFY physicalDotsPerInchChanged)
    Q_PROPERTY(qreal logicalDotsPerInchX READ logicalDotsPerInchX NOTIFY logicalDotsPerInchChanged)
    Q_PROPERTY(qreal logicalDotsPerInchY READ logicalDotsPerInchY NOTIFY logicalDotsPerInchChanged)
    Q_PROPERTY(qreal logicalDotsPerInch READ logicalDotsPerInch NOTIFY logicalDotsPerInchChanged)
    Q_PROPERTY(qreal devicePixelRatio READ devicePixelRatio NOTIFY physicalDotsPerInchChanged)
    Q_PROPERTY(Qt::ScreenOrientation primaryOrientation READ primaryOrientation NOTIFY primaryOrientationChanged)
    Q_PROPERTY(Qt::ScreenOrientation orientation READ orientation NOTIFY orientationChanged)
    Q_PROPERTY(Qt::ScreenOrientation nativeOrientation READ nativeOrientation)
    Q_PROPERTY(qreal refreshRate READ refreshRate NOTIFY refreshRateChanged)

public:
    ~QScreen();
    QPlatformScreen *handle() const;

    QString name() const;

    int depth() const;

    QSize size() const;
    QRect geometry() const;

    QSizeF physicalSize() const;

    qreal physicalDotsPerInchX() const;
    qreal physicalDotsPerInchY() const;
    qreal physicalDotsPerInch() const;

    qreal logicalDotsPerInchX() const;
    qreal logicalDotsPerInchY() const;
    qreal logicalDotsPerInch() const;

    qreal devicePixelRatio() const;

    QSize availableSize() const;
    QRect availableGeometry() const;

    QList<QScreen *> virtualSiblings() const;

    QSize virtualSize() const;
    QRect virtualGeometry() const;

    QSize availableVirtualSize() const;
    QRect availableVirtualGeometry() const;

    Qt::ScreenOrientation primaryOrientation() const;
    Qt::ScreenOrientation orientation() const;
    Qt::ScreenOrientation nativeOrientation() const;

    Qt::ScreenOrientations orientationUpdateMask() const;
    void setOrientationUpdateMask(Qt::ScreenOrientations mask);

    int angleBetween(Qt::ScreenOrientation a, Qt::ScreenOrientation b) const;
    QTransform transformBetween(Qt::ScreenOrientation a, Qt::ScreenOrientation b, const QRect &target) const;
    QRect mapBetween(Qt::ScreenOrientation a, Qt::ScreenOrientation b, const QRect &rect) const;

    bool isPortrait(Qt::ScreenOrientation orientation) const;
    bool isLandscape(Qt::ScreenOrientation orientation) const;

    QPixmap grabWindow(WId window, int x = 0, int y = 0, int w = -1, int h = -1);

    qreal refreshRate() const;

Q_SIGNALS:
    void geometryChanged(const QRect &geometry);
    void availableGeometryChanged(const QRect &geometry);
    void physicalSizeChanged(const QSizeF &size);
    void physicalDotsPerInchChanged(qreal dpi);
    void logicalDotsPerInchChanged(qreal dpi);
    void virtualGeometryChanged(const QRect &rect);
    void primaryOrientationChanged(Qt::ScreenOrientation orientation);
    void orientationChanged(Qt::ScreenOrientation orientation);
    void refreshRateChanged(qreal refreshRate);

private:
    explicit QScreen(QPlatformScreen *screen);

    Q_DISABLE_COPY(QScreen)
    friend class QGuiApplicationPrivate;
    friend class QPlatformIntegration;
    friend class QPlatformScreen;
    friend class QHighDpiScaling;
};

#ifndef QT_NO_DEBUG_STREAM
Q_GUI_EXPORT QDebug operator<<(QDebug, const QScreen *);
#endif

QT_END_NAMESPACE

#endif // QSCREEN_H

