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

#ifndef QSIGNALMAPPER_H
#define QSIGNALMAPPER_H

#include <QtCore/qobject.h>

QT_BEGIN_NAMESPACE

class QSignalMapperPrivate;

class Q_CORE_EXPORT QSignalMapper : public QObject
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QSignalMapper)
public:
    explicit QSignalMapper(QObject *parent = Q_NULLPTR);
    ~QSignalMapper();

    void setMapping(QObject *sender, int id);
    void setMapping(QObject *sender, const QString &text);
    void setMapping(QObject *sender, QWidget *widget);
    void setMapping(QObject *sender, QObject *object);
    void removeMappings(QObject *sender);

    QObject *mapping(int id) const;
    QObject *mapping(const QString &text) const;
    QObject *mapping(QWidget *widget) const;
    QObject *mapping(QObject *object) const;

Q_SIGNALS:
    void mapped(int);
    void mapped(const QString &);
    void mapped(QWidget *);
    void mapped(QObject *);

public Q_SLOTS:
    void map();
    void map(QObject *sender);

private:
    Q_DISABLE_COPY(QSignalMapper)
    Q_PRIVATE_SLOT(d_func(), void _q_senderDestroyed())
};

QT_END_NAMESPACE

#endif // QSIGNALMAPPER_H
