/****************************************************************************
**
** Copyright (C) 2012 David Faure <faure@kde.org>
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

#ifndef QSAVEFILE_H
#define QSAVEFILE_H

#include <QtCore/qglobal.h>

#ifndef QT_NO_TEMPORARYFILE

#include <QtCore/qfiledevice.h>
#include <QtCore/qstring.h>

#ifdef open
#error qsavefile.h must be included before any header file that defines open
#endif

QT_BEGIN_NAMESPACE

class QAbstractFileEngine;
class QSaveFilePrivate;

class Q_CORE_EXPORT QSaveFile : public QFileDevice
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QSaveFile)

public:

    explicit QSaveFile(const QString &name);
    explicit QSaveFile(QObject *parent = Q_NULLPTR);
    explicit QSaveFile(const QString &name, QObject *parent);
    ~QSaveFile();

    QString fileName() const Q_DECL_OVERRIDE;
    void setFileName(const QString &name);

    bool open(OpenMode flags) Q_DECL_OVERRIDE;
    bool commit();

    void cancelWriting();

    void setDirectWriteFallback(bool enabled);
    bool directWriteFallback() const;

protected:
    qint64 writeData(const char *data, qint64 len) Q_DECL_OVERRIDE;

private:
    void close() Q_DECL_OVERRIDE;

private:
    Q_DISABLE_COPY(QSaveFile)
};

QT_END_NAMESPACE

#endif // QT_NO_TEMPORARYFILE

#endif // QSAVEFILE_H
