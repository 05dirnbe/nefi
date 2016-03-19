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

#ifndef QINPUTMETHOD_H
#define QINPUTMETHOD_H

#include <QtCore/qobject.h>

QT_BEGIN_NAMESPACE

class QInputMethodPrivate;
class QWindow;
class QRectF;
class QTransform;
class QInputMethodQueryEvent;

class Q_GUI_EXPORT QInputMethod : public QObject
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QInputMethod)
    Q_PROPERTY(QRectF cursorRectangle READ cursorRectangle NOTIFY cursorRectangleChanged)
    Q_PROPERTY(QRectF keyboardRectangle READ keyboardRectangle NOTIFY keyboardRectangleChanged)
    Q_PROPERTY(bool visible READ isVisible NOTIFY visibleChanged)
    Q_PROPERTY(bool animating READ isAnimating NOTIFY animatingChanged)
    Q_PROPERTY(QLocale locale READ locale NOTIFY localeChanged)
    Q_PROPERTY(Qt::LayoutDirection inputDirection READ inputDirection NOTIFY inputDirectionChanged)

public:
    QTransform inputItemTransform() const;
    void setInputItemTransform(const QTransform &transform);

    QRectF inputItemRectangle() const;
    void setInputItemRectangle(const QRectF &rect);

    // in window coordinates
    QRectF cursorRectangle() const; // ### what if we have rotations for the item?

    // keyboard geometry in window coords
    QRectF keyboardRectangle() const;

    enum Action {
        Click,
        ContextMenu
    };
    Q_ENUM(Action)

    bool isVisible() const;
    void setVisible(bool visible);

    bool isAnimating() const;

    QLocale locale() const;
    Qt::LayoutDirection inputDirection() const;

    static QVariant queryFocusObject(Qt::InputMethodQuery query, QVariant argument); // ### Qt 6: QVariant by const-ref

public Q_SLOTS:
    void show();
    void hide();

    void update(Qt::InputMethodQueries queries);
    void reset();
    void commit();

    void invokeAction(Action a, int cursorPosition);

Q_SIGNALS:
    void cursorRectangleChanged();
    void keyboardRectangleChanged();
    void visibleChanged();
    void animatingChanged();
    void localeChanged();
    void inputDirectionChanged(Qt::LayoutDirection newDirection);

private:
    friend class QGuiApplication;
    friend class QGuiApplicationPrivate;
    friend class QPlatformInputContext;
    QInputMethod();
    ~QInputMethod();
};

QT_END_NAMESPACE

#endif
