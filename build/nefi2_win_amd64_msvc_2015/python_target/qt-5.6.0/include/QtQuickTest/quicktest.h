/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the test suite of the Qt Toolkit.
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

#ifndef QUICKTEST_H
#define QUICKTEST_H

#include <QtQuickTest/quicktestglobal.h>
#include <QtTest/qtest.h>

QT_BEGIN_NAMESPACE

QTEST_ADD_GPU_BLACKLIST_SUPPORT_DEFS

Q_QUICK_TEST_EXPORT int quick_test_main(int argc, char **argv, const char *name, const char *sourceDir);

#ifdef QUICK_TEST_SOURCE_DIR

#define QUICK_TEST_MAIN(name) \
    int main(int argc, char **argv) \
    { \
        QTEST_ADD_GPU_BLACKLIST_SUPPORT \
        QTEST_SET_MAIN_SOURCE_PATH \
        return quick_test_main(argc, argv, #name, QUICK_TEST_SOURCE_DIR); \
    }

#define QUICK_TEST_OPENGL_MAIN(name) \
    int main(int argc, char **argv) \
    { \
        QTEST_ADD_GPU_BLACKLIST_SUPPORT \
        QTEST_SET_MAIN_SOURCE_PATH \
        return quick_test_main(argc, argv, #name, QUICK_TEST_SOURCE_DIR); \
    }

#else

#define QUICK_TEST_MAIN(name) \
    int main(int argc, char **argv) \
    { \
        QTEST_ADD_GPU_BLACKLIST_SUPPORT \
        QTEST_SET_MAIN_SOURCE_PATH \
        return quick_test_main(argc, argv, #name, 0); \
    }

#define QUICK_TEST_OPENGL_MAIN(name) \
    int main(int argc, char **argv) \
    { \
        QTEST_ADD_GPU_BLACKLIST_SUPPORT \
        QTEST_SET_MAIN_SOURCE_PATH \
        return quick_test_main(argc, argv, #name, 0); \
    }

#endif

QT_END_NAMESPACE

#endif
