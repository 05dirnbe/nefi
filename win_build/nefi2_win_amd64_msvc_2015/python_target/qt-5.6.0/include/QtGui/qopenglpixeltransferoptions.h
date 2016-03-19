/****************************************************************************
**
** Copyright (C) 2013 Klaralvdalens Datakonsult AB (KDAB).
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

#ifndef QOPENGLPIXELUPLOADOPTIONS_H
#define QOPENGLPIXELUPLOADOPTIONS_H

#include <QtCore/qglobal.h>

#if !defined(QT_NO_OPENGL)

#include <QtCore/QSharedDataPointer>

QT_BEGIN_NAMESPACE

class QOpenGLPixelTransferOptionsData;

class Q_GUI_EXPORT QOpenGLPixelTransferOptions
{
public:
    QOpenGLPixelTransferOptions();
    QOpenGLPixelTransferOptions(const QOpenGLPixelTransferOptions &);
#ifdef Q_COMPILER_RVALUE_REFS
    QOpenGLPixelTransferOptions &operator=(QOpenGLPixelTransferOptions &&other) Q_DECL_NOTHROW
    { swap(other); return *this; }
#endif
    QOpenGLPixelTransferOptions &operator=(const QOpenGLPixelTransferOptions &);
    ~QOpenGLPixelTransferOptions();

    void swap(QOpenGLPixelTransferOptions &other) Q_DECL_NOTHROW
    { data.swap(other.data); }

    void setAlignment(int alignment);
    int alignment() const;

    void setSkipImages(int skipImages);
    int skipImages() const;

    void setSkipRows(int skipRows);
    int skipRows() const;

    void setSkipPixels(int skipPixels);
    int skipPixels() const;

    void setImageHeight(int imageHeight);
    int imageHeight() const;

    void setRowLength(int rowLength);
    int rowLength() const;

    void setLeastSignificantByteFirst(bool lsbFirst);
    bool isLeastSignificantBitFirst() const;

    void setSwapBytesEnabled(bool swapBytes);
    bool isSwapBytesEnabled() const;

private:
    QSharedDataPointer<QOpenGLPixelTransferOptionsData> data;
};

Q_DECLARE_SHARED(QOpenGLPixelTransferOptions)

QT_END_NAMESPACE

#endif // QT_NO_OPENGL

#endif // QOPENGLPIXELUPLOADOPTIONS_H
