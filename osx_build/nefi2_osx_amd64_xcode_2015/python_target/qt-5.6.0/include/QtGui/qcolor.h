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

#ifndef QCOLOR_H
#define QCOLOR_H

#include <QtGui/qrgb.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qstringlist.h>
#include <QtGui/qrgba64.h>

QT_BEGIN_NAMESPACE


class QColor;
class QColormap;
class QVariant;

#ifndef QT_NO_DEBUG_STREAM
Q_GUI_EXPORT QDebug operator<<(QDebug, const QColor &);
#endif
#ifndef QT_NO_DATASTREAM
Q_GUI_EXPORT QDataStream &operator<<(QDataStream &, const QColor &);
Q_GUI_EXPORT QDataStream &operator>>(QDataStream &, QColor &);
#endif

class Q_GUI_EXPORT QColor
{
public:
    enum Spec { Invalid, Rgb, Hsv, Cmyk, Hsl };
    enum NameFormat { HexRgb, HexArgb };

    QColor();
    QColor(Qt::GlobalColor color);
    QColor(int r, int g, int b, int a = 255);
    QColor(QRgb rgb);
    QColor(QRgba64 rgba64);
    QColor(const QString& name);
    QColor(const char *name);
    QColor(Spec spec);

#if QT_VERSION < QT_VERSION_CHECK(6,0,0)
    QColor(const QColor &color); // ### Qt 6: remove all of these, the trivial ones are fine.
# ifdef Q_COMPILER_RVALUE_REFS
    QColor(QColor &&other) Q_DECL_NOTHROW : cspec(other.cspec), ct(other.ct) {}
    QColor &operator=(QColor &&other) Q_DECL_NOTHROW
    { cspec = other.cspec; ct = other.ct; return *this; }
# endif
    QColor &operator=(const QColor &);
#endif // Qt < 6

    QColor &operator=(Qt::GlobalColor color);

    bool isValid() const;

    // ### Qt 6: merge overloads
    QString name() const;
    QString name(NameFormat format) const;
    void setNamedColor(const QString& name);

    static QStringList colorNames();

    inline Spec spec() const
    { return cspec; }

    int alpha() const;
    void setAlpha(int alpha);

    qreal alphaF() const;
    void setAlphaF(qreal alpha);

    int red() const;
    int green() const;
    int blue() const;
    void setRed(int red);
    void setGreen(int green);
    void setBlue(int blue);

    qreal redF() const;
    qreal greenF() const;
    qreal blueF() const;
    void setRedF(qreal red);
    void setGreenF(qreal green);
    void setBlueF(qreal blue);

    void getRgb(int *r, int *g, int *b, int *a = Q_NULLPTR) const;
    void setRgb(int r, int g, int b, int a = 255);

    void getRgbF(qreal *r, qreal *g, qreal *b, qreal *a = Q_NULLPTR) const;
    void setRgbF(qreal r, qreal g, qreal b, qreal a = 1.0);

    QRgb rgba() const;
    void setRgba(QRgb rgba);

    QRgba64 rgba64() const;
    void setRgba64(QRgba64 rgba);

    QRgb rgb() const;
    void setRgb(QRgb rgb);

    int hue() const; // 0 <= hue < 360
    int saturation() const;
    int hsvHue() const; // 0 <= hue < 360
    int hsvSaturation() const;
    int value() const;

    qreal hueF() const; // 0.0 <= hueF < 360.0
    qreal saturationF() const;
    qreal hsvHueF() const; // 0.0 <= hueF < 360.0
    qreal hsvSaturationF() const;
    qreal valueF() const;

    void getHsv(int *h, int *s, int *v, int *a = Q_NULLPTR) const;
    void setHsv(int h, int s, int v, int a = 255);

    void getHsvF(qreal *h, qreal *s, qreal *v, qreal *a = Q_NULLPTR) const;
    void setHsvF(qreal h, qreal s, qreal v, qreal a = 1.0);

    int cyan() const;
    int magenta() const;
    int yellow() const;
    int black() const;

    qreal cyanF() const;
    qreal magentaF() const;
    qreal yellowF() const;
    qreal blackF() const;

    void getCmyk(int *c, int *m, int *y, int *k, int *a = Q_NULLPTR);
    void setCmyk(int c, int m, int y, int k, int a = 255);

