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

#ifndef QMEMROTATE_P_H
#define QMEMROTATE_P_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists purely as an
// implementation detail.  This header file may change from version to
// version without notice, or even be removed.
//
// We mean it.
//

#include "private/qdrawhelper_p.h"

QT_BEGIN_NAMESPACE

#define QT_ROTATION_CACHEDREAD 1
#define QT_ROTATION_CACHEDWRITE 2
#define QT_ROTATION_PACKING 3
#define QT_ROTATION_TILED 4

#ifndef QT_ROTATION_ALGORITHM
#if Q_BYTE_ORDER == Q_LITTLE_ENDIAN
#define QT_ROTATION_ALGORITHM QT_ROTATION_TILED
#else
#define QT_ROTATION_ALGORITHM QT_ROTATION_CACHEDREAD
#endif
#endif

#define QT_DECL_MEMROTATE(type)                            \
    void Q_GUI_EXPORT qt_memrotate90(const type*, int, int, int, type*, int); \
    void Q_GUI_EXPORT qt_memrotate180(const type*, int, int, int, type*, int); \
    void Q_GUI_EXPORT qt_memrotate270(const type*, int, int, int, type*, int)

QT_DECL_MEMROTATE(quint32);
QT_DECL_MEMROTATE(quint16);
QT_DECL_MEMROTATE(quint24);
QT_DECL_MEMROTATE(quint8);

#undef QT_DECL_MEMROTATE

QT_END_NAMESPACE

#endif // QMEMROTATE_P_H
