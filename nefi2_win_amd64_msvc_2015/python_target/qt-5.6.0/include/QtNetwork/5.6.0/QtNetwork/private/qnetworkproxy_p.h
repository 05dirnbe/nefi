/****************************************************************************
**
** Copyright (C) 2009 David Faure <dfaure@kdab.net>
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

#ifndef QNETWORKPROXY_P_H
#define QNETWORKPROXY_P_H


//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of the QLibrary class.  This header file may change from
// version to version without notice, or even be removed.
//
// We mean it.
//

#ifndef QT_NO_NETWORKPROXY

QT_BEGIN_NAMESPACE

class QSystemConfigurationProxyFactory : public QNetworkProxyFactory
{
public:
    QSystemConfigurationProxyFactory() : QNetworkProxyFactory() {}

    virtual QList<QNetworkProxy> queryProxy(const QNetworkProxyQuery& query)
    {
        QList<QNetworkProxy> proxies = QNetworkProxyFactory::systemProxyForQuery(query);

        // Make sure NoProxy is in the list, so that QTcpServer can work:
        // it searches for the first proxy that can has the ListeningCapability capability
        // if none have (as is the case with HTTP proxies), it fails to bind.
        // NoProxy allows it to fallback to the 'no proxy' case and bind.
        proxies.append(QNetworkProxy::NoProxy);

        return proxies;
    }
};

QT_END_NAMESPACE

#endif // QT_NO_NETWORKINTERFACE

#endif

