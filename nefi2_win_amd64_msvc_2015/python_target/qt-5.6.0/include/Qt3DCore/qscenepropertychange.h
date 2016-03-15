/****************************************************************************
**
** Copyright (C) 2014 Klaralvdalens Datakonsult AB (KDAB).
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

#ifndef QT3DCORE_QSCENEPROPERTYCHANGE_H
#define QT3DCORE_QSCENEPROPERTYCHANGE_H

#include <Qt3DCore/qscenechange.h>

QT_BEGIN_NAMESPACE

namespace Qt3DCore {

class QScenePropertyChangePrivate;

class QT3DCORESHARED_EXPORT QScenePropertyChange : public QSceneChange
{
public:
    QScenePropertyChange(ChangeFlag type, ObservableType observableType, const QNodeId &subjectId, Priority priority = Standard);
    virtual ~QScenePropertyChange();

    const char *propertyName() const;
    QVariant value() const;

    void setPropertyName(const char *name);
    void setValue(const QVariant &value);

    static void *operator new(size_t size);
    static void operator delete(void *ptr, size_t size);

protected:
    Q_DECLARE_PRIVATE(QScenePropertyChange)
    QScenePropertyChange(QScenePropertyChangePrivate &dd);
    QScenePropertyChange(QScenePropertyChangePrivate &dd, ChangeFlag type, ObservableType observableType, const QNodeId &subjectId, Priority priority = Standard);
};

typedef QSharedPointer<QScenePropertyChange> QScenePropertyChangePtr;

} // namespace Qt3DCore

QT_END_NAMESPACE

#endif // QT3DCORE_QSCENEPROPERTYCHANGE_H
