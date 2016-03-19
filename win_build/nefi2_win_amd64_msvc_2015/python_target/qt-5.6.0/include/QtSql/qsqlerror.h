/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtSql module of the Qt Toolkit.
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

#ifndef QSQLERROR_H
#define QSQLERROR_H

#include <QtCore/qstring.h>
#include <QtSql/qsql.h>

QT_BEGIN_NAMESPACE

class QSqlErrorPrivate;

class Q_SQL_EXPORT QSqlError
{
public:
    enum ErrorType {
        NoError,
        ConnectionError,
        StatementError,
        TransactionError,
        UnknownError
    };
#if QT_DEPRECATED_SINCE(5, 3)
    QT_DEPRECATED QSqlError(const QString &driverText, const QString &databaseText,
                            ErrorType type, int number);
#endif
    QSqlError(const QString &driverText = QString(),
              const QString &databaseText = QString(),
              ErrorType type = NoError,
              const QString &errorCode = QString());
    QSqlError(const QSqlError& other);
    QSqlError& operator=(const QSqlError& other);
    bool operator==(const QSqlError& other) const;
    bool operator!=(const QSqlError& other) const;
    ~QSqlError();

    QString driverText() const;
    QString databaseText() const;
    ErrorType type() const;
#if QT_DEPRECATED_SINCE(5, 3)
    QT_DEPRECATED int number() const;
#endif
    QString nativeErrorCode() const;
    QString text() const;
    bool isValid() const;

#if QT_DEPRECATED_SINCE(5, 1)
    QT_DEPRECATED void setDriverText(const QString &driverText);
    QT_DEPRECATED void setDatabaseText(const QString &databaseText);
    QT_DEPRECATED void setType(ErrorType type);
    QT_DEPRECATED void setNumber(int number);
#endif

private:
    // ### Qt6: Keep the pointer and remove the rest.
    QString unused1;
    QString unused2;
    struct Unused {
        ErrorType unused3;
        int unused4;
    };
    union {
        QSqlErrorPrivate *d;
        Unused unused5;
    };
};

#ifndef QT_NO_DEBUG_STREAM
Q_SQL_EXPORT QDebug operator<<(QDebug, const QSqlError &);
#endif

QT_END_NAMESPACE

#endif // QSQLERROR_H
