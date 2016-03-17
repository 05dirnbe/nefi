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

#ifndef QTCONCURRENT_FUNCTIONWRAPPERS_H
#define QTCONCURRENT_FUNCTIONWRAPPERS_H

#include <QtConcurrent/qtconcurrentcompilertest.h>
#include <QtCore/QStringList>

#ifndef QT_NO_CONCURRENT

QT_BEGIN_NAMESPACE


#ifndef Q_QDOC

namespace QtConcurrent {

template <typename T>
class FunctionWrapper0
{
public:
    typedef T (*FunctionPointerType)();
    typedef T result_type;
    inline FunctionWrapper0(FunctionPointerType _functionPointer)
    :functionPointer(_functionPointer) { }

    inline T operator()()
    {
        return functionPointer();
    }
private:
    FunctionPointerType functionPointer;
};

template <typename T, typename U>
class FunctionWrapper1
{
public:
    typedef T (*FunctionPointerType)(U u);
    typedef T result_type;
    inline FunctionWrapper1(FunctionPointerType _functionPointer)
    :functionPointer(_functionPointer) { }

    inline T operator()(U u)
    {
        return functionPointer(u);
    }

private:
    FunctionPointerType functionPointer;
};

template <typename T, typename U, typename V>
class FunctionWrapper2
{
public:
    typedef T (*FunctionPointerType)(U u, V v);
    typedef T result_type;
    inline FunctionWrapper2(FunctionPointerType _functionPointer)
    :functionPointer(_functionPointer) { }

    inline T operator()(U u, V v)
    {
        return functionPointer(u, v);
    }
private:
    FunctionPointerType functionPointer;
};

template <typename T, typename C>
class MemberFunctionWrapper
{
public:
    typedef T (C::*FunctionPointerType)();
    typedef T result_type;
    inline MemberFunctionWrapper(FunctionPointerType _functionPointer)
    :functionPointer(_functionPointer) { }

    inline T operator()(C &c)
    {
        return (c.*functionPointer)();
    }
private:
    FunctionPointerType functionPointer;
};

template <typename T, typename C, typename U>
class MemberFunctionWrapper1
{
public:
    typedef T (C::*FunctionPointerType)(U);
    typedef T result_type;

    inline MemberFunctionWrapper1(FunctionPointerType _functionPointer)
        : functionPointer(_functionPointer)
    { }

    inline T operator()(C &c, U u)
    {
        return (c.*functionPointer)(u);
    }

private:
    FunctionPointerType functionPointer;
};

template <typename T, typename C>
class ConstMemberFunctionWrapper
{
public:
    typedef T (C::*FunctionPointerType)() const;
    typedef T result_type;
    inline ConstMemberFunctionWrapper(FunctionPointerType _functionPointer)
    :functionPointer(_functionPointer) { }

    inline T operator()(const C &c) const
    {
        return (c.*functionPointer)();
    }
private:
    FunctionPointerType functionPointer;
};

} // namespace QtConcurrent.

namespace QtPrivate {

template <typename T>
const T& createFunctionWrapper(const T& t)
{
    return t;
}

template <typename T, typename U>
QtConcurrent::FunctionWrapper1<T, U> createFunctionWrapper(T (*func)(U))
{
    return QtConcurrent::FunctionWrapper1<T, U>(func);
}

template <typename T, typename C>
QtConcurrent::MemberFunctionWrapper<T, C> createFunctionWrapper(T (C::*func)())
{
    return QtConcurrent::MemberFunctionWrapper<T, C>(func);
}

template <typename T, typename C, typename U>
QtConcurrent::MemberFunctionWrapper1<T, C, U> createFunctionWrapper(T (C::*func)(U))
{
    return QtConcurrent::MemberFunctionWrapper1<T, C, U>(func);
}

template <typename T, typename C>
QtConcurrent::ConstMemberFunctionWrapper<T, C> createFunctionWrapper(T (C::*func)() const)
{
    return QtConcurrent::ConstMemberFunctionWrapper<T, C>(func);
}

struct PushBackWrapper
{
    typedef void result_type;

    template <class C, class U>
    inline void operator()(C &c, const U &u) const
    {
        return c.push_back(u);
    }

#ifdef Q_COMPILER_RVALUE_REFS
    template <class C, class U>
    inline void operator()(C &c, U &&u) const
    {
        return c.push_back(u);
    }
#endif
};

template <typename Functor, bool foo = HasResultType<Functor>::Value>
struct LazyResultType { typedef typename Functor::result_type Type; };
template <typename Functor>
struct LazyResultType<Functor, false> { typedef void Type; };

template <class T>
struct ReduceResultType;

template <class U, class V>
struct ReduceResultType<void(*)(U&,V)>
{
    typedef U ResultType;
};

template <class T, class C, class U>
struct ReduceResultType<T(C::*)(U)>
{
    typedef C ResultType;
};

template <class InputSequence, class MapFunctor>
struct MapResultType
{
    typedef typename LazyResultType<MapFunctor>::Type ResultType;
};

template <class U, class V>
struct MapResultType<void, U (*)(V)>
{
    typedef U ResultType;
};

template <class T, class C>
struct MapResultType<void, T(C::*)() const>
{
    typedef T ResultType;
};

#ifndef QT_NO_TEMPLATE_TEMPLATE_PARAMETERS

template <template <typename> class InputSequence, typename MapFunctor, typename T>
struct MapResultType<InputSequence<T>, MapFunctor>
{
    typedef InputSequence<typename LazyResultType<MapFunctor>::Type> ResultType;
};

template <template <typename> class InputSequence, class T, class U, class V>
struct MapResultType<InputSequence<T>, U (*)(V)>
{
    typedef InputSequence<U> ResultType;
};

template <template <typename> class InputSequence, class T, class U, class C>
struct MapResultType<InputSequence<T>, U(C::*)() const>
{
    typedef InputSequence<U> ResultType;
};

#endif // QT_NO_TEMPLATE_TEMPLATE_PARAMETER

template <class MapFunctor>
struct MapResultType<QStringList, MapFunctor>
{
    typedef QList<typename LazyResultType<MapFunctor>::Type> ResultType;
};

template <class U, class V>
struct MapResultType<QStringList, U (*)(V)>
{
    typedef QList<U> ResultType;
};

template <class U, class C>
struct MapResultType<QStringList, U(C::*)() const>
{
    typedef QList<U> ResultType;
};

} // namespace QtPrivate.

#endif //Q_QDOC

QT_END_NAMESPACE

#endif // QT_NO_CONCURRENT

#endif
