'''
vrdTurntable
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
This class provides control over the turntable of a camera.
'''

from typing import List


class TurntableDirection():
    pass


def getAngle() -> float:
    '''
    Returns the angle of the turntable/.
    '''
    return None


def getAnimationDuration() -> float:
    '''
    Returns the duration of the turntable animation.
    '''
    return None


def getDirection() -> TurntableDirection:
    '''
    Returns the turntable animation playback direction.
    '''
    return None


def getDistance() -> float:
    '''
    Returns the distance of the turntable.
    '''
    return None


def getHeight() -> float:
    '''
    Returns the height of the turntable.
    '''
    return None


def getLoop() -> bool:
    '''
    Returns the state of the turntable animation loop mode.
    '''
    return None


def getPlaying() -> bool:
    '''
    Returns the playback state of the turntable animation.
    '''
    return None


def setAngle(angle: float):
    '''
    Sets the angle of the turntable.
    '''
    pass


def setAnimationDuration(seconds: float):
    '''
    Sets the duration of the turntable animation.
    '''
    pass


def setDirection(direction: TurntableDirection):
    '''
    Sets the playback direction of the turntable animation.
    '''
    pass


def setDistance(distance: float):
    '''
    Sets the distance of the turntable.
    '''
    pass


def setHeight(height: float):
    '''
    Sets the height of the turntable.
    '''
    pass


def setLoop(enable: bool):
    '''
    Sets the turntable animation to loop mode.
    '''
    pass


def setPlaying(value: bool):
    '''
    Starts / stops the turntable animation.
    '''
    pass


def updateFromView():
    '''
    Update the turntable parameters from the current view.
    '''
    pass

