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

#ifndef QDIALOG_H
#define QDIALOG_H

#include <QtWidgets/qwidget.h>

QT_BEGIN_NAMESPACE


class QPushButton;
class QDialogPrivate;

class Q_WIDGETS_EXPORT QDialog : public QWidget
{
    Q_OBJECT
    friend class QPushButton;

    Q_PROPERTY(bool sizeGripEnabled READ isSizeGripEnabled WRITE setSizeGripEnabled)
    Q_PROPERTY(bool modal READ isModal WRITE setModal)

public:
    explicit QDialog(QWidget *parent = Q_NULLPTR, Qt::WindowFlags f = Qt::WindowFlags());
    ~QDialog();

    enum DialogCode { Rejected, Accepted };

    int result() const;

    void setVisible(bool visible);

    void setOrientation(Qt::Orientation orientation);
    Qt::Orientation orientation() const;

    void setExtension(QWidget* extension);
    QWidget* extension() const;

    QSize sizeHint() const;
    QSize minimumSizeHint() const;

    void setSizeGripEnabled(bool);
    bool isSizeGripEnabled() const;

    void setModal(bool modal);
    void setResult(int r);

Q_SIGNALS:
    void finished(int result);
    void accepted();
    void rejected();

public Q_SLOTS:
    virtual void open();
    virtual int exec();
    virtual void done(int);
    virtual void accept();
    virtual void reject();

    void showExtension(bool);

protected:
    QDialog(QDialogPrivate &, QWidget *parent, Qt::WindowFlags f = Qt::WindowFlags());

#if defined(Q_OS_WINCE)
    bool event(QEvent *e);
#endif
    void keyPressEvent(QKeyEvent *);
    void closeEvent(QCloseEvent *);
    void showEvent(QShowEvent *);
    void resizeEvent(QResizeEvent *);
#ifndef QT_NO_CONTEXTMENU
    void contextMenuEvent(QContextMenuEvent *);
#endif
    bool eventFilter(QObject *, QEvent *);
    void adjustPosition(QWidget*);
private:
    Q_DECLARE_PRIVATE(QDialog)
    Q_DISABLE_COPY(QDialog)

#ifdef Q_OS_WINCE_WM
    Q_PRIVATE_SLOT(d_func(), void _q_doneAction())
#endif
};

QT_END_NAMESPACE

#endif // QDIALOG_H
