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

#ifndef QURLINFO_H
#define QURLINFO_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists purely as an
// implementation detail.  This header file may change from version to
// version without notice, or even be removed.
//
// We mean it.
//

#include <QtCore/qdatetime.h>
#include <QtCore/qstring.h>
#include <QtCore/qiodevice.h>

QT_BEGIN_NAMESPACE


#ifndef QT_NO_FTP

class QUrl;
class QUrlInfoPrivate;

class Q_NETWORK_EXPORT QUrlInfo
{
public:
    enum PermissionSpec {
        ReadOwner = 00400, WriteOwner = 00200, ExeOwner = 00100,
        ReadGroup = 00040, WriteGroup = 00020, ExeGroup = 00010,
        ReadOther = 00004, WriteOther = 00002, ExeOther = 00001 };

    QUrlInfo();
    QUrlInfo(const QUrlInfo &ui);
    QUrlInfo(const QString &name, int permissions, const QString &owner,
             const QString &group, qint64 size, const QDateTime &lastModified,
             const QDateTime &lastRead, bool isDir, bool isFile, bool isSymLink,
             bool isWritable, bool isReadable, bool isExecutable);
    QUrlInfo(const QUrl &url, int permissions, const QString &owner,
             const QString &group, qint64 size, const QDateTime &lastModified,
             const QDateTime &lastRead, bool isDir, bool isFile, bool isSymLink,
             bool isWritable, bool isReadable, bool isExecutable);
    QUrlInfo &operator=(const QUrlInfo &ui);
    virtual ~QUrlInfo();

    virtual void setName(const QString &name);
    virtual void setDir(bool b);
    virtual void setFile(bool b);
    virtual void setSymLink(bool b);
    virtual void setOwner(const QString &s);
    virtual void setGroup(const QString &s);
    virtual void setSize(qint64 size);
    virtual void setWritable(bool b);
    virtual void setReadable(bool b);
    virtual void setPermissions(int p);
    virtual void setLastModified(const QDateTime &dt);
    void setLastRead(const QDateTime &dt);

    bool isValid() const;

    QString name() const;
    int permissions() const;
    QString owner() const;
    QString group() const;
    qint64 size() const;
    QDateTime lastModified() const;
    QDateTime lastRead() const;
    bool isDir() const;
    bool isFile() const;
    bool isSymLink() const;
    bool isWritable() const;
    bool isReadable() const;
    bool isExecutable() const;

    static bool greaterThan(const QUrlInfo &i1, const QUrlInfo &i2,
                             int sortBy);
    static bool lessThan(const QUrlInfo &i1, const QUrlInfo &i2,
                          int sortBy);
    static bool equal(const QUrlInfo &i1, const QUrlInfo &i2,
                       int sortBy);

    bool operator==(const QUrlInfo &i) const;
    inline bool operator!=(const QUrlInfo &i) const
    { return !operator==(i); }

private:
    QUrlInfoPrivate *d;
};

#endif // QT_NO_FTP

QT_END_NAMESPACE

#endif // QURLINFO_H
