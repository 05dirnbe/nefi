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

#ifndef QPAINTDEVICE_H
#define QPAINTDEVICE_H

#include <QtGui/qwindowdefs.h>
#include <QtCore/qrect.h>

QT_BEGIN_NAMESPACE



class QPaintEngine;
class QPaintDevicePrivate;

class Q_GUI_EXPORT QPaintDevice                                // device for QPainter
{
public:
    enum PaintDeviceMetric {
        PdmWidth = 1,
        PdmHeight,
        PdmWidthMM,
        PdmHeightMM,
        PdmNumColors,
        PdmDepth,
        PdmDpiX,
        PdmDpiY,
        PdmPhysicalDpiX,
        PdmPhysicalDpiY,
        PdmDevicePixelRatio,
        PdmDevicePixelRatioScaled
    };

    virtual ~QPaintDevice();

    virtual int devType() const;
    bool paintingActive() const;
    virtual QPaintEngine *paintEngine() const = 0;

    int width() const { return metric(PdmWidth); }
    int height() const { return metric(PdmHeight); }
    int widthMM() const { return metric(PdmWidthMM); }
    int heightMM() const { return metric(PdmHeightMM); }
    int logicalDpiX() const { return metric(PdmDpiX); }
    int logicalDpiY() const { return metric(PdmDpiY); }
    int physicalDpiX() const { return metric(PdmPhysicalDpiX); }
    int physicalDpiY() const { return metric(PdmPhysicalDpiY); }
    int devicePixelRatio() const { return metric(PdmDevicePixelRatio); }
    qreal devicePixelRatioF()  const { return metric(PdmDevicePixelRatioScaled) / devicePixelRatioFScale(); }
    int colorCount() const { return metric(PdmNumColors); }
    int depth() const { return metric(PdmDepth); }

    static inline qreal devicePixelRatioFScale() { return 0x10000; }
protected:
    QPaintDevice() Q_DECL_NOEXCEPT;
    virtual int metric(PaintDeviceMetric metric) const;
    virtual void initPainter(QPainter *painter) const;
    virtual QPaintDevice *redirected(QPoint *offset) const;
    virtual QPainter *sharedPainter() const;

    ushort        painters;                        // refcount
private:
    Q_DISABLE_COPY(QPaintDevice)

    QPaintDevicePrivate *reserved;

    friend class QPainter;
    friend class QPainterPrivate;
    friend class QFontEngineMac;
    friend class QX11PaintEngine;
    friend Q_GUI_EXPORT int qt_paint_device_metric(const QPaintDevice *device, PaintDeviceMetric metric);
};

/*****************************************************************************
  Inline functions
 *****************************************************************************/

inline int QPaintDevice::devType() const
{ return QInternal::UnknownDevice; }

inline bool QPaintDevice::paintingActive() const
{ return painters != 0; }

QT_END_NAMESPACE

#endif // QPAINTDEVICE_H
