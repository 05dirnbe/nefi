/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtTest module of the Qt Toolkit.
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

#ifndef QXCTESTLOGGER_P_H
#define QXCTESTLOGGER_P_H

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

#include <QtTest/private/qabstracttestlogger_p.h>

#include <dispatch/dispatch.h>

Q_FORWARD_DECLARE_OBJC_CLASS(XCTest);
Q_FORWARD_DECLARE_OBJC_CLASS(XCTestRun);
Q_FORWARD_DECLARE_OBJC_CLASS(NSMutableArray);

QT_BEGIN_NAMESPACE

class QXcodeTestLogger : public QAbstractTestLogger
{
public:
    QXcodeTestLogger();
    ~QXcodeTestLogger() Q_DECL_OVERRIDE;

    void startLogging() Q_DECL_OVERRIDE;
    void stopLogging() Q_DECL_OVERRIDE;

    void enterTestFunction(const char *function) Q_DECL_OVERRIDE;
    void leaveTestFunction() Q_DECL_OVERRIDE;

    void addIncident(IncidentTypes type, const char *description,
        const char *file = 0, int line = 0) Q_DECL_OVERRIDE;

    void addMessage(MessageTypes type, const QString &message,
        const char *file = 0, int line = 0) Q_DECL_OVERRIDE;

    void addBenchmarkResult(const QBenchmarkResult &result) Q_DECL_OVERRIDE;

    static bool canLogTestProgress();
    static int parseCommandLineArgument(const char *argument);

    static bool isActive();

private:
    void pushTestRunForTest(XCTest *test, bool start);
    XCTestRun *popTestRun();

    NSMutableArray *m_testRuns;

    static QXcodeTestLogger *s_currentTestLogger;
};


QT_END_NAMESPACE

#endif
