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

#ifndef QSQLRECORD_H
#define QSQLRECORD_H

#include <QtCore/qstring.h>
#include <QtSql/qsql.h>

QT_BEGIN_NAMESPACE


class QSqlField;
class QStringList;
class QVariant;
class QSqlRecordPrivate;

class Q_SQL_EXPORT QSqlRecord
{
public:
    QSqlRecord();
    QSqlRecord(const QSqlRecord& other);
    QSqlRecord& operator=(const QSqlRecord& other);
    ~QSqlRecord();

    bool operator==(const QSqlRecord &other) const;
    inline bool operator!=(const QSqlRecord &other) const { return !operator==(other); }

    QVariant value(int i) const;
    QVariant value(const QString& name) const;
    void setValue(int i, const QVariant& val);
    void setValue(const QString& name, const QVariant& val);

    void setNull(int i);
    void setNull(const QString& name);
    bool isNull(int i) const;
    bool isNull(const QString& name) const;

    int indexOf(const QString &name) const;
    QString fieldName(int i) const;

    QSqlField field(int i) const;
    QSqlField field(const QString &name) const;

    bool isGenerated(int i) const;
    bool isGenerated(const QString& name) const;
    void setGenerated(const QString& name, bool generated);
    void setGenerated(int i, bool generated);

    void append(const QSqlField& field);
    void replace(int pos, const QSqlField& field);
    void insert(int pos, const QSqlField& field);
    void remove(int pos);

    bool isEmpty() const;
    bool contains(const QString& name) const;
    void clear();
    void clearValues();
    int count() const;
    QSqlRecord keyValues(const QSqlRecord &keyFields) const;

private:
    void detach();
    QSqlRecordPrivate* d;
};

#ifndef QT_NO_DEBUG_STREAM
Q_SQL_EXPORT QDebug operator<<(QDebug, const QSqlRecord &);
#endif

QT_END_NAMESPACE

#endif // QSQLRECORD_H