    void getCmykF(qreal *c, qreal *m, qreal *y, qreal *k, qreal *a = Q_NULLPTR);
    void setCmykF(qreal c, qreal m, qreal y, qreal k, qreal a = 1.0);

    int hslHue() const; // 0 <= hue < 360
    int hslSaturation() const;
    int lightness() const;

    qreal hslHueF() const; // 0.0 <= hueF < 360.0
    qreal hslSaturationF() const;
    qreal lightnessF() const;

    void getHsl(int *h, int *s, int *l, int *a = Q_NULLPTR) const;
    void setHsl(int h, int s, int l, int a = 255);

    void getHslF(qreal *h, qreal *s, qreal *l, qreal *a = Q_NULLPTR) const;
    void setHslF(qreal h, qreal s, qreal l, qreal a = 1.0);

    QColor toRgb() const;
    QColor toHsv() const;
    QColor toCmyk() const;
    QColor toHsl() const;

    QColor convertTo(Spec colorSpec) const Q_REQUIRED_RESULT;

    static QColor fromRgb(QRgb rgb);
    static QColor fromRgba(QRgb rgba);

    static QColor fromRgb(int r, int g, int b, int a = 255);
    static QColor fromRgbF(qreal r, qreal g, qreal b, qreal a = 1.0);

    static QColor fromRgba64(ushort r, ushort g, ushort b, ushort a = USHRT_MAX);
    static QColor fromRgba64(QRgba64 rgba);

    static QColor fromHsv(int h, int s, int v, int a = 255);
    static QColor fromHsvF(qreal h, qreal s, qreal v, qreal a = 1.0);

    static QColor fromCmyk(int c, int m, int y, int k, int a = 255);
    static QColor fromCmykF(qreal c, qreal m, qreal y, qreal k, qreal a = 1.0);

    static QColor fromHsl(int h, int s, int l, int a = 255);
    static QColor fromHslF(qreal h, qreal s, qreal l, qreal a = 1.0);

    QColor light(int f = 150) const Q_REQUIRED_RESULT;
    QColor lighter(int f = 150) const Q_REQUIRED_RESULT;
    QColor dark(int f = 200) const Q_REQUIRED_RESULT;
    QColor darker(int f = 200) const Q_REQUIRED_RESULT;

    bool operator==(const QColor &c) const;
    bool operator!=(const QColor &c) const;

    operator QVariant() const;

    static bool isValidColor(const QString &name);

private:

    void invalidate();
    bool setColorFromString(const QString &name);

    Spec cspec;
    union {
        struct {
            ushort alpha;
            ushort red;
            ushort green;
            ushort blue;
            ushort pad;
        } argb;
        struct {
            ushort alpha;
            ushort hue;
            ushort saturation;
            ushort value;
            ushort pad;
        } ahsv;
        struct {
            ushort alpha;
            ushort cyan;
            ushort magenta;
            ushort yellow;
            ushort black;
        } acmyk;
        struct {
            ushort alpha;
            ushort hue;
            ushort saturation;
            ushort lightness;
            ushort pad;
        } ahsl;
        ushort array[5];
    } ct;

    friend class QColormap;
#ifndef QT_NO_DATASTREAM
    friend Q_GUI_EXPORT QDataStream &operator<<(QDataStream &, const QColor &);
    friend Q_GUI_EXPORT QDataStream &operator>>(QDataStream &, QColor &);
#endif
};

inline QColor::QColor()
{ invalidate(); }

inline QColor::QColor(int r, int g, int b, int a)
{ setRgb(r, g, b, a); }

inline QColor::QColor(const char *aname)
{ setNamedColor(QLatin1String(aname)); }

inline QColor::QColor(const QString& aname)
{ setNamedColor(aname); }

#if QT_VERSION < QT_VERSION_CHECK(6,0,0)
inline QColor::QColor(const QColor &acolor)
    : cspec(acolor.cspec)
{ ct.argb = acolor.ct.argb; }
#endif

inline bool QColor::isValid() const
{ return cspec != Invalid; }

inline QColor QColor::lighter(int f) const
{ return light(f); }

inline QColor QColor::darker(int f) const
{ return dark(f); }

QT_END_NAMESPACE

#endif // QCOLOR_H
