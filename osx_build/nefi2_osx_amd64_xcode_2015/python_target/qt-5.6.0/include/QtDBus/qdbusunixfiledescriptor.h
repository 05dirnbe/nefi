/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtDBus module of the Qt Toolkit.
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


#ifndef QDBUSUNIXFILEDESCRIPTOR_H
#define QDBUSUNIXFILEDESCRIPTOR_H

#include <QtCore/qshareddata.h>
#include <QtDBus/qdbusmacros.h>

#ifndef QT_NO_DBUS

#ifdef Q_COMPILER_RVALUE_REFS
# include <utility>
#endif

QT_BEGIN_NAMESPACE


class QDBusUnixFileDescriptorPrivate;

class Q_DBUS_EXPORT QDBusUnixFileDescriptor
{
public:
    QDBusUnixFileDescriptor();
    explicit QDBusUnixFileDescriptor(int fileDescriptor);
    QDBusUnixFileDescriptor(const QDBusUnixFileDescriptor &other);
#if defined(Q_COMPILER_RVALUE_REFS)
    QDBusUnixFileDescriptor &operator=(QDBusUnixFileDescriptor &&other) Q_DECL_NOTHROW { swap(other); return *this; }
#endif
    QDBusUnixFileDescriptor &operator=(const QDBusUnixFileDescriptor &other);
    ~QDBusUnixFileDescriptor();

    void swap(QDBusUnixFileDescriptor &other) Q_DECL_NOTHROW
    { qSwap(d, other.d); }

    bool isValid() const;

    int fileDescriptor() const;
    void setFileDescriptor(int fileDescriptor);

    void giveFileDescriptor(int fileDescriptor);
    int takeFileDescriptor();

    static bool isSupported();

protected:
    typedef QExplicitlySharedDataPointer<QDBusUnixFileDescriptorPrivate>  Data;
    Data d;
};

Q_DECLARE_SHARED(QDBusUnixFileDescriptor)

QT_END_NAMESPACE

Q_DECLARE_METATYPE(QDBusUnixFileDescriptor)

#endif // QT_NO_DBUS
#endif // QDBUSUNIXFILEDESCRIPTOR_H
