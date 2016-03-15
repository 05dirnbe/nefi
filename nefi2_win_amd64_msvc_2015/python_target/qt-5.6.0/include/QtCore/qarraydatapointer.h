/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtCore module of the Qt Toolkit.
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

#ifndef QARRAYDATAPOINTER_H
#define QARRAYDATAPOINTER_H

#include <QtCore/qarraydataops.h>

QT_BEGIN_NAMESPACE

template <class T>
struct QArrayDataPointer
{
private:
    typedef QTypedArrayData<T> Data;
    typedef QArrayDataOps<T> DataOps;

public:
    QArrayDataPointer() Q_DECL_NOTHROW
        : d(Data::sharedNull())
    {
    }

    QArrayDataPointer(const QArrayDataPointer &other)
        : d(other.d->ref.ref()
            ? other.d
            : other.clone(other.d->cloneFlags()))
    {
    }

    explicit QArrayDataPointer(QTypedArrayData<T> *ptr)
        : d(ptr)
    {
        Q_CHECK_PTR(ptr);
    }

    QArrayDataPointer(QArrayDataPointerRef<T> ref)
        : d(ref.ptr)
    {
    }

    QArrayDataPointer &operator=(const QArrayDataPointer &other)
    {
        QArrayDataPointer tmp(other);
        this->swap(tmp);
        return *this;
    }

#ifdef Q_COMPILER_RVALUE_REFS
    QArrayDataPointer(QArrayDataPointer &&other) Q_DECL_NOTHROW
        : d(other.d)
    {
        other.d = Data::sharedNull();
    }

    QArrayDataPointer &operator=(QArrayDataPointer &&other) Q_DECL_NOTHROW
    {
        QArrayDataPointer moved(std::move(other));
        this->swap(moved);
        return *this;
    }
#endif

    DataOps &operator*() const
    {
        Q_ASSERT(d);
        return *static_cast<DataOps *>(d);
    }

    DataOps *operator->() const
    {
        Q_ASSERT(d);
        return static_cast<DataOps *>(d);
    }

    ~QArrayDataPointer()
    {
        if (!d->ref.deref()) {
            if (d->isMutable())
                (*this)->destroyAll();
            Data::deallocate(d);
        }
    }

    bool isNull() const
    {
        return d == Data::sharedNull();
    }

    Data *data() const
    {
        return d;
    }

    bool needsDetach() const
    {
        return (!d->isMutable() || d->ref.isShared());
    }

#if QT_SUPPORTS(UNSHARABLE_CONTAINERS)
    void setSharable(bool sharable)
    {
        if (needsDetach()) {
            Data *detached = clone(sharable
                    ? d->detachFlags() & ~QArrayData::Unsharable
                    : d->detachFlags() | QArrayData::Unsharable);
            QArrayDataPointer old(d);
            d = detached;
        } else {
            d->ref.setSharable(sharable);
        }
    }

    bool isSharable() const { return d->isSharable(); }
#endif

    void swap(QArrayDataPointer &other) Q_DECL_NOTHROW
    {
        qSwap(d, other.d);
    }

    void clear()
    {
        QArrayDataPointer tmp(d);
        d = Data::sharedNull();
    }

    bool detach()
    {
        if (needsDetach()) {
            Data *copy = clone(d->detachFlags());
            QArrayDataPointer old(d);
            d = copy;
            return true;
        }

        return false;
    }

private:
    Data *clone(QArrayData::AllocationOptions options) const Q_REQUIRED_RESULT
    {
        Data *x = Data::allocate(d->detachCapacity(d->size), options);
        Q_CHECK_PTR(x);
        QArrayDataPointer copy(x);

        if (d->size)
            copy->copyAppend(d->begin(), d->end());

        Data *result = copy.d;
        copy.d = Data::sharedNull();
        return result;
    }

    Data *d;
};

template <class T>
inline bool operator==(const QArrayDataPointer<T> &lhs, const QArrayDataPointer<T> &rhs)
{
    return lhs.data() == rhs.data();
}

template <class T>
inline bool operator!=(const QArrayDataPointer<T> &lhs, const QArrayDataPointer<T> &rhs)
{
    return lhs.data() != rhs.data();
}

template <class T>
inline void qSwap(QArrayDataPointer<T> &p1, QArrayDataPointer<T> &p2)
{
    p1.swap(p2);
}

QT_END_NAMESPACE

namespace std
{
    template <class T>
    inline void swap(
            QT_PREPEND_NAMESPACE(QArrayDataPointer)<T> &p1,
            QT_PREPEND_NAMESPACE(QArrayDataPointer)<T> &p2)
    {
        p1.swap(p2);
    }
}

#endif // include guard
