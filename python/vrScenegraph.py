'''
vrScenegraph
------------------------------------------
API version: v1 | Generation Date: 2020-09-13 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------

'''

from __future__ import annotations
from typing import List


def addNodeTag(tag, node):
    '''
    Adds a tag to the node.
    '''
    pass


def addNodeTag(tag, nodes):
    '''
    Adds a tag to the node.
    '''
    pass


def addNodeTag(node, tags):
    '''
    Adds a list of tags to the node.
    '''
    pass


def addNodeTag(tags, nodes):
    '''
    Adds a list of tags to a list of node.
    '''
    pass


def getNodesWithTag(tag):
    '''
    Returns a list of nodes which have the metadatatag assigned starting from the root node.
    '''
    pass


def getNodesWithTag(tag, node):
    '''
    Returns a list of nodes which have the metadatatag assigned starting from the root node.
    '''
    pass


def getNodesWithTags(matchAllTags, tags):
    '''
    Returns a list of nodes which have the metadatatag assigned.
    '''
    pass


def getNodesWithTags(matchAllTags, node, tags):
    '''
    Returns a list of nodes which have the metadatatag assigned.
    '''
    pass


def removeNodeTag(tag, node):
    '''
    Removes a tag from a node.
    '''
    pass


def removeNodeTag(tag, nodes):
    '''
    Removes a tag from the given nodes.
    '''
    pass


def removeNodeTags(node, tags):
    '''
    Removes the tags from a node.
    '''
    pass


def removeNodeTags(tags, nodes):
    '''
    Removes the tags from the given nodes.
    '''
    pass


def replaceNodeTag(oldTag, node, newTag):
    '''
    Replaces an existing tag.
    '''
    pass


def replaceNodeTag(newTag, oldTag, nodes):
    '''
    Replaces an existing tag.
    '''
    pass


def setIgnoreMaterialGroup(nodepath, ignore):
    '''
    Ignores a material group.
    '''
    pass


def setIgnoreMaterialGroup(node, ignore):
    '''
    Ignores a material group.
    '''
    pass


def addChilds(node, children):
    '''
    Adds a list of child nodes to a node.
    '''
    pass


def addNodeTags():
    '''
    
    '''
    pass


def applyMaterial(mats, skipMaterialGroupChilds, applyToMaterialGroupParent, nodes):
    '''
    Applies a list of materials to a list of nodes.
    '''
    pass


def clearFindCache():
    '''
    Clears the find cache.
    '''
    pass


def cloneMirrorAxisNode(deep, axis, flush, node):
    '''
    Clone mirrors a subtree at a specific axis.
    '''
    pass


def cloneMirrorNode(deep, flush, node):
    '''
    Clone mirrors a subtree at the y-axis.
    '''
    pass


def cloneNode(deep, node):
    '''
    Clones a subtree.
    '''
    pass


def convertCore(type, node):
    '''
    Converts the core of a node to another type.
    '''
    pass


def copyNode(node):
    '''
    Copy a node from the scenegraph.
    '''
    pass


def copyNodes(nodes):
    '''
    Copy a list of nodes from the scenegraph.
    '''
    pass


def copyTransformation(source, copyRotatePivot, copyShearing, target, copyTranslation, copyRotation, copyScalePivot, copyScale):
    '''
    Copies the transformation of one node to another.
    '''
    pass


def createNode(name, type, parent):
    '''
    Creates a new node of a given type ans name into the scenegraph as a child of given parent.
    '''
    pass


def cutNode(node):
    '''
    Cut a node from the scenegraph.
    '''
    pass


def cutNodes(nodes):
    '''
    Cut a list of nodes from the scenegraph.
    '''
    pass


def deleteNode(force, node):
    '''
    Deletes a node.
    '''
    pass


def deleteNodes(force, nodes):
    '''
    Deletes a list of nodes.
    '''
    pass


def deselectAll():
    '''
    Deselects all objects from scenegraph.
    '''
    pass


def enableScenegraph(status):
    '''
    Enables scenegraph updates.
    '''
    pass


def findNode(regex, node_name):
    '''
    Finds the node via name.
    '''
    pass


def findNodePath(node_path, regex):
    '''
    Finds the node via path name.
    '''
    pass


def findNodes(regex, node_names, node_name):
    '''
    Finds the node via name.
    '''
    pass


def findUniquePath(unique_path):
    '''
    Finds the node via path unique path
    '''
    pass


def getAllNodes():
    '''
    Returns a list of all scenegraph nodes.
    '''
    pass


def getClipboard():
    '''
    Returns a list of all nodes in the clipboard.
    '''
    pass


def getHeadlight():
    '''
    Returns the headlight node.
    '''
    pass


def getInternalRootNode():
    '''
    Returns the internal root node.
    '''
    pass


def getNodeID(name):
    '''
    Returns the node id of the node with the provided name.
    '''
    pass


def getNodeName(node):
    '''
    Returns the name of a node.
    '''
    pass


