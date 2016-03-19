/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtCore module of the Qt Toolkit.
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

#ifndef QJNIHELPERS_H
#define QJNIHELPERS_H

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

#include <jni.h>
#include <QtCore/qglobal.h>

QT_BEGIN_NAMESPACE

class QRunnable;

namespace QtAndroidPrivate
{
    class Q_CORE_EXPORT ActivityResultListener
    {
    public:
        virtual ~ActivityResultListener() {}
        virtual bool handleActivityResult(jint requestCode, jint resultCode, jobject data) = 0;
    };

    class Q_CORE_EXPORT NewIntentListener
    {
    public:
        virtual ~NewIntentListener() {}
        virtual bool handleNewIntent(JNIEnv *env, jobject intent) = 0;
    };

    class Q_CORE_EXPORT ResumePauseListener
    {
    public:
        virtual ~ResumePauseListener() {}
        virtual void handlePause() {};
        virtual void handleResume() {};
    };

    class Q_CORE_EXPORT GenericMotionEventListener
    {
    public:
        virtual ~GenericMotionEventListener() {}
        virtual bool handleGenericMotionEvent(jobject event) = 0;
    };

    class Q_CORE_EXPORT KeyEventListener
    {
    public:
        virtual ~KeyEventListener() {}
        virtual bool handleKeyEvent(jobject event) = 0;
    };

    Q_CORE_EXPORT jobject activity();
    Q_CORE_EXPORT JavaVM *javaVM();
    Q_CORE_EXPORT jint initJNI(JavaVM *vm, JNIEnv *env);
    jobject classLoader();
    Q_CORE_EXPORT jint androidSdkVersion();
    Q_CORE_EXPORT void runOnUiThread(QRunnable *runnable, JNIEnv *env);

    Q_CORE_EXPORT void handleActivityResult(jint requestCode, jint resultCode, jobject data);
    Q_CORE_EXPORT void registerActivityResultListener(ActivityResultListener *listener);
    Q_CORE_EXPORT void unregisterActivityResultListener(ActivityResultListener *listener);

    Q_CORE_EXPORT void handleNewIntent(JNIEnv *env, jobject intent);
    Q_CORE_EXPORT void registerNewIntentListener(NewIntentListener *listener);
    Q_CORE_EXPORT void unregisterNewIntentListener(NewIntentListener *listener);

    Q_CORE_EXPORT void handlePause();
    Q_CORE_EXPORT void handleResume();
    Q_CORE_EXPORT void registerResumePauseListener(ResumePauseListener *listener);
    Q_CORE_EXPORT void unregisterResumePauseListener(ResumePauseListener *listener);

    Q_CORE_EXPORT void registerGenericMotionEventListener(GenericMotionEventListener *listener);
    Q_CORE_EXPORT void unregisterGenericMotionEventListener(GenericMotionEventListener *listener);

    Q_CORE_EXPORT void registerKeyEventListener(KeyEventListener *listener);
    Q_CORE_EXPORT void unregisterKeyEventListener(KeyEventListener *listener);
}

QT_END_NAMESPACE

#endif // QJNIHELPERS_H
