'''
vrdPositionConstraintNode
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
This class gives access to a position constraint object in VRED. A position constraint will synchronize the position of a source and a target. If there are multiple sources, the position is calculated as the weighted average value of it.
'''

from typing import List


def getMaintainOffset() -> bool:
    '''
    Returns if the constraint maintains the offset to its sources.
    '''
    return None


def setMaintainOffset(value: bool):
    '''
    Sets if the constraint should maintain the offset to the sources when creating it.
    '''
    pass

