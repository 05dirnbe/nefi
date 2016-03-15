/****************************************************************************
**
** Copyright (C) 2014 Klaralvdalens Datakonsult AB (KDAB).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the Qt3D module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL3$
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
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or later as published by the Free
** Software Foundation and appearing in the file LICENSE.GPL included in
** the packaging of this file. Please review the following information to
** ensure the GNU General Public License version 2.0 requirements will be
** met: http://www.gnu.org/licenses/gpl-2.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QT3DRENDER_RENDERVIEWJOBUTILS_P_H
#define QT3DRENDER_RENDERVIEWJOBUTILS_P_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of other Qt classes.  This header file may change from version to
// version without notice, or even be removed.
//
// We mean it.
//

#include <Qt3DRender/qt3drender_global.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qhash.h>
#include <QtCore/qvariant.h>

QT_BEGIN_NAMESPACE

namespace Qt3DCore {
class QFrameAllocator;
}

namespace Qt3DRender {
namespace Render {

class FrameGraphNode;
class ParameterManager;
class Effect;
class Entity;
class Material;
class RenderPass;
class RenderStateSet;
class Technique;
class RenderView;
class Renderer;
class NodeManagers;
class ShaderDataManager;
struct ShaderUniform;
class ShaderData;
class RenderState;

Q_AUTOTEST_EXPORT void setRenderViewConfigFromFrameGraphLeafNode(RenderView *rv,
                                                                 const FrameGraphNode *fgLeaf);

Q_AUTOTEST_EXPORT Technique *findTechniqueForEffect(Renderer *renderer,
                                                    RenderView *renderView,
                                                    Effect *effect);

typedef QVarLengthArray<RenderPass*, 4> RenderRenderPassList;
Q_AUTOTEST_EXPORT RenderRenderPassList findRenderPassesForTechnique(NodeManagers *manager,
                                                                    RenderView *renderView,
                                                                    Technique *technique);

struct ParameterInfo
{
    ParameterInfo(const QString &name = QString(), const QVariant &value = QVariant())
        : name(name)
        , value(value)
    {}

    QString name;
    QVariant value;

    bool operator<(const QString &otherName) const
    {
        return name < otherName;
    }

    bool operator<(const ParameterInfo &other) const
    {
        return name < other.name;
    }
};

inline bool operator<(const QString &otherName, const ParameterInfo &pi)
{
    return otherName < pi.name;
}

typedef QVarLengthArray<ParameterInfo, 16> ParameterInfoList;

Q_AUTOTEST_EXPORT void parametersFromMaterialEffectTechnique(ParameterInfoList *infoList,
                                                             ParameterManager *manager,
                                                             Material *material,
                                                             Effect *effect,
                                                             Technique *technique);

Q_AUTOTEST_EXPORT void addParametersForIds(ParameterInfoList *params, ParameterManager *manager,
                                           const QList<Qt3DCore::QNodeId> &parameterIds);

template<class T>
void parametersFromParametersProvider(ParameterInfoList *infoList,
                                      ParameterManager *manager,
                                      T *pass)
{
    if (pass)
        addParametersForIds(infoList, manager, pass->parameters());
}

Q_AUTOTEST_EXPORT ParameterInfoList::iterator findParamInfo(ParameterInfoList *infoList,
                                                            const QString &name);

Q_AUTOTEST_EXPORT RenderStateSet *buildRenderStateSet(const QList<RenderState*> &states,
                                                      Qt3DCore::QFrameAllocator *allocator);


struct Q_AUTOTEST_EXPORT UniformBlockValueBuilder
{
    UniformBlockValueBuilder();
    ~UniformBlockValueBuilder();

    void buildActiveUniformNameValueMapHelper(const QString &blockName,
                                              const QString &qmlPropertyName,
                                              const QVariant &value);
    void buildActiveUniformNameValueMapStructHelper(ShaderData *rShaderData,
                                                    const QString &blockName,
                                                    const QString &qmlPropertyName = QString());

    bool updatedPropertiesOnly;
    QHash<QString, ShaderUniform> uniforms;
    QHash<QString, QVariant> activeUniformNamesToValue;
    ShaderDataManager *shaderDataManager;
};

} // namespace Render
} // namespace Qt3DRender

Q_DECLARE_TYPEINFO(Qt3DRender::Render::ParameterInfo, Q_MOVABLE_TYPE);

QT_END_NAMESPACE

#endif // QT3DRENDER_RENDERVIEWJOBUTILS_P_H
