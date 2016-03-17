/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtQuick module of the Qt Toolkit.
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

#ifndef QSGDISTANCEFIELDUTIL_H
#define QSGDISTANCEFIELDUTIL_H

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

#include <qrawfont.h>
#include <private/qfontengine_p.h>
#include <private/qsgadaptationlayer_p.h>

QT_BEGIN_NAMESPACE

typedef float (*ThresholdFunc)(float glyphScale);
typedef float (*AntialiasingSpreadFunc)(float glyphScale);

class QOpenGLShaderProgram;
class QSGDistanceFieldGlyphCache;
class QSGContext;

class Q_QUICK_PRIVATE_EXPORT QSGDistanceFieldGlyphCacheManager
{
public:
    QSGDistanceFieldGlyphCacheManager();
    ~QSGDistanceFieldGlyphCacheManager();

    QSGDistanceFieldGlyphCache *cache(const QRawFont &font);
    void insertCache(const QRawFont &font, QSGDistanceFieldGlyphCache *cache);

    ThresholdFunc thresholdFunc() const { return m_threshold_func; }
    void setThresholdFunc(ThresholdFunc func) { m_threshold_func = func; }

    AntialiasingSpreadFunc antialiasingSpreadFunc() const { return m_antialiasingSpread_func; }
    void setAntialiasingSpreadFunc(AntialiasingSpreadFunc func) { m_antialiasingSpread_func = func; }

private:
    static QString fontKey(const QRawFont &font);

    QHash<QString, QSGDistanceFieldGlyphCache *> m_caches;

    ThresholdFunc m_threshold_func;
    AntialiasingSpreadFunc m_antialiasingSpread_func;
};

QT_END_NAMESPACE

#endif // QSGDISTANCEFIELDUTIL_H
