'''
Autogenerated Method-Stub for:
module vrImmersiveInteractionService
------------------------------------------

API version: v2
Generation Date: 2020-04-24

VRED-Py: Visual Studio Code Tools for Autodesk VRED
'''

from typing import List



def activateGroundCalibrationMode(rightHand):
    '''
    Start ground calibration.
    '''
    pass



def getAutoCreateCollisionObjects():
    '''
    Returns whether collision objects are automatically created.
    '''
    pass



def getControllerVisualizationMode():
    '''
    Returns the current controller visualization mode.
    '''
    pass



def getControlMode():
    '''
    Returns the current control mode.
    '''
    pass



def getPreferredTooltipsMode():
    '''
    Returns whether to show tooltips on start.
    '''
    pass



def getRelativeTeleportOrientation():
    '''
    Returns if the angle of the orientation is taken from the wrists absolute or relative rotation.
    '''
    pass



def getTeleportGroundHeight():
    '''
    Returns the height of the ground plane used in �On Ground Plane� teleport mode.
    '''
    pass



def getTeleportGroundMode():
    '''
    Returns the current teleport ground mode.
    '''
    pass



def getTeleportRange():
    '''
    Returns the maximum teleport distance.
    '''
    pass



def hideControllerMessage(message):
    '''
    Hide a controller message.
    '''
    pass



def isHmdActive():
    '''
    Check if an HMD (VR) display mode is active.
    '''
    pass



def pickingMoved(hit):
    '''
    Triggers a pointer move event.
    '''
    pass



def pickingPressed(hit):
    '''
    Triggers a pointer button pressed event.
    '''
    pass



def pickingReleased(hit):
    '''
    Triggers a pointer button released event.
    '''
    pass



def setAutoCreateCollisionObjects(automatic):
    '''
    Toggles collision object creation for touch-sensors and web-engines.
    '''
    pass



def setControllerVisualizationMode(mode):
    '''
    Sets the visualization mode for the HMD controllers.
    '''
    pass



def setControlMode(mode):
    '''
    Sets the controle mode and corresponding button mappings for the immersive interactions.
    '''
    pass



def setDefaultInteractionsActive(active):
    '''
    Activates or deactivates all built-in interaction tools (teleport, pointer).
    '''
    pass



def setInteractionActive(name, active):
    '''
    Activates or deactivates the specified interaction tool. Built-in interactions are named �Teleport�, �Pointer�.
    '''
    pass



def setPreferredControllerVisualizeMode(mode):
    '''
    Toggles the default visualisation style for the hands.
    '''
    pass



def setPreferredTooltipsMode(show):
    '''
    Toggles whether to show tooltips when the session starts.
    '''
    pass



def setRelativeTeleportOrientation(isRelative):
    '''
    Sets if the angle of the orientation is taken from the wrists absolute or relative rotation.
    '''
    pass



def setTeleportGroundHeight(height):
    '''
    Sets the height of the ground plane for the �On Ground Plane� teleport mode.
    '''
    pass



def setTeleportGroundMode(mode):
    '''
    Sets whether to teleport on scene geometries, or to teleport only on a virtual ground plane.
    '''
    pass



def setTeleportRange(range):
    '''
    Sets the maximum teleport distance.
    '''
    pass



def setViewpointMode(adjustHeight, adjustOrientation, adjustPosition):
    '''
    Changes the default behavior for viewpoint selection. The actual camera position is the transformation of a viewpoint plus the transformation of the hmd. If adjustment is enabled, the camera position is modified in a way, that the resulting camera plus hmd position matches exaclty a viewpoint positon, height or orientation.
    '''
    pass



def showControllerMessage(data, rightHand):
    '''
    Show a controller message depending on the provided data.
    '''
    pass

