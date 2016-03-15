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


#ifndef QSSLCIPHER_H
#define QSSLCIPHER_H

#include <QtCore/qstring.h>
#include <QtCore/qscopedpointer.h>
#include <QtNetwork/qssl.h>

QT_BEGIN_NAMESPACE


#ifndef QT_NO_SSL

class QSslCipherPrivate;
class Q_NETWORK_EXPORT QSslCipher
{
public:
    QSslCipher();
    explicit QSslCipher(const QString &name);
    QSslCipher(const QString &name, QSsl::SslProtocol protocol);
    QSslCipher(const QSslCipher &other);
#ifdef Q_COMPILER_RVALUE_REFS
    QSslCipher &operator=(QSslCipher &&other) Q_DECL_NOTHROW { swap(other); return *this; }
#endif
    QSslCipher &operator=(const QSslCipher &other);
    ~QSslCipher();

    void swap(QSslCipher &other) Q_DECL_NOTHROW
    { qSwap(d, other.d); }

    bool operator==(const QSslCipher &other) const;
    inline bool operator!=(const QSslCipher &other) const { return !operator==(other); }

    bool isNull() const;
    QString name() const;
    int supportedBits() const;
    int usedBits() const;

    QString keyExchangeMethod() const;
    QString authenticationMethod() const;
    QString encryptionMethod() const;
    QString protocolString() const;
    QSsl::SslProtocol protocol() const;

private:
    QScopedPointer<QSslCipherPrivate> d;
    friend class QSslSocketBackendPrivate;
};

Q_DECLARE_SHARED(QSslCipher)

#ifndef QT_NO_DEBUG_STREAM
class QDebug;
Q_NETWORK_EXPORT QDebug operator<<(QDebug debug, const QSslCipher &cipher);
#endif

#endif // QT_NO_SSL

QT_END_NAMESPACE

#endif

