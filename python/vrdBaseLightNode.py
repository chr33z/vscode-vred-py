'''
vrdBaseLightNode
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
This class is the base from which all other light nodes are derived from. It contains the functionality that is shared among all lights.
'''

from typing import List


class Unit():
    pass


class vrdLightTransform():
    pass


class integer():
    pass


class QVector3D():
    pass


def getCastShadowOnShadowMaterial() -> bool:
    '''
    Returns if the light casts a shadow on the shadow material.
    '''
    return None


def getDiffuseColor() -> QVector3D:
    '''
    Returns the diffuse color of the light.
    '''
    return None


def getGlossyColor() -> QVector3D:
    '''
    Returns the light�s glossy color.
    '''
    return None


def getGroundShadowIntensity() -> float:
    '''
    Returns the intensity of shadows on the shadow material.
    '''
    return None


def getIlluminateShadowMaterial() -> bool:
    '''
    Returns whether the light illuminates the shadow material.
    '''
    return None


def getImportanceMultiplier() -> float:
    '''
    Returns the importance multiplier of the light.
    '''
    return None


def getIntensity() -> float:
    '''
    Returns the intensity of the light.
    '''
    return None


def getIsPhysicallyBased() -> bool:
    '''
    Returns whether the light source is physically based.
    '''
    return None


def getLightTransform() -> vrdLightTransform:
    '''
    Returns the light transform.
    '''
    return None


def getLightUnit() -> Unit:
    '''
    Returns the unit used for this light source.
    '''
    return None


def getMaterialShadowIntensity() -> float:
    '''
    Returns the intensity of shadows of brdf based materials.
    '''
    return None


def getOn() -> bool:
    '''
    Returns the state of the light.
    '''
    return None


def getTemperature() -> integer:
    '''
    Returns the light temperature.
    '''
    return None


def getUseLightTemperature() -> bool:
    '''
    Returns whether the light uses the temperature value to determine its color.
    '''
    return None


def getVisualizationVisible() -> bool:
    '''
    Returns whether the light source visualization is visible.
    '''
    return None


def setCastShadowOnShadowMaterial(castShadow: bool):
    '''
    Set whether the light casts a shadow on the shadow material or not.
    '''
    pass


def setDiffuseColor(diffuseColor: QVector3D):
    '''
    Sets the diffuse color of the light.
    '''
    pass


def setGlossyColor(glossyColor: QVector3D):
    '''
    Sets the glossy color of the light.
    '''
    pass


def setGroundShadowIntensity(intensity: float):
    '''
    Sets the intensity of shadows on the shadow material.
    '''
    pass


def setIlluminateShadowMaterial(illuminateShadosMeterial: bool):
    '''
    Sets whether the light illuminates the shadow material.
    '''
    pass


def setImportanceMultiplier(importanceMultiplier: float):
    '''
    Sets the importance multiplier of the light.
    '''
    pass


def setIntensity(intensity: float):
    '''
    Sets the intensity of the light.
    '''
    pass


def setIsPhysicallyBased(on: bool):
    '''
    Sets whether the light source is physically based.
    '''
    pass


def setLightUnit(unit: Unit):
    '''
    Sets the unit used for this light source.
    '''
    pass


def setMaterialShadowIntensity(intensity: float):
    '''
    Sets the intensity of shadows of brdf based materials.
    '''
    pass


def setOn(on: bool):
    '''
    Switch the light on / off.
    '''
    pass


def setTemperature(kelvin: integer):
    '''
    Sets the light temperature.
    '''
    pass


def setUseLightTemperature(use: bool):
    '''
    Sets whether the light uses the temperature value to determine its color.
    '''
    pass


def setVisualizationVisible(showVisualization: bool):
    '''
    Sets whether the light source visualization is visible.
    '''
    pass

