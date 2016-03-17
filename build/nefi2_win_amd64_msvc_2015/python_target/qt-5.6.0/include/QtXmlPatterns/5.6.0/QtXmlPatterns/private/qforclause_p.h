/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtXmlPatterns module of the Qt Toolkit.
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

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists purely as an
// implementation detail.  This header file may change from version to
// version without notice, or even be removed.
//
// We mean it.

#ifndef Patternist_ForClause_H
#define Patternist_ForClause_H

#include <private/qpaircontainer_p.h>

QT_BEGIN_NAMESPACE

namespace QPatternist
{

    /**
     * @short Implements XPath 2.0's @c for expression.
     *
     * @see <a href="http://www.w3.org/TR/xpath20/#id-for-expressions">XML Path Language
     * (XPath) 2.0, 3.7 For Expressions</a>
     * @author Frans Englich <frans.englich@nokia.com>
     * @ingroup Patternist_expressions
     */
    class ForClause : public PairContainer
    {
    public:
        /**
         * If @p positionSlot is -1, no positional variable will be used.
         */
        ForClause(const VariableSlotID varSlot,
                  const Expression::Ptr &bindingSequence,
                  const Expression::Ptr &returnExpression,
                  const VariableSlotID positionSlot);

        virtual Item::Iterator::Ptr evaluateSequence(const DynamicContext::Ptr &context) const;
        virtual Item evaluateSingleton(const DynamicContext::Ptr &context) const;
        virtual void evaluateToSequenceReceiver(const DynamicContext::Ptr &context) const;

        virtual SequenceType::Ptr staticType() const;
        virtual SequenceType::List expectedOperandTypes() const;
        virtual Expression::Ptr typeCheck(const StaticContext::Ptr &context,
                                          const SequenceType::Ptr &reqType);
        virtual ExpressionVisitorResult::Ptr accept(const ExpressionVisitor::Ptr &visitor) const;
        virtual QList<QExplicitlySharedDataPointer<OptimizationPass> > optimizationPasses() const;

        inline Item mapToItem(const Item &item,
                              const DynamicContext::Ptr &context) const;
        virtual ID id() const;
        inline Item::Iterator::Ptr mapToSequence(const Item &item,
                                                 const DynamicContext::Ptr &context) const;

        /**
         * Sets m_allowsMany properly.
         */
        virtual Expression::Ptr compress(const StaticContext::Ptr &context);

    private:
        inline void riggPositionalVariable(const DynamicContext::Ptr &context,
                                           const Item::Iterator::Ptr &source) const;
        typedef QExplicitlySharedDataPointer<const ForClause> ConstPtr;
        const VariableSlotID m_varSlot;
        const VariableSlotID m_positionSlot;
        /**
         * Initialized to @c false. This default is always safe.
         */
        bool m_allowsMany;
    };
}

QT_END_NAMESPACE

#endif
