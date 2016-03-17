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
#ifndef QTEXTDOCUMENTWRITER_H
#define QTEXTDOCUMENTWRITER_H

#include <QtCore/qstring.h>

QT_BEGIN_NAMESPACE


class QTextDocumentWriterPrivate;
class QIODevice;
class QByteArray;
class QTextDocument;
class QTextDocumentFragment;

class Q_GUI_EXPORT QTextDocumentWriter
{
public:
    QTextDocumentWriter();
    QTextDocumentWriter(QIODevice *device, const QByteArray &format);
    explicit QTextDocumentWriter(const QString &fileName, const QByteArray &format = QByteArray());
    ~QTextDocumentWriter();

    void setFormat (const QByteArray &format);
    QByteArray format () const;

    void setDevice (QIODevice *device);
    QIODevice *device () const;
    void setFileName (const QString &fileName);
    QString fileName () const;

    bool write(const QTextDocument *document);
    bool write(const QTextDocumentFragment &fragment);

#ifndef QT_NO_TEXTCODEC
    void setCodec(QTextCodec *codec);
    QTextCodec *codec() const;
#endif

    static QList<QByteArray> supportedDocumentFormats();

private:
    Q_DISABLE_COPY(QTextDocumentWriter)
    QTextDocumentWriterPrivate *d;
};

QT_END_NAMESPACE

#endif
