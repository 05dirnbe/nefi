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

#ifndef QPLATFORMINTEGRATIONPLUGIN_H
#define QPLATFORMINTEGRATIONPLUGIN_H

//
//  W A R N I N G
//  -------------
//
// This file is part of the QPA API and is not meant to be used
// in applications. Usage of this API may make your code
// source and binary incompatible with future versions of Qt.
//

#include <QtCore/qplugin.h>
#include <QtCore/qfactoryinterface.h>

QT_BEGIN_NAMESPACE


class QPlatformIntegration;

#define QPlatformIntegrationFactoryInterface_iid "org.qt-project.Qt.QPA.QPlatformIntegrationFactoryInterface.5.3"

class Q_GUI_EXPORT QPlatformIntegrationPlugin : public QObject
{
    Q_OBJECT
public:
    explicit QPlatformIntegrationPlugin(QObject *parent = 0);
    ~QPlatformIntegrationPlugin();

    virtual QPlatformIntegration *create(const QString &key, const QStringList &paramList);
    virtual QPlatformIntegration *create(const QString &key, const QStringList &paramList, int &argc, char **argv);
};

QT_END_NAMESPACE

#endif // QPLATFORMINTEGRATIONPLUGIN_H
