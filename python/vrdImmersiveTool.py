'''
vrdImmersiveTool
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
VR tool object.
'''

from typing import List


class QIcon():
    pass


class QWidget():
    pass


def getCheckable():
    '''
    Documentation missing
    '''
    pass


def getChecked():
    '''
    Documentation missing
    '''
    pass


def getCheckedCommand():
    '''
    Documentation missing
    '''
    pass


def getClickedCommand():
    '''
    Documentation missing
    '''
    pass


def getGroup():
    '''
    Documentation missing
    '''
    pass


def getHideAway() -> bool:
    '''
    Returns if the tool is hidden from the VR menu.
    '''
    return None


def getIcon():
    '''
    Documentation missing
    '''
    pass


def getIsInternal() -> bool:
    '''
    Returns if the tool is marked as internal. All tools that are created internally by default will have this flag set.
    '''
    return None


def getName():
    '''
    Documentation missing
    '''
    pass


def getText():
    '''
    Documentation missing
    '''
    pass


def getUncheckedCommand():
    '''
    Documentation missing
    '''
    pass


def getViewContent():
    '''
    Documentation missing
    '''
    pass


def getViewWidget():
    '''
    Documentation missing
    '''
    pass


def hideAway(value: bool):
    '''
    If value is True, this tool is not visible on the VR menu.
    '''
    pass


def setCheckable(value: bool):
    '''
    Sets the tool button to checkable.
    '''
    pass


def setChecked(value: bool):
    '''
    Sets the tool button to checked.
    '''
    pass


def setCheckedCommand(value: str):
    '''
    Sets the Python command that is executed when the button is checked.
    '''
    pass


def setClickedCommand(value: str):
    '''
    Sets the Python command that is executed on button click.
    '''
    pass


def setGroup(value: str):
    '''
    Changes the group in which the tool is inserted.
    '''
    pass


def setIcon(icon: QIcon):
    '''
    Sets the icon displayed on the VR tools menu.
    '''
    pass


def setIconData(data: str, format: str):
    '''
    Use a base64 encoded string to set the icon.
    '''
    pass


def setIconPath(iconPath: str):
    '''
    Use the image at the given path as an icon.
    '''
    pass


def setOnOffIconData(onData: str, offData: str, format: str):
    '''
    Use two base64 encoded strings to set the icon.
    '''
    pass


def setText(text: str):
    '''
    Changes the text displayed on the VR tools menu.
    '''
    pass


def setUncheckedCommand(value: str):
    '''
    Sets the Python command that is executed when the button is unchecked.
    '''
    pass


def setViewContent(value: str):
    '''
    On tool button press, the given content is displayed on a menu panel.
    '''
    pass


def setViewWidget(widget: QWidget):
    '''
    On tool button press, the given content is displayed on a menu panel.
    '''
    pass


def signal():
    '''
    Documentation missing
    '''
    pass

