/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtGui module of the Qt Toolkit.
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

#ifndef QICONENGINE_H
#define QICONENGINE_H

#include <QtCore/qglobal.h>
#include <QtCore/qlist.h>
#include <QtGui/qicon.h>

QT_BEGIN_NAMESPACE


class Q_GUI_EXPORT QIconEngine
{
public:
    QIconEngine();
    virtual ~QIconEngine();
    virtual void paint(QPainter *painter, const QRect &rect, QIcon::Mode mode, QIcon::State state) = 0;
    virtual QSize actualSize(const QSize &size, QIcon::Mode mode, QIcon::State state);
    virtual QPixmap pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state);

    virtual void addPixmap(const QPixmap &pixmap, QIcon::Mode mode, QIcon::State state);
    virtual void addFile(const QString &fileName, const QSize &size, QIcon::Mode mode, QIcon::State state);

    virtual QString key() const;
    virtual QIconEngine *clone() const = 0;
    virtual bool read(QDataStream &in);
    virtual bool write(QDataStream &out) const;

    enum IconEngineHook { AvailableSizesHook = 1, IconNameHook };

    struct AvailableSizesArgument
    {
        QIcon::Mode mode;
        QIcon::State state;
        QList<QSize> sizes;
    };

    virtual QList<QSize> availableSizes(QIcon::Mode mode = QIcon::Normal,
                                    QIcon::State state = QIcon::Off) const;

    virtual QString iconName() const;

    virtual void virtual_hook(int id, void *data);
};

#if QT_DEPRECATED_SINCE(5, 0)
typedef QIconEngine QIconEngineV2;
#endif

QT_END_NAMESPACE

#endif // QICONENGINE_H
