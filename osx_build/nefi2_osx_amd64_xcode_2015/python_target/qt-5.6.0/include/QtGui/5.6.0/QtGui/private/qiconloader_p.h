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

#ifndef QICONLOADER_P_H
#define QICONLOADER_P_H

#include <QtCore/qglobal.h>

#ifndef QT_NO_ICON
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

#include <QtGui/QIcon>
#include <QtGui/QIconEngine>
#include <QtGui/QPixmapCache>
#include <private/qicon_p.h>
#include <private/qfactoryloader_p.h>
#include <QtCore/QHash>
#include <QtCore/QVector>
#include <QtCore/QTypeInfo>

QT_BEGIN_NAMESPACE

class QIconLoader;

struct QIconDirInfo
{
    enum Type { Fixed, Scalable, Threshold };
    QIconDirInfo(const QString &_path = QString()) :
            path(_path),
            size(0),
            maxSize(0),
            minSize(0),
            threshold(0),
            type(Threshold) {}
    QString path;
    short size;
    short maxSize;
    short minSize;
    short threshold;
    Type type;
};
Q_DECLARE_TYPEINFO(QIconDirInfo, Q_MOVABLE_TYPE);

class QIconLoaderEngineEntry
 {
public:
    virtual ~QIconLoaderEngineEntry() {}
    virtual QPixmap pixmap(const QSize &size,
                           QIcon::Mode mode,
                           QIcon::State state) = 0;
    QString filename;
    QIconDirInfo dir;
    static int count;
};

struct ScalableEntry : public QIconLoaderEngineEntry
{
    QPixmap pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state) Q_DECL_OVERRIDE;
    QIcon svgIcon;
};

struct PixmapEntry : public QIconLoaderEngineEntry
{
    QPixmap pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state) Q_DECL_OVERRIDE;
    QPixmap basePixmap;
};

typedef QList<QIconLoaderEngineEntry*> QThemeIconEntries;

struct QThemeIconInfo
{
    QThemeIconEntries entries;
    QString iconName;
};

class QIconLoaderEngine : public QIconEngine
{
public:
    QIconLoaderEngine(const QString& iconName = QString());
    ~QIconLoaderEngine();

    void paint(QPainter *painter, const QRect &rect, QIcon::Mode mode, QIcon::State state);
    QPixmap pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state);
    QSize actualSize(const QSize &size, QIcon::Mode mode, QIcon::State state);
    QIconEngine *clone() const;
    bool read(QDataStream &in);
    bool write(QDataStream &out) const;

private:
    QString key() const;
    bool hasIcon() const;
    void ensureLoaded();
    void virtual_hook(int id, void *data);
    QIconLoaderEngineEntry *entryForSize(const QSize &size);
    QIconLoaderEngine(const QIconLoaderEngine &other);
    QThemeIconInfo m_info;
    QString m_iconName;
    uint m_key;

    friend class QIconLoader;
};

class QIconTheme
{
public:
    QIconTheme(const QString &name);
    QIconTheme() : m_valid(false) {}
    QStringList parents() { return m_parents; }
    QVector<QIconDirInfo> keyList() { return m_keyList; }
    QStringList contentDirs() { return m_contentDirs; }
    bool isValid() { return m_valid; }

private:
    QStringList m_contentDirs;
    QVector<QIconDirInfo> m_keyList;
    QStringList m_parents;
    bool m_valid;
};

class Q_GUI_EXPORT QIconLoader
{
public:
    QIconLoader();
    QThemeIconInfo loadIcon(const QString &iconName) const;
    uint themeKey() const { return m_themeKey; }

    QString themeName() const { return m_userTheme.isEmpty() ? m_systemTheme : m_userTheme; }
    void setThemeName(const QString &themeName);
    QIconTheme theme() { return themeList.value(themeName()); }
    void setThemeSearchPath(const QStringList &searchPaths);
    QStringList themeSearchPaths() const;
    QIconDirInfo dirInfo(int dirindex);
    static QIconLoader *instance();
    void updateSystemTheme();
    void invalidateKey() { m_themeKey++; }
    void ensureInitialized();
    bool hasUserTheme() const { return !m_userTheme.isEmpty(); }

private:
    QThemeIconInfo findIconHelper(const QString &themeName,
                                  const QString &iconName,
                                  QStringList &visited) const;
    uint m_themeKey;
    bool m_supportsSvg;
    bool m_initialized;

    mutable QString m_userTheme;
    mutable QString m_systemTheme;
    mutable QStringList m_iconDirs;
    mutable QHash <QString, QIconTheme> themeList;
};

QT_END_NAMESPACE

#endif // QT_NO_ICON

#endif // QICONLOADER_P_H
