/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the plugins of the Qt Toolkit.
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

#ifndef QMACMIME_H
#define QMACMIME_H

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

#include <QtCore>

#include <CoreFoundation/CoreFoundation.h>

QT_BEGIN_NAMESPACE

// Duplicate of QMacPasteboardMime in QtMacExtras. Keep in sync!
class QMacInternalPasteboardMime {
    char type;
public:
    enum QMacPasteboardMimeType { MIME_DND=0x01,
        MIME_CLIP=0x02,
        MIME_QT_CONVERTOR=0x04,
        MIME_QT3_CONVERTOR=0x08,
        MIME_ALL=MIME_DND|MIME_CLIP
    };
    explicit QMacInternalPasteboardMime(char);
    virtual ~QMacInternalPasteboardMime();

    static void initializeMimeTypes();
    static void destroyMimeTypes();

    static QList<QMacInternalPasteboardMime*> all(uchar);
    static QMacInternalPasteboardMime *convertor(uchar, const QString &mime, QString flav);
    static QString flavorToMime(uchar, QString flav);

    virtual QString convertorName() = 0;

    virtual bool canConvert(const QString &mime, QString flav) = 0;
    virtual QString mimeFor(QString flav) = 0;
    virtual QString flavorFor(const QString &mime) = 0;
    virtual QVariant convertToMime(const QString &mime, QList<QByteArray> data, QString flav) = 0;
    virtual QList<QByteArray> convertFromMime(const QString &mime, QVariant data, QString flav) = 0;
    virtual int count(QMimeData *mimeData);
};

void qt_mac_addToGlobalMimeList(QMacInternalPasteboardMime *macMime);
void qt_mac_removeFromGlobalMimeList(QMacInternalPasteboardMime *macMime);
void qt_mac_registerDraggedTypes(const QStringList &types);
const QStringList& qt_mac_enabledDraggedTypes();

QT_END_NAMESPACE

#endif

