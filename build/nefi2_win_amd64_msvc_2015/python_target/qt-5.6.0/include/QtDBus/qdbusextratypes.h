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

#ifndef QDBUSEXTRATYPES_H
#define QDBUSEXTRATYPES_H

// define some useful types for D-BUS

#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbusmacros.h>
#if QT_DEPRECATED_SINCE(5, 6)
#include <QtCore/qhash.h>
#endif
#include <QtCore/qhashfunctions.h>

#ifndef QT_NO_DBUS

QT_BEGIN_NAMESPACE


class Q_DBUS_EXPORT QDBusObjectPath
{
    QString m_path;
public:
    QDBusObjectPath() Q_DECL_NOTHROW : m_path() {}
    // compiler-generated copy/move constructor/assignment operators are ok!
    // compiler-generated destructor is ok!

    inline explicit QDBusObjectPath(const char *path);
    inline explicit QDBusObjectPath(QLatin1String path);
    inline explicit QDBusObjectPath(const QString &path);
#ifdef Q_COMPILER_RVALUE_REFS
    explicit QDBusObjectPath(QString &&p) : m_path(std::move(p)) { doCheck(); }
#endif

    void swap(QDBusObjectPath &other) Q_DECL_NOTHROW { qSwap(m_path, other.m_path); }

    inline void setPath(const QString &path);

    inline QString path() const
    { return m_path; }

private:
    void doCheck();
};
Q_DECLARE_SHARED_NOT_MOVABLE_UNTIL_QT6(QDBusObjectPath)

inline QDBusObjectPath::QDBusObjectPath(const char *objectPath)
    : m_path(QString::fromLatin1(objectPath))
{ doCheck(); }

inline QDBusObjectPath::QDBusObjectPath(QLatin1String objectPath)
    : m_path(objectPath)
{ doCheck(); }

inline QDBusObjectPath::QDBusObjectPath(const QString &objectPath)
    : m_path(objectPath)
{ doCheck(); }

inline void QDBusObjectPath::setPath(const QString &objectPath)
{ m_path = objectPath; doCheck(); }

inline bool operator==(const QDBusObjectPath &lhs, const QDBusObjectPath &rhs)
{ return lhs.path() == rhs.path(); }

inline bool operator!=(const QDBusObjectPath &lhs, const QDBusObjectPath &rhs)
{ return lhs.path() != rhs.path(); }

inline bool operator<(const QDBusObjectPath &lhs, const QDBusObjectPath &rhs)
{ return lhs.path() < rhs.path(); }

inline uint qHash(const QDBusObjectPath &objectPath, uint seed = 0)
{ return qHash(objectPath.path(), seed); }


class Q_DBUS_EXPORT QDBusSignature
{
    QString m_signature;
public:
    QDBusSignature() Q_DECL_NOTHROW : m_signature() {}
    // compiler-generated copy/move constructor/assignment operators are ok!
    // compiler-generated destructor is ok!

    inline explicit QDBusSignature(const char *signature);
    inline explicit QDBusSignature(QLatin1String signature);
    inline explicit QDBusSignature(const QString &signature);
#ifdef Q_COMPILER_RVALUE_REFS
    explicit QDBusSignature(QString &&sig) : m_signature(std::move(sig)) { doCheck(); }
#endif

    void swap(QDBusSignature &other) Q_DECL_NOTHROW { qSwap(m_signature, other.m_signature); }

    inline void setSignature(const QString &signature);

    inline QString signature() const
    { return m_signature; }

private:
    void doCheck();
};
Q_DECLARE_SHARED_NOT_MOVABLE_UNTIL_QT6(QDBusSignature)

inline QDBusSignature::QDBusSignature(const char *dBusSignature)
    : m_signature(QString::fromLatin1(dBusSignature))
{ doCheck(); }

inline QDBusSignature::QDBusSignature(QLatin1String dBusSignature)
    : m_signature(dBusSignature)
{ doCheck(); }

inline QDBusSignature::QDBusSignature(const QString &dBusSignature)
    : m_signature(dBusSignature)
{ doCheck(); }

inline void QDBusSignature::setSignature(const QString &dBusSignature)
{ m_signature = dBusSignature; doCheck(); }

inline bool operator==(const QDBusSignature &lhs, const QDBusSignature &rhs)
{ return lhs.signature() == rhs.signature(); }

inline bool operator!=(const QDBusSignature &lhs, const QDBusSignature &rhs)
{ return lhs.signature() != rhs.signature(); }

inline bool operator<(const QDBusSignature &lhs, const QDBusSignature &rhs)
{ return lhs.signature() < rhs.signature(); }

inline uint qHash(const QDBusSignature &signature, uint seed = 0)
{ return qHash(signature.signature(), seed); }

class QDBusVariant
{
    QVariant m_variant;
public:
    QDBusVariant() Q_DECL_NOTHROW : m_variant() {}
    // compiler-generated copy/move constructor/assignment operators are ok!
    // compiler-generated destructor is ok!

    inline explicit QDBusVariant(const QVariant &variant);
#ifdef Q_COMPILER_RVALUE_REFS
    explicit QDBusVariant(QVariant &&v) Q_DECL_NOTHROW : m_variant(std::move(v)) {}
#endif

    void swap(QDBusVariant &other) Q_DECL_NOTHROW { qSwap(m_variant, other.m_variant); }

    inline void setVariant(const QVariant &variant);

    inline QVariant variant() const
    { return m_variant; }
};
Q_DECLARE_SHARED_NOT_MOVABLE_UNTIL_QT6(QDBusVariant)

inline  QDBusVariant::QDBusVariant(const QVariant &dBusVariant)
    : m_variant(dBusVariant) { }

inline void QDBusVariant::setVariant(const QVariant &dBusVariant)
{ m_variant = dBusVariant; }

inline bool operator==(const QDBusVariant &v1, const QDBusVariant &v2)
{ return v1.variant() == v2.variant(); }

QT_END_NAMESPACE

Q_DECLARE_METATYPE(QDBusVariant)
Q_DECLARE_METATYPE(QDBusObjectPath)
Q_DECLARE_METATYPE(QDBusSignature)

#endif // QT_NO_DBUS
#endif
