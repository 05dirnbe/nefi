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

#ifndef QABSTRACTPRINTDIALOG_H
#define QABSTRACTPRINTDIALOG_H

#include <QtWidgets/qdialog.h>
#include <QtPrintSupport/qtprintsupportglobal.h>

QT_BEGIN_NAMESPACE


#ifndef QT_NO_PRINTER

class QAbstractPrintDialogPrivate;
class QPrinter;

// ### QtPrintNG: merge this class with QPrintDialog
class Q_PRINTSUPPORT_EXPORT QAbstractPrintDialog : public QDialog
{
    Q_DECLARE_PRIVATE(QAbstractPrintDialog)
    Q_OBJECT

public:
    // Keep in sync with QPrinter::PrintRange
    enum PrintRange {
        AllPages,
        Selection,
        PageRange,
        CurrentPage
    };

    enum PrintDialogOption {
        None                    = 0x0000, // obsolete
        PrintToFile             = 0x0001,
        PrintSelection          = 0x0002,
        PrintPageRange          = 0x0004,
        PrintShowPageSize       = 0x0008,
        PrintCollateCopies      = 0x0010,
        DontUseSheet            = 0x0020,
        PrintCurrentPage        = 0x0040
    };

    Q_DECLARE_FLAGS(PrintDialogOptions, PrintDialogOption)

#ifndef QT_NO_PRINTDIALOG
    explicit QAbstractPrintDialog(QPrinter *printer, QWidget *parent = Q_NULLPTR);
    ~QAbstractPrintDialog();

    virtual int exec() = 0;

    // obsolete
    void addEnabledOption(PrintDialogOption option);
    void setEnabledOptions(PrintDialogOptions options);
    PrintDialogOptions enabledOptions() const;
    bool isOptionEnabled(PrintDialogOption option) const;

    void setOptionTabs(const QList<QWidget*> &tabs);

    void setPrintRange(PrintRange range);
    PrintRange printRange() const;

    void setMinMax(int min, int max);
    int minPage() const;
    int maxPage() const;

    void setFromTo(int fromPage, int toPage);
    int fromPage() const;
    int toPage() const;

    QPrinter *printer() const;

protected:
    QAbstractPrintDialog(QAbstractPrintDialogPrivate &ptr, QPrinter *printer, QWidget *parent = Q_NULLPTR);

private:
    Q_DISABLE_COPY(QAbstractPrintDialog)

#endif // QT_NO_PRINTDIALOG
};

Q_DECLARE_OPERATORS_FOR_FLAGS(QAbstractPrintDialog::PrintDialogOptions)

#endif // QT_NO_PRINTER

QT_END_NAMESPACE

#endif // QABSTRACTPRINTDIALOG_H
