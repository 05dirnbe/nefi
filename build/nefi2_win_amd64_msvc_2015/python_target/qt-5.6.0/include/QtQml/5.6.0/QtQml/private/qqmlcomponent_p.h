/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtQml module of the Qt Toolkit.
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

#ifndef QQMLCOMPONENT_P_H
#define QQMLCOMPONENT_P_H

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

#include "qqmlcomponent.h"

#include "qqmlengine_p.h"
#include "qqmltypeloader_p.h"
#include <private/qbitfield_p.h>
#include "qqmlvme_p.h"
#include "qqmlerror.h"
#include "qqml.h"
#include <private/qqmlobjectcreator_p.h>

#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QList>

#include <private/qobject_p.h>

QT_BEGIN_NAMESPACE

class QV8Engine;

class QQmlComponent;
class QQmlEngine;
class QQmlCompiledData;

class QQmlComponentAttached;
class Q_QML_PRIVATE_EXPORT QQmlComponentPrivate : public QObjectPrivate, public QQmlTypeData::TypeDataCallback
{
    Q_DECLARE_PUBLIC(QQmlComponent)

public:
    QQmlComponentPrivate()
        : typeData(0), progress(0.), start(-1), cc(0), engine(0), creationContext(0), depthIncreased(false) {}

    void loadUrl(const QUrl &newUrl, QQmlComponent::CompilationMode mode = QQmlComponent::PreferSynchronous);

    QObject *beginCreate(QQmlContextData *);
    void completeCreate();
    void initializeObjectWithInitialProperties(const QV4::Value &valuemap, QObject *toCreate);

    QQmlTypeData *typeData;
    virtual void typeDataReady(QQmlTypeData *);
    virtual void typeDataProgress(QQmlTypeData *, qreal);

    void fromTypeData(QQmlTypeData *data);

    QUrl url;
    qreal progress;

    int start;
    QQmlCompiledData *cc;

    struct ConstructionState {
        ConstructionState()
            : completePending(false)
        {}
        ~ConstructionState()
        {
        }

        QScopedPointer<QQmlObjectCreator> creator;
        QList<QQmlError> errors;
        bool completePending;
    };
    ConstructionState state;

    static void beginDeferred(QQmlEnginePrivate *enginePriv, QObject *object,
                              ConstructionState *state);
    static void complete(QQmlEnginePrivate *enginePriv, ConstructionState *state);

    QQmlEngine *engine;
    QQmlGuardedContextData creationContext;
    bool depthIncreased;

    void clear();

    static QQmlComponentPrivate *get(QQmlComponent *c) {
        return static_cast<QQmlComponentPrivate *>(QObjectPrivate::get(c));
    }
};

QT_END_NAMESPACE

#endif // QQMLCOMPONENT_P_H
