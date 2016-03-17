/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtCore module of the Qt Toolkit.
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

#include <QtCore/qglobal.h>

#ifndef QISENUM_H
#define QISENUM_H

#ifndef Q_IS_ENUM
#  if defined(Q_CC_GNU) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
#    define Q_IS_ENUM(x) __is_enum(x)
#  elif defined(Q_CC_MSVC) && defined(_MSC_FULL_VER) && (_MSC_FULL_VER >=140050215)
#    define Q_IS_ENUM(x) __is_enum(x)
#  elif defined(Q_CC_CLANG)
#    if __has_extension(is_enum)
#      define Q_IS_ENUM(x) __is_enum(x)
#    endif
#  endif
#endif

#ifndef Q_IS_ENUM
#  include <QtCore/qtypetraits.h>
#  define Q_IS_ENUM(x) QtPrivate::is_enum<x>::value
#endif

// shut up syncqt
QT_BEGIN_NAMESPACE
QT_END_NAMESPACE
#endif // QISENUM_H
