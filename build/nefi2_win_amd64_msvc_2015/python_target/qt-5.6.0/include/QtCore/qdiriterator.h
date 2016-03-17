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

#ifndef QDIRITERATOR_H
#define QDIRITERATOR_H

#include <QtCore/qdir.h>

QT_BEGIN_NAMESPACE


class QDirIteratorPrivate;
class Q_CORE_EXPORT QDirIterator {
public:
    enum IteratorFlag {
        NoIteratorFlags = 0x0,
        FollowSymlinks = 0x1,
        Subdirectories = 0x2
    };
    Q_DECLARE_FLAGS(IteratorFlags, IteratorFlag)

    QDirIterator(const QDir &dir, IteratorFlags flags = NoIteratorFlags);
    QDirIterator(const QString &path,
                 IteratorFlags flags = NoIteratorFlags);
    QDirIterator(const QString &path,
                 QDir::Filters filter,
                 IteratorFlags flags = NoIteratorFlags);
    QDirIterator(const QString &path,
                 const QStringList &nameFilters,
                 QDir::Filters filters = QDir::NoFilter,
                 IteratorFlags flags = NoIteratorFlags);

    ~QDirIterator();

    QString next();
    bool hasNext() const;

    QString fileName() const;
    QString filePath() const;
    QFileInfo fileInfo() const;
    QString path() const;

private:
    Q_DISABLE_COPY(QDirIterator)

    QScopedPointer<QDirIteratorPrivate> d;
    friend class QDir;
};

Q_DECLARE_OPERATORS_FOR_FLAGS(QDirIterator::IteratorFlags)

QT_END_NAMESPACE

#endif
