'''
vrdNode
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Base class for all nodes.
'''

from typing import List


class QMatrix4x4():
    pass


class string():
    pass


class integer():
    pass


class vrdNode():
    pass


def getChild(index: integer) -> vrdNode:
    '''
    Gets a child node by index.
    '''
    return None


def getChildCount() -> integer:
    '''
    Get the number of child nodes.
    '''
    return None


def getChildIndex(child: vrdNode) -> integer:
    '''
    Get the index of the child node in the list of children.
    '''
    return None


def getChildren() -> List[vrdNode]:
    '''
    Returns a list of all child nodes.
    '''
    return None


def getChildrenRecursive() -> List[vrdNode]:
    '''
    Returns a list of all child nodes recursively (including children of children).
    '''
    return None


def getName() -> string:
    '''
    Returns the name of the node.
    '''
    return None


def getParent() -> vrdNode:
    '''
    Returns the parent node.
    '''
    return None


def getSharedNodes() -> List[vrdNode]:
    '''
    Returns scene nodes that share this node.
    '''
    return None


def getVisibilityFlag() -> bool:
    '''
    Returns the local visibility flag.
    '''
    return None


def getWorldTransform() -> QMatrix4x4:
    '''
    Gets the world transformation matrix of this node.
    '''
    return None


def isShared() -> bool:
    '''
    Returns true, if this node has shared instances in the scene.
    '''
    return None


def isVisible() -> bool:
    '''
    Returns if the node is visible.
    '''
    return None


def setName(name: string):
    '''
    Sets the name of the node.
    '''
    pass


def setVisibilityFlag(visible: bool):
    '''
    Sets the local visibility flag.
    '''
    pass

