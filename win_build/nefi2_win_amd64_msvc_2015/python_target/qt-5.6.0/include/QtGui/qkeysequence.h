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

#ifndef QKEYSEQUENCE_H
#define QKEYSEQUENCE_H

#include <QtCore/qnamespace.h>
#include <QtCore/qstring.h>
#include <QtCore/qobjectdefs.h>

QT_BEGIN_NAMESPACE


#ifndef QT_NO_SHORTCUT

class QKeySequence;

/*****************************************************************************
  QKeySequence stream functions
 *****************************************************************************/
#ifndef QT_NO_DATASTREAM
Q_GUI_EXPORT QDataStream &operator<<(QDataStream &in, const QKeySequence &ks);
Q_GUI_EXPORT QDataStream &operator>>(QDataStream &out, QKeySequence &ks);
#endif

#ifdef Q_QDOC
void qt_set_sequence_auto_mnemonic(bool b);
#endif

class QVariant;
class QKeySequencePrivate;

Q_GUI_EXPORT Q_DECL_PURE_FUNCTION uint qHash(const QKeySequence &key, uint seed = 0) Q_DECL_NOTHROW;

class Q_GUI_EXPORT QKeySequence
{
    Q_GADGET

public:
    enum StandardKey {
        UnknownKey,
        HelpContents,
        WhatsThis,
        Open,
        Close,
        Save,
        New,
        Delete,
        Cut,
        Copy,
        Paste,
        Undo,
        Redo,
        Back,
        Forward,
        Refresh,
        ZoomIn,
        ZoomOut,
        Print,
        AddTab,
        NextChild,
        PreviousChild,
        Find,
        FindNext,
        FindPrevious,
        Replace,
        SelectAll,
        Bold,
        Italic,
        Underline,
        MoveToNextChar,
        MoveToPreviousChar,
        MoveToNextWord,
        MoveToPreviousWord,
        MoveToNextLine,
        MoveToPreviousLine,
        MoveToNextPage,
        MoveToPreviousPage,
        MoveToStartOfLine,
        MoveToEndOfLine,
        MoveToStartOfBlock,
        MoveToEndOfBlock,
        MoveToStartOfDocument,
        MoveToEndOfDocument,
        SelectNextChar,
        SelectPreviousChar,
        SelectNextWord,
        SelectPreviousWord,
        SelectNextLine,
        SelectPreviousLine,
        SelectNextPage,
        SelectPreviousPage,
        SelectStartOfLine,
        SelectEndOfLine,
        SelectStartOfBlock,
        SelectEndOfBlock,
        SelectStartOfDocument,
        SelectEndOfDocument,
        DeleteStartOfWord,
        DeleteEndOfWord,
        DeleteEndOfLine,
        InsertParagraphSeparator,
        InsertLineSeparator,
        SaveAs,
        Preferences,
        Quit,
        FullScreen,
        Deselect,
        DeleteCompleteLine,
        Backspace,
        Cancel
     };
     Q_ENUM(StandardKey)

    enum SequenceFormat {
        NativeText,
        PortableText
    };

    QKeySequence();
    QKeySequence(const QString &key, SequenceFormat format = NativeText);
    QKeySequence(int k1, int k2 = 0, int k3 = 0, int k4 = 0);
    QKeySequence(const QKeySequence &ks);
    QKeySequence(StandardKey key);
    ~QKeySequence();

    int count() const;
    bool isEmpty() const;

    enum SequenceMatch {
        NoMatch,
        PartialMatch,
        ExactMatch
    };

    QString toString(SequenceFormat format = PortableText) const;
    static QKeySequence fromString(const QString &str, SequenceFormat format = PortableText);

    static QList<QKeySequence> listFromString(const QString &str, SequenceFormat format = PortableText);
    static QString listToString(const QList<QKeySequence> &list, SequenceFormat format = PortableText);

    SequenceMatch matches(const QKeySequence &seq) const;
    static QKeySequence mnemonic(const QString &text);
    static QList<QKeySequence> keyBindings(StandardKey key);

#if QT_DEPRECATED_SINCE(5, 0)
    QT_DEPRECATED operator QString() const { return toString(QKeySequence::NativeText); }
    QT_DEPRECATED operator int() const { if (1 <= count()) return operator [](0); return 0; }
#endif
    operator QVariant() const;
    int operator[](uint i) const;
    QKeySequence &operator=(const QKeySequence &other);
#ifdef Q_COMPILER_RVALUE_REFS
    QKeySequence &operator=(QKeySequence &&other) Q_DECL_NOTHROW { swap(other); return *this; }
#endif
    void swap(QKeySequence &other) Q_DECL_NOTHROW { qSwap(d, other.d); }

    bool operator==(const QKeySequence &other) const;
    inline bool operator!= (const QKeySequence &other) const
    { return !(*this == other); }
    bool operator< (const QKeySequence &ks) const;
    inline bool operator> (const QKeySequence &other) const
    { return other < *this; }
    inline bool operator<= (const QKeySequence &other) const
    { return !(other < *this); }
    inline bool operator>= (const QKeySequence &other) const
    { return !(*this < other); }

    bool isDetached() const;
private:
    static int decodeString(const QString &ks);
    static QString encodeString(int key);
    int assign(const QString &str);
    int assign(const QString &str, SequenceFormat format);
    void setKey(int key, int index);

    QKeySequencePrivate *d;

    friend Q_GUI_EXPORT QDataStream &operator<<(QDataStream &in, const QKeySequence &ks);
    friend Q_GUI_EXPORT QDataStream &operator>>(QDataStream &in, QKeySequence &ks);
    friend Q_GUI_EXPORT uint qHash(const QKeySequence &key, uint seed) Q_DECL_NOTHROW;
    friend class QShortcutMap;
    friend class QShortcut;

public:
    typedef QKeySequencePrivate * DataPtr;
    inline DataPtr &data_ptr() { return d; }
};

Q_DECLARE_SHARED(QKeySequence)

#ifndef QT_NO_DEBUG_STREAM
Q_GUI_EXPORT QDebug operator<<(QDebug, const QKeySequence &);
#endif

#else

class Q_GUI_EXPORT QKeySequence
{
public:
    QKeySequence() {}
    QKeySequence(int) {}
};

#endif // QT_NO_SHORTCUT

QT_END_NAMESPACE

#endif // QKEYSEQUENCE_H
