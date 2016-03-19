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

#ifndef QQMLBINDING_P_H
#define QQMLBINDING_P_H

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

#include "qqml.h"
#include "qqmlpropertyvaluesource.h"
#include "qqmlexpression.h"
#include "qqmlproperty.h"
#include "qqmlscriptstring.h"
#include "qqmlproperty_p.h"

#include <QtCore/QObject>
#include <QtCore/QMetaProperty>

#include <private/qpointervaluepair_p.h>
#include <private/qqmlabstractbinding_p.h>
#include <private/qqmljavascriptexpression_p.h>

QT_BEGIN_NAMESPACE

class QQmlContext;
class Q_QML_PRIVATE_EXPORT QQmlBinding : public QQmlJavaScriptExpression,
                                         public QQmlAbstractBinding
{
    friend class QQmlAbstractBinding;
public:
    QQmlBinding(const QString &, QObject *, QQmlContext *);
    QQmlBinding(const QQmlScriptString &, QObject *, QQmlContext *);
    QQmlBinding(const QString &, QObject *, QQmlContextData *);
    QQmlBinding(const QString &, QObject *, QQmlContextData *,
                const QString &url, quint16 lineNumber, quint16 columnNumber);
    QQmlBinding(const QV4::Value &, QObject *, QQmlContextData *);
    ~QQmlBinding();

    void setTarget(const QQmlProperty &);
    void setTarget(QObject *, const QQmlPropertyData &);

    void setNotifyOnValueChanged(bool);

    // Inherited from QQmlJavaScriptExpression
    virtual void refresh();

    // Inherited from QQmlAbstractBinding
    virtual void setEnabled(bool, QQmlPropertyPrivate::WriteFlags flags = QQmlPropertyPrivate::DontRemoveBinding);
    virtual QString expression() const;
    void update(QQmlPropertyPrivate::WriteFlags flags = QQmlPropertyPrivate::DontRemoveBinding);

    typedef int Identifier;
    enum {
        Invalid = -1
    };

    QVariant evaluate();

    virtual QString expressionIdentifier();
    virtual void expressionChanged();

private:
    inline bool updatingFlag() const;
    inline void setUpdatingFlag(bool);
    inline bool enabledFlag() const;
    inline void setEnabledFlag(bool);
    QQmlPropertyData getPropertyData() const;

    bool write(const QQmlPropertyData &core,
                       const QV4::Value &result, bool isUndefined,
                       QQmlPropertyPrivate::WriteFlags flags);

};

bool QQmlBinding::updatingFlag() const
{
    return m_target.flag();
}

void QQmlBinding::setUpdatingFlag(bool v)
{
    m_target.setFlagValue(v);
}

bool QQmlBinding::enabledFlag() const
{
    return m_target.flag2();
}

void QQmlBinding::setEnabledFlag(bool v)
{
    m_target.setFlag2Value(v);
}

QT_END_NAMESPACE

Q_DECLARE_METATYPE(QQmlBinding*)

#endif // QQMLBINDING_P_H
