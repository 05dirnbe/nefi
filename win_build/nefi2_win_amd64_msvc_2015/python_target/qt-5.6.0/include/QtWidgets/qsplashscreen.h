/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtWidgets module of the Qt Toolkit.
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

#ifndef QSPLASHSCREEN_H
#define QSPLASHSCREEN_H

#include <QtGui/qpixmap.h>
#include <QtWidgets/qwidget.h>

QT_BEGIN_NAMESPACE


#ifndef QT_NO_SPLASHSCREEN
class QSplashScreenPrivate;

class Q_WIDGETS_EXPORT QSplashScreen : public QWidget
{
    Q_OBJECT
public:
    explicit QSplashScreen(const QPixmap &pixmap = QPixmap(), Qt::WindowFlags f = Qt::WindowFlags());
    QSplashScreen(QWidget *parent, const QPixmap &pixmap = QPixmap(), Qt::WindowFlags f = Qt::WindowFlags());
    virtual ~QSplashScreen();

    void setPixmap(const QPixmap &pixmap);
    const QPixmap pixmap() const;
    void finish(QWidget *w);
    void repaint();
    QString message() const;

public Q_SLOTS:
    void showMessage(const QString &message, int alignment = Qt::AlignLeft,
                  const QColor &color = Qt::black);
    void clearMessage();

Q_SIGNALS:
    void messageChanged(const QString &message);

protected:
    bool event(QEvent *e) Q_DECL_OVERRIDE;
    virtual void drawContents(QPainter *painter);
    void mousePressEvent(QMouseEvent *) Q_DECL_OVERRIDE;

private:
    Q_DISABLE_COPY(QSplashScreen)
    Q_DECLARE_PRIVATE(QSplashScreen)
};

#endif // QT_NO_SPLASHSCREEN

QT_END_NAMESPACE

#endif // QSPLASHSCREEN_H
