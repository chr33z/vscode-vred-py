'''
Autogenerated Method-Stub for:
module vrDeviceService
------------------------------------------

API version: v2
Generation Date: 2020-04-24

VRED-Py: Visual Studio Code Tools for Autodesk VRED
'''

from typing import List



def activateInteraction(interaction):
    '''
    Activates an interaction. This allows an interaction to resume receiving input signals, if the interaction is in the active interaction group.
    '''
    pass



def createInteraction(name):
    '''
    Creates a new device interaction and makes it available for mapping inputs to its actions.
    '''
    pass



def createVRDevice(name):
    '''
    Creates a virtual device. This can be used to integrate custom hand tracking wtih python.
    '''
    pass



def deactivateInteraction(interaction):
    '''
    Deactivates an interaction. The interaction will not receive input signals anymore.
    '''
    pass



def deleteVRDevice(device):
    '''
    Removes a virtual device.
    '''
    pass



def getActiveInteractionGroup():
    '''
    Gets the currently active interaction group.
    '''
    pass



def getConnectedVRDevices():
    '''
    Gets the connected VR devices like controllers or trackers.
    '''
    pass



def getInteraction(name):
    '''
    Gets an interactions that is already known to the service.
    '''
    pass



def getInteractions():
    '''
    Gets all interactions that are known to the service.
    '''
    pass



def getTrackingOrigin():
    '''
    Returns the tracking reference origin. Default is (0, 0, 0). Can be changed with setTrackingOrigin.
    '''
    pass



def getVRDevice(name):
    '''
    Gets an VR device, which can be a controllers or a trackers by its name.
    '''
    pass



def getVRDeviceBySerialNumber(serialNumber):
    '''
    Gets an VR device, which can be a controllers or a trackers by its serial number.
    '''
    pass



def removeInteraction(interaction):
    '''
    Removes an interaction from the input mapping.
    '''
    pass



def setActiveInteractionGroup(interactionGroup):
    '''
    Activates a group of interactions which will from now on receive all the input signals. This will also deactivate all other interaction groups as only one interaction group can be active.
    '''
    pass



def setTrackingOrigin(position):
    '''
    Sets the tracking reference origin for tracking. Use it to correct any offsets in the scene This function always assumes Y-Up, even if Z-up is set in the scene. If the tracking origin should be at pos = (x_scene, y_scene, z_scene) in the VRED scene, call setTrackingOrigin(QVector3D(-x_scene, -z_scene, y_scene))
    '''
    pass

