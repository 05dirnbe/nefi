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

#ifndef QPICTUREFORMATPLUGIN_H
#define QPICTUREFORMATPLUGIN_H

#include <QtCore/qplugin.h>
#include <QtCore/qfactoryinterface.h>

QT_BEGIN_NAMESPACE


#if !defined(QT_NO_LIBRARY) && !defined(QT_NO_PICTURE)

class QPicture;
class QImage;
class QString;
class QStringList;

#define QPictureFormatInterface_iid "org.qt-project.Qt.QPictureFormatInterface"

class Q_GUI_EXPORT QPictureFormatPlugin : public QObject
{
    Q_OBJECT
public:
    explicit QPictureFormatPlugin(QObject *parent = Q_NULLPTR);
    ~QPictureFormatPlugin();

    virtual bool loadPicture(const QString &format, const QString &filename, QPicture *pic);
    virtual bool savePicture(const QString &format, const QString &filename, const QPicture &pic);
    virtual bool installIOHandler(const QString &format) = 0;

};

#endif // QT_NO_LIBRARY || QT_NO_PICTURE

QT_END_NAMESPACE

#endif // QPICTUREFORMATPLUGIN_H
