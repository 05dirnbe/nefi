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

#ifndef QHISTORYSTATE_H
#define QHISTORYSTATE_H

#include <QtCore/qabstractstate.h>

QT_BEGIN_NAMESPACE


#ifndef QT_NO_STATEMACHINE

class QAbstractTransition;
class QHistoryStatePrivate;
class Q_CORE_EXPORT QHistoryState : public QAbstractState
{
    Q_OBJECT
    Q_PROPERTY(QAbstractState* defaultState READ defaultState WRITE setDefaultState NOTIFY defaultStateChanged)
    Q_PROPERTY(QAbstractTransition* defaultTransition READ defaultTransition WRITE setDefaultTransition NOTIFY defaultTransitionChanged)
    Q_PROPERTY(HistoryType historyType READ historyType WRITE setHistoryType NOTIFY historyTypeChanged)
public:
    enum HistoryType {
        ShallowHistory,
        DeepHistory
    };
    Q_ENUM(HistoryType)

    QHistoryState(QState *parent = Q_NULLPTR);
    QHistoryState(HistoryType type, QState *parent = Q_NULLPTR);
    ~QHistoryState();

    QAbstractTransition *defaultTransition() const;
    void setDefaultTransition(QAbstractTransition *transition);

    QAbstractState *defaultState() const;
    void setDefaultState(QAbstractState *state);

    HistoryType historyType() const;
    void setHistoryType(HistoryType type);

Q_SIGNALS:
    void defaultTransitionChanged(QPrivateSignal);
    void defaultStateChanged(QPrivateSignal);
    void historyTypeChanged(QPrivateSignal);

protected:
    void onEntry(QEvent *event) Q_DECL_OVERRIDE;
    void onExit(QEvent *event) Q_DECL_OVERRIDE;

    bool event(QEvent *e) Q_DECL_OVERRIDE;

private:
    Q_DISABLE_COPY(QHistoryState)
    Q_DECLARE_PRIVATE(QHistoryState)
};

#endif //QT_NO_STATEMACHINE

QT_END_NAMESPACE

#endif
