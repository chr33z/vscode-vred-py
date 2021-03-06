'''
vrPBAR
------------------------------------------
API version: v1 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------

'''

from typing import List


def activatePBAR():
    '''
    Activates PBAR rendering.
    '''
    pass


def deactivatePBAR():
    '''
    Deactivates PBAR rendering.
    '''
    pass


def observerLookAtPlane(nx, nz, pz, p3x, p2y, px, py, ny, p1y, p2x, p2z, p1x, p3y, p3z, p1z):
    '''
    Sets the lookAt plane for the observer.
    '''
    pass


def pbarDebug():
    '''
    Debug PBAR.
    '''
    pass


def setManualPBARAt(cz, cx, cy):
    '''
    Defines the manual "at" point for observer.
    '''
    pass


def setManualPBARPlane(p3x, p2y, p4y, p4z, p1y, p2x, p2z, p1x, p3y, p3z, p1z, p4x):
    '''
    Defines manual plane to approximate projection geometry using four points.
    '''
    pass


def setObserverEyeSeparation():
    '''
    Sets eye separation for the observer.
    '''
    pass


def setObserverLeftEyeOffset():
    '''
    Sets left eye offset for the observer.
    '''
    pass


def setObserverRightEyeOffset():
    '''
    Sets right eye offset for the observer.
    '''
    pass


def setUseManualPBARAt(state):
    '''
    Toggles use of manual "at" point for observer.
    '''
    pass


def setUseManualPBARPlane(state):
    '''
    Toggles use of manual plane to approximate projection geometry.
    '''
    pass


def setUseVirtualPBARTrackball(state):
    '''
    Toggles use of virtual trackball.
    '''
    pass


def setVirtualPBARTrackball(cz, dist, cx, cy):
    '''
    Sets up a virtual trackball for observer view.
    '''
    pass


def useManualObserverLookAtPlane(state):
    '''
    Toggles manual use of lookAt plane for the observer.
    '''
    pass

