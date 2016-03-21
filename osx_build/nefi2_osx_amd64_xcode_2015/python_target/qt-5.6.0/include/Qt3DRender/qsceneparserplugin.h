/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd and/or its subsidiary(-ies).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the Qt3D module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL3$
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
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or later as published by the Free
** Software Foundation and appearing in the file LICENSE.GPL included in
** the packaging of this file. Please review the following information to
** ensure the GNU General Public License version 2.0 requirements will be
** met: http://www.gnu.org/licenses/gpl-2.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QSCENEPARSERPLUGIN_H
#define QSCENEPARSERPLUGIN_H

#include <QtCore/QObject>
#include <QtCore/QtPlugin>
#include <QtCore/QFactoryInterface>

#include <Qt3DRender/qt3drender_global.h>

QT_BEGIN_NAMESPACE

namespace Qt3DRender {

#define QSceneParserFactoryInterface_iid "org.qt-project.Qt3DRender.QSceneParserFactoryInterface 5.6"

class QAbstractSceneParser;

class QT3DRENDERSHARED_EXPORT QSceneParserPlugin : public QObject
{
    Q_OBJECT
public:
    explicit QSceneParserPlugin(QObject *parent = 0);
    ~QSceneParserPlugin();

    virtual QAbstractSceneParser *create(const QString &key, const QStringList &paramList);
};

} // namespace Qt3DRender

QT_END_NAMESPACE

#endif // QSCENEPARSERPLUGIN_H