def getNodePath(node):
    '''
    Returns the whole path name of a node.
    '''
    pass


def getNodeTags(node):
    '''
    Returns the list of tags attached to the given node.
    '''
    pass


def getRootNode():
    '''
    Returns the root node.
    '''
    pass


def getSceneSwitches():
    '''
    Finds all the switches in the scene.
    '''
    pass


def getSelectedNode():
    '''
    Returns the selected node.
    '''
    pass


def getSelectedNodes():
    '''
    Returns a list of selected nodes.
    '''
    pass


def getSelectedRootNodes():
    '''
    Returns a list of selected root nodes.
    '''
    pass


def getSuperRootNode():
    '''
    Returns the super root node.
    '''
    pass


def getTransformRootNode():
    '''
    Returns the transform root node.
    '''
    pass


def getUniquePath(node):
    '''
    Returns a unique path for this node.
    '''
    pass


def groupSelection():
    '''
    Groups the selected nodes under a newly created Transform3D node.
    '''
    pass


def hasNodeTag(tag, node):
    '''
    Checks if a node has a certain tag.
    '''
    pass


def hasNodeTags(tag, node):
    '''
    Checks if a node has a certain tag.
    '''
    pass


def hideNode(node):
    '''
    Hide the node from the perspective view and disable it on the scenegraph.
    '''
    pass


def hideNodes(nodes):
    '''
    Hide the nodes in the list from the perspective view and disable them on the scenegraph.
    '''
    pass


def ignoreAutoHeadlight():
    '''
    Ignores the automatic headlight if another lightsource is set.
    '''
    pass


def initFindCache():
    '''
    Build up an internal cache structure to speed up execution of the python commands findNode and findNodes.
    '''
    pass


def insertParentNode(newParent, node):
    '''
    Insert a new parent node.
    '''
    pass


def invertSelection():
    '''
    Inverts the current selection in the scenegraph.
    '''
    pass


def invertSelectionInGroup():
    '''
    Inverts the current selection inside the parent group in the scenegraph.
    '''
    pass


def isCloned(node):
    '''
    Checks if a node is cloned.
    '''
    pass


def macget():
    '''
    
    '''
    pass


def moveNode(from_, node, to):
    '''
    Move a node from "from" to "to".
    '''
    pass


def moveNodes(tos, froms, nodes):
    '''
    Move a List of nodes from a list "from" to a list "to".
    '''
    pass


def moveNodesAfter():
    '''
    Internal function.
    '''
    pass


def pasteNode(node):
    '''
    Paste a node into the scenegraph.
    '''
    pass


def pasteNodes(nodes):
    '''
    Paste some nodes into the scenegraph.
    '''
    pass


def rebuildClones():
    '''
    Rebuilds all clone nodes in case a operation has broken the cloning.
    '''
    pass


def removeSelectedNodes(nodes):
    '''
    Removes the selected node
    '''
    pass


def selectAll():
    '''
    Selects all objects from the scenegraph.
    '''
    pass


def selectNode(status, name, node):
    '''
    Select/Deselect a node.
    '''
    pass


def selectNodes(status, nodes):
    '''
    Select/Deselects multiple nodes.
    '''
    pass


def selectNodesNoUndo(status, nodes):
    '''
    Select/Deselects multiple nodes.
    '''
    pass


def selectParent():
    '''
    Selects the parent node from the currently selected node in the scenegraph.
    '''
    pass


def setBoundingBoxSelection(enabled):
    '''
    Sets bounding box selection mode.
    '''
    pass


def setSwitchChoiceByTag(node, tags):
    '''
    Sets the choice of a switch node based on the given tag.
    '''
    pass


def setSwitchChoiceByTags(matchAllTags, node, tags):
    '''
    Sets the choice of a switch node based on the given tags.
    '''
    pass


def showComponents(enabled):
    '''
    Sets show components mode.
    '''
    pass


def showNode(node):
    '''
    Show the node in the perspective view and enable it on the scenegraph.
    '''
    pass


def showNodes(nodes):
    '''
    Show the nodes in the list from the perspective view and enable them on the scenegraph.
    '''
    pass


def showScenegraph(status):
    '''
    Shows/hides the scenegraph widget.
    '''
    pass


def splitGeometryTris():
    '''
    Splits a geometry into triangles.
    '''
    pass


def subChilds(node, children):
    '''
    Remove a list of children from a node.
    '''
    pass


def uncreateNode(name, type, node, parent):
    '''
    Uncreates node with node, type, name, and parent.
    '''
    pass


def undeleteNode(node):
    '''
    Undeletes a node.
    '''
    pass


def undeleteNodes(nodes):
    '''
    Undelete a list of nodes.
    '''
    pass


def unshareNode(node):
    '''
    Unshares a subtree.
    '''
    pass


def unsplitGeometryTris():
    '''
    Merges a geometry that was split into triangles back to one geometry.
    '''
    pass


def updateScenegraph(force):
    '''
    Updates scenegraph.
    '''
    pass

