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

#ifndef QTEXTCURSOR_H
#define QTEXTCURSOR_H

#include <QtCore/qstring.h>
#include <QtCore/qshareddata.h>
#include <QtGui/qtextformat.h>

QT_BEGIN_NAMESPACE


class QTextDocument;
class QTextCursorPrivate;
class QTextDocumentFragment;
class QTextCharFormat;
class QTextBlockFormat;
class QTextListFormat;
class QTextTableFormat;
class QTextFrameFormat;
class QTextImageFormat;
class QTextDocumentPrivate;
class QTextList;
class QTextTable;
class QTextFrame;
class QTextBlock;

class Q_GUI_EXPORT QTextCursor
{
public:
    QTextCursor();
    explicit QTextCursor(QTextDocument *document);
    QTextCursor(QTextDocumentPrivate *p, int pos);
    explicit QTextCursor(QTextCursorPrivate *d);
    explicit QTextCursor(QTextFrame *frame);
    explicit QTextCursor(const QTextBlock &block);
    QTextCursor(const QTextCursor &cursor);
#ifdef Q_COMPILER_RVALUE_REFS
    QTextCursor &operator=(QTextCursor &&other) Q_DECL_NOTHROW { swap(other); return *this; }
#endif
    QTextCursor &operator=(const QTextCursor &other);
    ~QTextCursor();

    void swap(QTextCursor &other) Q_DECL_NOTHROW { qSwap(d, other.d); }

    bool isNull() const;

    enum MoveMode {
        MoveAnchor,
        KeepAnchor
    };

    void setPosition(int pos, MoveMode mode = MoveAnchor);
    int position() const;
    int positionInBlock() const;

    int anchor() const;

    void insertText(const QString &text);
    void insertText(const QString &text, const QTextCharFormat &format);

    enum MoveOperation {
        NoMove,

        Start,
        Up,
        StartOfLine,
        StartOfBlock,
        StartOfWord,
        PreviousBlock,
        PreviousCharacter,
        PreviousWord,
        Left,
        WordLeft,

        End,
        Down,
        EndOfLine,
        EndOfWord,
        EndOfBlock,
        NextBlock,
        NextCharacter,
        NextWord,
        Right,
        WordRight,

        NextCell,
        PreviousCell,
        NextRow,
        PreviousRow
    };

    bool movePosition(MoveOperation op, MoveMode = MoveAnchor, int n = 1);

    bool visualNavigation() const;
    void setVisualNavigation(bool b);

    void setVerticalMovementX(int x);
    int verticalMovementX() const;

    void setKeepPositionOnInsert(bool b);
    bool keepPositionOnInsert() const;

    void deleteChar();
    void deletePreviousChar();

    enum SelectionType {
        WordUnderCursor,
        LineUnderCursor,
        BlockUnderCursor,
        Document
    };
    void select(SelectionType selection);

    bool hasSelection() const;
    bool hasComplexSelection() const;
    void removeSelectedText();
    void clearSelection();
    int selectionStart() const;
    int selectionEnd() const;

    QString selectedText() const;
    QTextDocumentFragment selection() const;
    void selectedTableCells(int *firstRow, int *numRows, int *firstColumn, int *numColumns) const;

    QTextBlock block() const;

    QTextCharFormat charFormat() const;
    void setCharFormat(const QTextCharFormat &format);
    void mergeCharFormat(const QTextCharFormat &modifier);

    QTextBlockFormat blockFormat() const;
    void setBlockFormat(const QTextBlockFormat &format);
    void mergeBlockFormat(const QTextBlockFormat &modifier);

    QTextCharFormat blockCharFormat() const;
    void setBlockCharFormat(const QTextCharFormat &format);
    void mergeBlockCharFormat(const QTextCharFormat &modifier);

    bool atBlockStart() const;
    bool atBlockEnd() const;
    bool atStart() const;
    bool atEnd() const;

    void insertBlock();
    void insertBlock(const QTextBlockFormat &format);
    void insertBlock(const QTextBlockFormat &format, const QTextCharFormat &charFormat);

    QTextList *insertList(const QTextListFormat &format);
    QTextList *insertList(QTextListFormat::Style style);

    QTextList *createList(const QTextListFormat &format);
    QTextList *createList(QTextListFormat::Style style);
    QTextList *currentList() const;

    QTextTable *insertTable(int rows, int cols, const QTextTableFormat &format);
    QTextTable *insertTable(int rows, int cols);
    QTextTable *currentTable() const;

    QTextFrame *insertFrame(const QTextFrameFormat &format);
    QTextFrame *currentFrame() const;

    void insertFragment(const QTextDocumentFragment &fragment);

#ifndef QT_NO_TEXTHTMLPARSER
    void insertHtml(const QString &html);
#endif // QT_NO_TEXTHTMLPARSER

    void insertImage(const QTextImageFormat &format, QTextFrameFormat::Position alignment);
    void insertImage(const QTextImageFormat &format);
    void insertImage(const QString &name);
    void insertImage(const QImage &image, const QString &name = QString());

    void beginEditBlock();
    void joinPreviousEditBlock();
    void endEditBlock();

    bool operator!=(const QTextCursor &rhs) const;
    bool operator<(const QTextCursor &rhs) const;
    bool operator<=(const QTextCursor &rhs) const;
    bool operator==(const QTextCursor &rhs) const;
    bool operator>=(const QTextCursor &rhs) const;
    bool operator>(const QTextCursor &rhs) const;

    bool isCopyOf(const QTextCursor &other) const;

    int blockNumber() const;
    int columnNumber() const;

    QTextDocument *document() const;

private:
    QSharedDataPointer<QTextCursorPrivate> d;
    friend class QTextCursorPrivate;
    friend class QTextDocumentPrivate;
    friend class QTextDocumentFragmentPrivate;
    friend class QTextCopyHelper;
    friend class QWidgetTextControlPrivate;
};

Q_DECLARE_SHARED(QTextCursor)

QT_END_NAMESPACE

#endif // QTEXTCURSOR_H
