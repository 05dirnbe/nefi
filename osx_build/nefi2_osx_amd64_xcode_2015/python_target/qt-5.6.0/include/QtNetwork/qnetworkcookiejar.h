/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtNetwork module of the Qt Toolkit.
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

#ifndef QNETWORKCOOKIEJAR_H
#define QNETWORKCOOKIEJAR_H

#include <QtCore/QObject>
#include <QtCore/QUrl>

QT_BEGIN_NAMESPACE


class QNetworkCookie;

class QNetworkCookieJarPrivate;
class Q_NETWORK_EXPORT QNetworkCookieJar: public QObject
{
    Q_OBJECT
public:
    explicit QNetworkCookieJar(QObject *parent = Q_NULLPTR);
    virtual ~QNetworkCookieJar();

    virtual QList<QNetworkCookie> cookiesForUrl(const QUrl &url) const;
    virtual bool setCookiesFromUrl(const QList<QNetworkCookie> &cookieList, const QUrl &url);

    virtual bool insertCookie(const QNetworkCookie &cookie);
    virtual bool updateCookie(const QNetworkCookie &cookie);
    virtual bool deleteCookie(const QNetworkCookie &cookie);

protected:
    QList<QNetworkCookie> allCookies() const;
    void setAllCookies(const QList<QNetworkCookie> &cookieList);
    virtual bool validateCookie(const QNetworkCookie &cookie, const QUrl &url) const;

private:
    Q_DECLARE_PRIVATE(QNetworkCookieJar)
    Q_DISABLE_COPY(QNetworkCookieJar)
};

QT_END_NAMESPACE

#endif
