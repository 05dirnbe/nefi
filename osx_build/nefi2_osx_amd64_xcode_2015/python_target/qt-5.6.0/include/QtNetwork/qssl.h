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


#ifndef QSSL_H
#define QSSL_H

#include <QtCore/qglobal.h>
#include <QtCore/QFlags>

QT_BEGIN_NAMESPACE


namespace QSsl {
    enum KeyType {
        PrivateKey,
        PublicKey
    };

    enum EncodingFormat {
        Pem,
        Der
    };

    enum KeyAlgorithm {
        Opaque,
        Rsa,
        Dsa,
        Ec
    };

    enum AlternativeNameEntryType {
        EmailEntry,
        DnsEntry
    };

#if QT_DEPRECATED_SINCE(5,0)
    typedef AlternativeNameEntryType AlternateNameEntryType;
#endif

    enum SslProtocol {
        SslV3,
        SslV2,
        TlsV1_0,
#if QT_DEPRECATED_SINCE(5,0)
        TlsV1 = TlsV1_0,
#endif
        TlsV1_1,
        TlsV1_2,
        AnyProtocol,
        TlsV1SslV3,
        SecureProtocols,

        TlsV1_0OrLater,
        TlsV1_1OrLater,
        TlsV1_2OrLater,

        UnknownProtocol = -1
    };

    enum SslOption {
        SslOptionDisableEmptyFragments = 0x01,
        SslOptionDisableSessionTickets = 0x02,
        SslOptionDisableCompression = 0x04,
        SslOptionDisableServerNameIndication = 0x08,
        SslOptionDisableLegacyRenegotiation = 0x10,
        SslOptionDisableSessionSharing = 0x20,
        SslOptionDisableSessionPersistence = 0x40,
        SslOptionDisableServerCipherPreference = 0x80
    };
    Q_DECLARE_FLAGS(SslOptions, SslOption)
}

Q_DECLARE_OPERATORS_FOR_FLAGS(QSsl::SslOptions)

QT_END_NAMESPACE

#endif // QSSL_H
