/****************************************************************************
**
** Copyright (C) 2014 Jeremy Lainé <jeremy.laine@m4x.org>
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


#ifndef QASN1ELEMENT_P_H
#define QASN1ELEMENT_P_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of the QLibrary class.  This header file may change from
// version to version without notice, or even be removed.
//
// We mean it.
//

#include <QtCore/qdatetime.h>
#include <QtCore/qmap.h>

QT_BEGIN_NAMESPACE

#define RSA_ENCRYPTION_OID QByteArrayLiteral("1.2.840.113549.1.1.1")
#define DSA_ENCRYPTION_OID QByteArrayLiteral("1.2.840.10040.4.1")
#define EC_ENCRYPTION_OID QByteArrayLiteral("1.2.840.10045.2.1")

class Q_AUTOTEST_EXPORT QAsn1Element
{
public:
    enum ElementType {
        // universal
        BooleanType = 0x01,
        IntegerType  = 0x02,
        BitStringType  = 0x03,
        OctetStringType = 0x04,
        NullType = 0x05,
        ObjectIdentifierType = 0x06,
        Utf8StringType = 0x0c,
        PrintableStringType = 0x13,
        TeletexStringType = 0x14,
        UtcTimeType = 0x17,
        GeneralizedTimeType = 0x18,
        SequenceType = 0x30,
        SetType = 0x31,

        // GeneralNameTypes
        Rfc822NameType = 0x81,
        DnsNameType = 0x82,
        UniformResourceIdentifierType = 0x86,

        // context specific
        Context0Type = 0xA0,
        Context1Type = 0xA1,
        Context3Type = 0xA3
    };

    explicit QAsn1Element(quint8 type = 0, const QByteArray &value = QByteArray());
    bool read(QDataStream &data);
    bool read(const QByteArray &data);
    void write(QDataStream &data) const;

    static QAsn1Element fromBool(bool val);
    static QAsn1Element fromInteger(unsigned int val);
    static QAsn1Element fromVector(const QVector<QAsn1Element> &items);
    static QAsn1Element fromObjectId(const QByteArray &id);

    bool toBool(bool *ok = 0) const;
    QDateTime toDateTime() const;
    QMultiMap<QByteArray, QString> toInfo() const;
    qint64 toInteger(bool *ok = 0) const;
    QVector<QAsn1Element> toVector() const;
    QByteArray toObjectId() const;
    QByteArray toObjectName() const;
    QString toString() const;

    quint8 type() const { return mType; }
    QByteArray value() const { return mValue; }

    friend inline bool operator==(const QAsn1Element &, const QAsn1Element &);
    friend inline bool operator!=(const QAsn1Element &, const QAsn1Element &);

private:
    quint8 mType;
    QByteArray mValue;
};
Q_DECLARE_TYPEINFO(QAsn1Element, Q_MOVABLE_TYPE);

inline bool operator==(const QAsn1Element &e1, const QAsn1Element &e2)
{ return e1.mType == e2.mType && e1.mValue == e2.mValue; }

inline bool operator!=(const QAsn1Element &e1, const QAsn1Element &e2)
{ return e1.mType != e2.mType || e1.mValue != e2.mValue; }

QT_END_NAMESPACE

#endif
