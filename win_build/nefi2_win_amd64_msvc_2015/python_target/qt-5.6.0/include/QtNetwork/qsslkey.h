/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtNetwork module of the Qt Toolkit.
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


#ifndef QSSLKEY_H
#define QSSLKEY_H

#include <QtCore/qnamespace.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsharedpointer.h>
#include <QtNetwork/qssl.h>

QT_BEGIN_NAMESPACE


#ifndef QT_NO_SSL

template <typename A, typename B> struct QPair;

class QIODevice;

class QSslKeyPrivate;
class Q_NETWORK_EXPORT QSslKey
{
public:
    QSslKey();
    QSslKey(const QByteArray &encoded, QSsl::KeyAlgorithm algorithm,
            QSsl::EncodingFormat format = QSsl::Pem,
            QSsl::KeyType type = QSsl::PrivateKey,
            const QByteArray &passPhrase = QByteArray());
    QSslKey(QIODevice *device, QSsl::KeyAlgorithm algorithm,
            QSsl::EncodingFormat format = QSsl::Pem,
            QSsl::KeyType type = QSsl::PrivateKey,
            const QByteArray &passPhrase = QByteArray());
    explicit QSslKey(Qt::HANDLE handle, QSsl::KeyType type = QSsl::PrivateKey);
    QSslKey(const QSslKey &other);
#ifdef Q_COMPILER_RVALUE_REFS
    QSslKey &operator=(QSslKey &&other) Q_DECL_NOTHROW { swap(other); return *this; }
#endif
    QSslKey &operator=(const QSslKey &other);
    ~QSslKey();

    void swap(QSslKey &other) Q_DECL_NOTHROW { qSwap(d, other.d); }

    bool isNull() const;
    void clear();

    int length() const;
    QSsl::KeyType type() const;
    QSsl::KeyAlgorithm algorithm() const;

    QByteArray toPem(const QByteArray &passPhrase = QByteArray()) const;
    QByteArray toDer(const QByteArray &passPhrase = QByteArray()) const;

    Qt::HANDLE handle() const;

    bool operator==(const QSslKey &key) const;
    inline bool operator!=(const QSslKey &key) const { return !operator==(key); }

private:
    QExplicitlySharedDataPointer<QSslKeyPrivate> d;
    friend class QSslCertificate;
    friend class QSslSocketBackendPrivate;
};

Q_DECLARE_SHARED(QSslKey)

#ifndef QT_NO_DEBUG_STREAM
class QDebug;
Q_NETWORK_EXPORT QDebug operator<<(QDebug debug, const QSslKey &key);
#endif

#endif // QT_NO_SSL

QT_END_NAMESPACE

#endif
