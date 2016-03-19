/****************************************************************************
 **
 ** Copyright (C) 2013 Ivan Vizir <define-true-false@yandex.com>
 ** Copyright (C) 2015 The Qt Company Ltd.
 ** Contact: http://www.qt.io/licensing/
 **
 ** This file is part of the QtWinExtras module of the Qt Toolkit.
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

#ifndef QWINJUMPLISTITEM_H
#define QWINJUMPLISTITEM_H

#include <QtGui/qicon.h>
#include <QtCore/qobject.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qscopedpointer.h>
#include <QtWinExtras/qwinextrasglobal.h>

QT_BEGIN_NAMESPACE

class QWinJumpListItemPrivate;

class Q_WINEXTRAS_EXPORT QWinJumpListItem
{
public:
    enum Type {
        Destination,
        Link,
        Separator
    };

    explicit QWinJumpListItem(Type type);
    ~QWinJumpListItem();

    void setType(Type type);
    Type type() const;
    void setFilePath(const QString &filePath);
    QString filePath() const;
    void setWorkingDirectory(const QString &workingDirectory);
    QString workingDirectory() const;
    void setIcon(const QIcon &icon);
    QIcon icon() const;
    void setTitle(const QString &title);
    QString title() const;
    void setDescription(const QString &description);
    QString description() const;
    void setArguments(const QStringList &arguments);
    QStringList arguments() const;

private:
    Q_DISABLE_COPY(QWinJumpListItem)
    Q_DECLARE_PRIVATE(QWinJumpListItem)
    QScopedPointer<QWinJumpListItemPrivate> d_ptr;
};

#ifndef QT_NO_DEBUG_STREAM
Q_WINEXTRAS_EXPORT QDebug operator<<(QDebug, const QWinJumpListItem *);
#endif

QT_END_NAMESPACE

#endif // QWINJUMPLISTITEM_H
