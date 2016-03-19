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

#ifndef QABSTRACTLAYOUTSTYLEINFO_P_H
#define QABSTRACTLAYOUTSTYLEINFO_P_H

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

#include <QtCore/qnamespace.h>
#include "qlayoutpolicy_p.h"

QT_BEGIN_NAMESPACE


class Q_GUI_EXPORT QAbstractLayoutStyleInfo {
public:

    QAbstractLayoutStyleInfo() : m_isWindow(false) {}
    virtual ~QAbstractLayoutStyleInfo() {}
    virtual qreal combinedLayoutSpacing(QLayoutPolicy::ControlTypes /*controls1*/,
                                        QLayoutPolicy::ControlTypes /*controls2*/, Qt::Orientation /*orientation*/) const {
        return -1;
    }

    virtual qreal perItemSpacing(QLayoutPolicy::ControlType /*control1*/,
                                 QLayoutPolicy::ControlType /*control2*/,
                                 Qt::Orientation /*orientation*/) const {
        return -1;
    }

    virtual qreal spacing(Qt::Orientation orientation) const = 0;

    virtual bool hasChangedCore() const { return false; }   // ### Remove when usage is gone from subclasses

    virtual void invalidate() { }

    virtual qreal windowMargin(Qt::Orientation orientation) const = 0;

    bool isWindow() const {
        return m_isWindow;
    }

protected:
    unsigned m_isWindow : 1;
    mutable unsigned m_hSpacingState: 2;
    mutable unsigned m_vSpacingState: 2;
    mutable qreal m_spacing[2];
};

QT_END_NAMESPACE

#endif // QABSTRACTLAYOUTSTYLEINFO_P_H
