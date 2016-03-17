/****************************************************************************
**
** Copyright (C) 2014 John Layt <jlayt@kde.org>
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtPrintSupport module of the Qt Toolkit.
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

#ifndef QPRINTDEVICE_H
#define QPRINTDEVICE_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of internal files.  This header file may change from version to version
// without notice, or even be removed.
//
// We mean it.
//

#include "private/qprint_p.h"

#include <QtCore/qsharedpointer.h>
#include <QtGui/qpagelayout.h>

QT_BEGIN_NAMESPACE

#ifndef QT_NO_PRINTER

class QPlatformPrintDevice;
class QMarginsF;
class QMimeType;
class QDebug;

class Q_PRINTSUPPORT_EXPORT QPrintDevice
{
public:

    QPrintDevice();
    QPrintDevice(const QString & id);
    QPrintDevice(const QPrintDevice &other);
    ~QPrintDevice();

    QPrintDevice &operator=(const QPrintDevice &other);
 #ifdef Q_COMPILER_RVALUE_REFS
    QPrintDevice &operator=(QPrintDevice &&other) { swap(other); return *this; }
#endif

    void swap(QPrintDevice &other) { d.swap(other.d); }

    bool operator==(const QPrintDevice &other) const;

    QString id() const;
    QString name() const;
    QString location() const;
    QString makeAndModel() const;

    bool isValid() const;
    bool isDefault() const;
    bool isRemote() const;

    QPrint::DeviceState state() const;

    bool isValidPageLayout(const QPageLayout &layout, int resolution) const;

    bool supportsMultipleCopies() const;
    bool supportsCollateCopies() const;

    QPageSize defaultPageSize() const;
    QList<QPageSize> supportedPageSizes() const;

    QPageSize supportedPageSize(const QPageSize &pageSize) const;
    QPageSize supportedPageSize(QPageSize::PageSizeId pageSizeId) const;
    QPageSize supportedPageSize(const QString &pageName) const;
    QPageSize supportedPageSize(const QSize &pointSize) const;
    QPageSize supportedPageSize(const QSizeF &size, QPageSize::Unit units = QPageSize::Point) const;

    bool supportsCustomPageSizes() const;

    QSize minimumPhysicalPageSize() const;
    QSize maximumPhysicalPageSize() const;

    QMarginsF printableMargins(const QPageSize &pageSize, QPageLayout::Orientation orientation, int resolution) const;

    int defaultResolution() const;
    QList<int> supportedResolutions() const;

    QPrint::InputSlot defaultInputSlot() const;
    QList<QPrint::InputSlot> supportedInputSlots() const;

    QPrint::OutputBin defaultOutputBin() const;
    QList<QPrint::OutputBin> supportedOutputBins() const;

    QPrint::DuplexMode defaultDuplexMode() const;
    QList<QPrint::DuplexMode> supportedDuplexModes() const;

    QPrint::ColorMode defaultColorMode() const;
    QList<QPrint::ColorMode> supportedColorModes() const;

#ifndef QT_NO_MIMETYPE
    QList<QMimeType> supportedMimeTypes() const;
#endif

#  ifndef QT_NO_DEBUG_STREAM
    void format(QDebug debug) const;
#  endif

private:
    friend class QPlatformPrinterSupport;
    friend class QPlatformPrintDevice;
    QPrintDevice(QPlatformPrintDevice *dd);
    QSharedPointer<QPlatformPrintDevice> d;
};

Q_DECLARE_SHARED(QPrintDevice)

#  ifndef QT_NO_DEBUG_STREAM
Q_PRINTSUPPORT_EXPORT QDebug operator<<(QDebug debug, const QPrintDevice &);
#  endif
#endif // QT_NO_PRINTER

QT_END_NAMESPACE

#endif // QPLATFORMPRINTDEVICE_H
