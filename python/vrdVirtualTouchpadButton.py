'''
vrdVirtualTouchpadButton
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Represents a virtual button loacted on a touchpad of an VR controller. This virtual button can be used to split up the touchpad on a VR controller that can be used as regular buttons by the input mapping system.
'''

from typing import List


class vrdVirtualTouchpadButton():
    pass


def getEndAngle() -> float:
    '''
    Gets the end angle of the virtual button.
    '''
    return None


def getMaxRadius() -> float:
    '''
    Gets the maximum radius of the virtual button.
    '''
    return None


def getMinRadius() -> float:
    '''
    Gets the minimum radius of the virtual button.
    '''
    return None


def getName() -> str:
    '''
    Gets the name of the virtual button.
    '''
    return None


def getStartAngle() -> float:
    '''
    Gets the start angle of the virtual button.
    '''
    return None


def getVirtualButtonId() -> int:
    '''
    Gets the virtual button id, which is set internally.
    '''
    return None


def setEndAngle(end: float):
    '''
    Sets the end angle of the virtual button.
    '''
    pass


def setMaxRadius(max: float):
    '''
    Sets the maximum radius if the virtual button.
    '''
    pass


def setMinRadius(min: float):
    '''
    Sets the minimum radius of the virtual button.
    '''
    pass


def setName(name: str):
    '''
    Sets the name of the virtual button.
    '''
    pass


def setStartAngle(start: float):
    '''
    Sets the start angle of the virtual button.
    '''
    pass


def vrdVirtualTouchpadButton():
    '''
    Default constructor.
    '''
    pass


def vrdVirtualTouchpadButton(button: vrdVirtualTouchpadButton):
    '''
    Copy constructor.
    '''
    pass


def vrdVirtualTouchpadButton(name: str, minRadius: float, maxRadius: float, startAngle: float, endAngle: float):
    '''
    Constructor that creates an object with all necessary parameters to describe the virtual button.
    '''
    pass

