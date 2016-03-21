/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtPrintSupport module of the Qt Toolkit.
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


#ifndef QCUPSJOBWIDGET_P_H
#define QCUPSJOBWIDGET_P_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists purely as an
// implementation detail.  This header file may change from version to
// to version without notice, or even be removed.
//
// We mean it.
//
//

#include <ui_qcupsjobwidget.h>
#include <private/qcups_p.h>

QT_BEGIN_NAMESPACE

#if !defined(QT_NO_PRINTER) && !defined(QT_NO_CUPS)

class QString;
class QTime;
class QPrinter;

class QCupsJobWidget : public QWidget
{
    Q_OBJECT

public:
    explicit QCupsJobWidget(QWidget *parent = 0);
    ~QCupsJobWidget();
    void setPrinter(QPrinter *printer);
    void setupPrinter();

private Q_SLOTS:
    void toggleJobHoldTime();

private:

    void setJobHold(QCUPSSupport::JobHoldUntil jobHold = QCUPSSupport::NoHold, const QTime &holdUntilTime = QTime());
    QCUPSSupport::JobHoldUntil jobHold() const;
    QTime jobHoldTime() const;

    void setJobBilling(const QString &jobBilling = QString());
    QString jobBilling() const;

    void setJobPriority(int priority = 50);
    int jobPriority() const;

    void setStartBannerPage(const QCUPSSupport::BannerPage bannerPage = QCUPSSupport::NoBanner);
    QCUPSSupport::BannerPage startBannerPage() const;

    void setEndBannerPage(const QCUPSSupport::BannerPage bannerPage = QCUPSSupport::NoBanner);
    QCUPSSupport::BannerPage endBannerPage() const;

    void initJobHold();
    void initJobBilling();
    void initJobPriority();
    void initBannerPages();

    QPrinter *m_printer;
    Ui::QCupsJobWidget m_ui;

    Q_DISABLE_COPY(QCupsJobWidget)
};

#endif // QT_NO_PRINTER / QT_NO_CUPS

QT_END_NAMESPACE

#endif  // QCUPSJOBWIDGET_P_H
