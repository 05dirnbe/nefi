/****************************************************************************
**
** Copyright (C) 2015 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtQml module of the Qt Toolkit.
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
#ifndef QV4FUNCTIONOBJECT_H
#define QV4FUNCTIONOBJECT_H

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

#include "qv4object_p.h"
#include "qv4function_p.h"
#include "qv4context_p.h"
#include <private/qv4mm_p.h>

QT_BEGIN_NAMESPACE

struct QQmlSourceLocation;

namespace QV4 {

namespace Heap {

struct Q_QML_PRIVATE_EXPORT FunctionObject : Object {
    enum {
        Index_Prototype = 0,
        Index_ProtoConstructor = 0
    };

    FunctionObject(QV4::ExecutionContext *scope, QV4::String *name, bool createProto = false);
    FunctionObject(QV4::ExecutionContext *scope, QV4::Function *function, bool createProto = false);
    FunctionObject(QV4::ExecutionContext *scope, const QString &name = QString(), bool createProto = false);
    FunctionObject(ExecutionContext *scope, const QString &name = QString(), bool createProto = false);
    FunctionObject(QV4::ExecutionContext *scope, const ReturnedValue name);
    FunctionObject(ExecutionContext *scope, const ReturnedValue name);
    FunctionObject();
    ~FunctionObject();

    unsigned int formalParameterCount() { return function ? function->nFormals : 0; }
    unsigned int varCount() { return function ? function->compiledFunction->nLocals : 0; }
    bool needsActivation() const { return function ? function->needsActivation() : false; }

    Pointer<ExecutionContext> scope;
    Function *function;
};

struct FunctionCtor : FunctionObject {
    FunctionCtor(QV4::ExecutionContext *scope);
};

struct FunctionPrototype : FunctionObject {
    FunctionPrototype();
};

struct Q_QML_EXPORT BuiltinFunction : FunctionObject {
    BuiltinFunction(QV4::ExecutionContext *scope, QV4::String *name, ReturnedValue (*code)(QV4::CallContext *));
    ReturnedValue (*code)(QV4::CallContext *);
};

struct IndexedBuiltinFunction : FunctionObject {
    inline IndexedBuiltinFunction(QV4::ExecutionContext *scope, uint index, ReturnedValue (*code)(QV4::CallContext *ctx, uint index));
    ReturnedValue (*code)(QV4::CallContext *, uint index);
    uint index;
};

struct SimpleScriptFunction : FunctionObject {
    enum {
        Index_Name = FunctionObject::Index_Prototype + 1,
        Index_Length
    };
    SimpleScriptFunction(QV4::ExecutionContext *scope, Function *function, bool createProto);
};

struct ScriptFunction : SimpleScriptFunction {
    ScriptFunction(QV4::ExecutionContext *scope, Function *function);
};

struct BoundFunction : FunctionObject {
    BoundFunction(QV4::ExecutionContext *scope, QV4::FunctionObject *target, const Value &boundThis, QV4::MemberData *boundArgs);
    Pointer<FunctionObject> target;
    Value boundThis;
    Pointer<MemberData> boundArgs;
};

}

struct Q_QML_EXPORT FunctionObject: Object {
    enum {
        IsFunctionObject = true
    };
    V4_OBJECT2(FunctionObject, Object)
    Q_MANAGED_TYPE(FunctionObject)
    V4_INTERNALCLASS(functionClass)
    V4_PROTOTYPE(functionPrototype)
    V4_NEEDS_DESTROY

    Heap::ExecutionContext *scope() const { return d()->scope; }
    Function *function() const { return d()->function; }

    ReturnedValue name() const;
    unsigned int formalParameterCount() const { return d()->formalParameterCount(); }
    unsigned int varCount() const { return d()->varCount(); }

    void init(String *name, bool createProto);

    ReturnedValue newInstance();

    using Object::construct;
    using Object::call;
    static ReturnedValue construct(const Managed *that, CallData *);
    static ReturnedValue call(const Managed *that, CallData *d);

    static Heap::FunctionObject *createScriptFunction(ExecutionContext *scope, Function *function, bool createProto = true);
    static Heap::FunctionObject *createQmlFunction(QQmlContextData *qmlContext, QObject *scopeObject, QV4::Function *runtimeFunction,
                                                   const QList<QByteArray> &signalParameters = QList<QByteArray>(), QString *error = 0);

    ReturnedValue protoProperty() { return propertyData(Heap::FunctionObject::Index_Prototype)->asReturnedValue(); }

    bool needsActivation() const { return d()->needsActivation(); }
    bool strictMode() const { return d()->function ? d()->function->isStrict() : false; }
    bool isBinding() const;
    bool isBoundFunction() const;

    QQmlSourceLocation sourceLocation() const;

    static void markObjects(Heap::Base *that, ExecutionEngine *e);
};

template<>
inline const FunctionObject *Value::as() const {
    return isManaged() && m() && m()->vtable()->isFunctionObject ? reinterpret_cast<const FunctionObject *>(this) : 0;
}


struct FunctionCtor: FunctionObject
{
    V4_OBJECT2(FunctionCtor, FunctionObject)

    static ReturnedValue construct(const Managed *that, CallData *callData);
    static ReturnedValue call(const Managed *that, CallData *callData);
};

struct FunctionPrototype: FunctionObject
{
    V4_OBJECT2(FunctionPrototype, FunctionObject)

    void init(ExecutionEngine *engine, Object *ctor);

    static ReturnedValue method_toString(CallContext *ctx);
    static ReturnedValue method_apply(CallContext *ctx);
    static ReturnedValue method_call(CallContext *ctx);
    static ReturnedValue method_bind(CallContext *ctx);
};

struct Q_QML_EXPORT BuiltinFunction: FunctionObject {
    V4_OBJECT2(BuiltinFunction, FunctionObject)

    static Heap::BuiltinFunction *create(ExecutionContext *scope, String *name, ReturnedValue (*code)(CallContext *))
    {
        return scope->engine()->memoryManager->allocObject<BuiltinFunction>(scope, name, code);
    }

    static ReturnedValue construct(const Managed *, CallData *);
    static ReturnedValue call(const Managed *that, CallData *callData);
};

struct IndexedBuiltinFunction: FunctionObject
{
    V4_OBJECT2(IndexedBuiltinFunction, FunctionObject)

    static ReturnedValue construct(const Managed *m, CallData *)
    {
        return static_cast<const IndexedBuiltinFunction *>(m)->engine()->throwTypeError();
    }

    static ReturnedValue call(const Managed *that, CallData *callData);
};

Heap::IndexedBuiltinFunction::IndexedBuiltinFunction(QV4::ExecutionContext *scope, uint index,
                                                     ReturnedValue (*code)(QV4::CallContext *ctx, uint index))
    : Heap::FunctionObject(scope),
      code(code)
    , index(index)
{
}


struct SimpleScriptFunction: FunctionObject {
    V4_OBJECT2(SimpleScriptFunction, FunctionObject)
    V4_INTERNALCLASS(simpleScriptFunctionClass)

    static ReturnedValue construct(const Managed *, CallData *callData);
    static ReturnedValue call(const Managed *that, CallData *callData);

    Heap::Object *protoForConstructor();
};

struct ScriptFunction: SimpleScriptFunction {
    V4_OBJECT2(ScriptFunction, FunctionObject)

    static ReturnedValue construct(const Managed *, CallData *callData);
    static ReturnedValue call(const Managed *that, CallData *callData);
};


struct BoundFunction: FunctionObject {
    V4_OBJECT2(BoundFunction, FunctionObject)

    static Heap::BoundFunction *create(ExecutionContext *scope, FunctionObject *target, const Value &boundThis, QV4::MemberData *boundArgs)
    {
        return scope->engine()->memoryManager->allocObject<BoundFunction>(scope, target, boundThis, boundArgs);
    }

    Heap::FunctionObject *target() const { return d()->target; }
    Value boundThis() const { return d()->boundThis; }
    Heap::MemberData *boundArgs() const { return d()->boundArgs; }

    static ReturnedValue construct(const Managed *, CallData *d);
    static ReturnedValue call(const Managed *that, CallData *dd);

    static void markObjects(Heap::Base *that, ExecutionEngine *e);
};

}

QT_END_NAMESPACE

#endif // QMLJS_OBJECTS_H
