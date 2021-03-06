'''
vrCameraService
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Interface to access cameras and viewpoints in VRED.
'''

from typing import List


class vrdCameraNode():
    pass


class vrdCameraTrackNode():
    pass


class CameraConstraint():
    pass


class vrdViewpointNode():
    pass


class vrdNode():
    pass


class CameraProjectionMode():
    pass


class ViewpointCreationMode():
    pass


def createCamera(name: str, mode: CameraProjectionMode, constraint: CameraConstraint, sceneGraphParentNode: vrdNode, cameraGraphParentNode: vrdNode) -> vrdCameraNode:
    '''
    Creates a new camera.
    '''
    return None


def createCameraGroup(name: str, cameraGraphParentNode: vrdNode) -> vrdNode:
    '''
    Creates a new camera group.
    '''
    return None


def createCameraTrack(name: str, cameraNode: vrdCameraNode) -> vrdCameraTrackNode:
    '''
    Creates a new camera track.
    '''
    return None


def createViewpoint(name: str, cameraTrack: vrdCameraTrackNode) -> vrdViewpointNode:
    '''
    Creates a new viewpoint.
    '''
    return None


def duplicateNode(node: vrdNode) -> vrdNode:
    '''
    Creates a copy of a camera tree node (including its children).
    '''
    return None


def getActiveCamera(useCameraGraph: bool) -> vrdCameraNode:
    '''
    Returns the active camera of the currently active viewport.
    '''
    return None


def getAllCameraTracks() -> List[vrdCameraTrackNode]:
    '''
    Returns the list of all camera tracks.
    '''
    return None


def getAllViewpoints() -> List[vrdViewpointNode]:
    '''
    Returns the list of all viewpoints.
    '''
    return None


def getCamera(name: str, useCameraGraph: bool) -> vrdCameraNode:
    '''
    Returns the first camera with the given name.
    '''
    return None


def getCameraNames() -> List[str]:
    '''
    Returns a list with the names of all cameras.
    '''
    return None


def getCameraRoot() -> vrdNode:
    '''
    Returns the root node of cameras, that contains all cameras, camera tracks and viewpoints.
    '''
    return None


def getCameras(useCameraScenegraph: bool) -> List[vrdCameraNode]:
    '''
    Returns the list of all cameras (not including viewpoints or camera tracks).
    '''
    return None


def getViewpoint(name: str) -> vrdViewpointNode:
    '''
    Returns the first viewpoint with the given name.
    '''
    return None


def getViewpointCreationMode() -> ViewpointCreationMode:
    '''
    Returns if tracking transformation should be included in viewpoint transformation.
    '''
    return None


def load(filename: str) -> List[vrdNode]:
    '''
    Load camera related nodes.
    '''
    return None


def saveCameras(nodes: List[vrdNode], filename: str) -> bool:
    '''
    Save cameras and viewpoints to an .xml file (no hierarchy, groups or tracks supported).
    '''
    return None


def saveNodes(nodes: List[vrdNode], filename: str) -> bool:
    '''
    Save nodes including children (tracks, groups, viewpoints) to .osb file.
    '''
    return None


def saveViewpoints(filename: str) -> bool:
    '''
    Save all viewpoints to �.xml� file.
    '''
    return None


def setViewpointCreationMode(mode: ViewpointCreationMode):
    '''
    Defines if tracking transformation should be included in viewpoint transformation.
    '''
    pass

