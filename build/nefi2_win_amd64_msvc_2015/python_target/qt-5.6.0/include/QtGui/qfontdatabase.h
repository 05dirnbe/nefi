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

#ifndef QFONTDATABASE_H
#define QFONTDATABASE_H

#include <QtGui/qwindowdefs.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>

QT_BEGIN_NAMESPACE


class QStringList;
template <class T> class QList;
struct QFontDef;
class QFontEngine;

class QFontDatabasePrivate;

class Q_GUI_EXPORT QFontDatabase
{
    Q_GADGET
public:
    // do not re-order or delete entries from this enum without updating the
    // QPF2 format and makeqpf!!
    enum WritingSystem {
        Any,

        Latin,
        Greek,
        Cyrillic,
        Armenian,
        Hebrew,
        Arabic,
        Syriac,
        Thaana,
        Devanagari,
        Bengali,
        Gurmukhi,
        Gujarati,
        Oriya,
        Tamil,
        Telugu,
        Kannada,
        Malayalam,
        Sinhala,
        Thai,
        Lao,
        Tibetan,
        Myanmar,
        Georgian,
        Khmer,
        SimplifiedChinese,
        TraditionalChinese,
        Japanese,
        Korean,
        Vietnamese,

        Symbol,
        Other = Symbol,

        Ogham,
        Runic,
        Nko,

        WritingSystemsCount
    };
    Q_ENUM(WritingSystem)

    enum SystemFont {
        GeneralFont,
        FixedFont,
        TitleFont,
        SmallestReadableFont
    };
    Q_ENUM(SystemFont)

    static QList<int> standardSizes();

    QFontDatabase();

    QList<WritingSystem> writingSystems() const;
    QList<WritingSystem> writingSystems(const QString &family) const;

    QStringList families(WritingSystem writingSystem = Any) const;
    QStringList styles(const QString &family) const;
    QList<int> pointSizes(const QString &family, const QString &style = QString());
    QList<int> smoothSizes(const QString &family, const QString &style);
    QString styleString(const QFont &font);
    QString styleString(const QFontInfo &fontInfo);

    QFont font(const QString &family, const QString &style, int pointSize) const;

    bool isBitmapScalable(const QString &family, const QString &style = QString()) const;
    bool isSmoothlyScalable(const QString &family, const QString &style = QString()) const;
    bool isScalable(const QString &family, const QString &style = QString()) const;
    bool isFixedPitch(const QString &family, const QString &style = QString()) const;

    bool italic(const QString &family, const QString &style) const;
    bool bold(const QString &family, const QString &style) const;
    int weight(const QString &family, const QString &style) const;

    bool hasFamily(const QString &family) const;
    bool isPrivateFamily(const QString &family) const;

    static QString writingSystemName(WritingSystem writingSystem);
    static QString writingSystemSample(WritingSystem writingSystem);

    static int addApplicationFont(const QString &fileName);
    static int addApplicationFontFromData(const QByteArray &fontData);
    static QStringList applicationFontFamilies(int id);
    static bool removeApplicationFont(int id);
    static bool removeAllApplicationFonts();

#if QT_DEPRECATED_SINCE(5, 2)
    QT_DEPRECATED static bool supportsThreadedFontRendering();
#endif

    static QFont systemFont(SystemFont type);

private:
    static void createDatabase();
    static void parseFontName(const QString &name, QString &foundry, QString &family);
    static QString resolveFontFamilyAlias(const QString &family);
    static QFontEngine *findFont(const QFontDef &request, int script);
    static void load(const QFontPrivate *d, int script);

    friend struct QFontDef;
    friend class QFontPrivate;
    friend class QFontDialog;
    friend class QFontDialogPrivate;
    friend class QFontEngineMulti;

    QFontDatabasePrivate *d;
};

QT_END_NAMESPACE

#endif // QFONTDATABASE_H
