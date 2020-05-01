'''
vrdCameraBaseNode
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
This class serves as base class for     vrdCameraNode and vrdViewpointNode.
'''

from typing import List


class QVector2D():
    pass


class vrdCameraBaseNode():
    pass


class QMatrix4x4():
    pass


class CameraStereoLayout():
    pass


class CameraProjectionMode():
    pass


class vrdImage():
    pass


class CameraEye():
    pass


class QColor():
    pass


class FogFalloffMode():
    pass


class vrdTonemapper():
    pass


class BlendMode():
    pass


class vrCameraFromAtUp():
    pass


class vrdPerspectiveMatch():
    pass


class vrdNode():
    pass


class QVector4D():
    pass


class CameraAxis():
    pass


class QVector3D():
    pass


class FovMode():
    pass


def adjustAtPosition(root: vrdNode):
    '''
    Adjust the look at point onto the surface of the closest object in the direction of viewing.
    '''
    pass


def getApplyColorCorrectionToBackground() -> bool:
    '''
    Returns if color correction should be applied to background.
    '''
    return None


def getApplyColorCorrectionToForeground() -> bool:
    '''
    Returns if color correction should be applied to foreground.
    '''
    return None


def getBlendAmount() -> float:
    '''
    Returns the amount of blending used.
    '''
    return None


def getBlendMapLeftEye() -> vrdImage:
    '''
    Returns the blending map for the left eye of the camera.
    '''
    return None


def getBlendMapRightEye() -> vrdImage:
    '''
    Returns the blending map for the right eye of the camera.
    '''
    return None


def getBlendMode() -> BlendMode:
    '''
    Returns the current blending mode.
    '''
    return None


def getColorCorrectionBrightness() -> float:
    '''
    Returns the color correction brightness.
    '''
    return None


def getColorCorrectionContrast() -> float:
    '''
    Returns the color correction contrast.
    '''
    return None


def getColorCorrectionHueOffset() -> float:
    '''
    Returns the color correction hue offset.
    '''
    return None


def getColorCorrectionSaturation() -> float:
    '''
    Returns the color correction saturation.
    '''
    return None


def getCustomFrustumEnabled() -> bool:
    '''
    Returns the state of the custom frustum.
    '''
    return None


def getCustomProjectionMatrix() -> QMatrix4x4:
    '''
    Returns the custom 4x4 projection matrix.
    '''
    return None


def getDepthOfField() -> bool:
    '''
    Returns the current depth of field state of the camera.
    '''
    return None


def getDistanceFog() -> bool:
    '''
    Returns the current activation state of distance-fog.
    '''
    return None


def getDistanceFogColor() -> QColor:
    '''
    Get the color of distance-fog.
    '''
    return None


def getDistanceFogDensity() -> float:
    '''
    Returns the density of distance-fog.
    '''
    return None


def getDistanceFogEnableNoiseSizeUniform() -> bool:
    '''
    Returns the uniform noise size flag for distance-fog.
    '''
    return None


def getDistanceFogFalloff() -> FogFalloffMode:
    '''
    Returns the falloff type of distance-fog.
    '''
    return None


def getDistanceFogNoise() -> float:
    '''
    Returns the noise intensity of distance-fog.
    '''
    return None


def getDistanceFogNoiseOffset() -> QVector3D:
    '''
    Returns the noise offset of distance-fog.
    '''
    return None


def getDistanceFogNoiseSize() -> QVector3D:
    '''
    Returns the noise size of distance-fog.
    '''
    return None


def getDistanceFogRange() -> float:
    '''
    Get the near value of distance-fog.
    '''
    return None


def getDistortion() -> bool:
    '''
    Returns if distortion is enabled.
    '''
    return None


def getDistortionMapLeftEye() -> vrdImage:
    '''
    Returns the distortion map for the left eye of the camera.
    '''
    return None


def getDistortionMapRightEye() -> vrdImage:
    '''
    Returns the distortion map for the left right of the camera.
    '''
    return None


def getFarClippingDistance() -> float:
    '''
    Returns the distance of the far clipping plane.
    '''
    return None


def getFocalLength() -> float:
    '''
    Returns the focal length.
    '''
    return None


def getFocusDistance() -> float:
    '''
    Returns the focus distance.
    '''
    return None


def getFov() -> float:
    '''
    Gets the field of view.
    '''
    return None


def getFovMode() -> FovMode:
    '''
    Returns the field of view mode.
    '''
    return None


def getFromAtUp() -> vrCameraFromAtUp:
    '''
    Gets the from at and up vectors in local space.
    '''
    return None


def getFromAtUpWorld() -> vrCameraFromAtUp:
    '''
    Returns from, at and up vectors in world space.
    '''
    return None


def getFrustum() -> QVector4D:
    '''
    Returns the custom frustum.
    '''
    return None


def getFrustumBottom() -> float:
    '''
    Returns the size bottom side of the frustum.
    '''
    return None


def getFrustumLeft() -> float:
    '''
    Returns the size left side of the frustum.
    '''
    return None


def getFrustumRight() -> float:
    '''
    Returns the size right side of the frustum.
    '''
    return None


def getFrustumTop() -> float:
    '''
    Returns the size top side of the frustum.
    '''
    return None


def getFStop() -> float:
    '''
    Returns the FStop of the camera,.
    '''
    return None


def getGlare() -> bool:
    '''
    Returns the current glare state of the camera.
    '''
    return None


def getGlareIntensity() -> float:
    '''
    Returns the glare intensity.
    '''
    return None


def getGlareRotation() -> float:
    '''
    Returns the glare rotation.
    '''
    return None


def getGlareSize() -> float:
    '''
    Returns the glare size.
    '''
    return None


def getGlareStreaks() -> int:
    '''
    Returns the number of glare streaks.
    '''
    return None


def getGlareThreshold() -> float:
    '''
    Returns the glare threshold.
    '''
    return None


def getGlow() -> bool:
    '''
    Returns the current glow state of the camera.
    '''
    return None


def getGlowFalloff() -> float:
    '''
    Returns the glow falloff.
    '''
    return None


def getGlowIntensity() -> float:
    '''
    Returns the glow intensity.
    '''
    return None


def getGlowSize() -> float:
    '''
    Returns the glow size.
    '''
    return None


def getGlowThreshold() -> float:
    '''
    Returns the glow threshold.
    '''
    return None


def getHeightFog() -> bool:
    '''
    Returns the current activation value of height-fog.
    '''
    return None


def getHeightFogBlend() -> float:
    '''
    Returns the blend value of height-fog.
    '''
    return None


def getHeightFogColor() -> QColor:
    '''
    Get the color of height-fog.
    '''
    return None


def getHeightFogDensity() -> float:
    '''
    Returns the density of height-fog.
    '''
    return None


def getHeightFogEnableNoiseSizeUniform() -> bool:
    '''
    Returns the uniform noise size flag for height-fog.
    '''
    return None


def getHeightFogFalloff() -> FogFalloffMode:
    '''
    Returns the falloff type of height-fog.
    '''
    return None


def getHeightFogNoise() -> float:
    '''
    Returns the noise intensity of height-fog.
    '''
    return None


def getHeightFogNoiseOffset() -> QVector3D:
    '''
    Returns the noise offset of height-fog.
    '''
    return None


def getHeightFogNoiseSize() -> QVector3D:
    '''
    Returns the noise size of height-fog.
    '''
    return None


def getHeightFogRange() -> QVector2D:
    '''
    Returns the range of height-fog.
    '''
    return None


def getLensFlare() -> bool:
    '''
    Queries if lens flares are visible for this camera.
    '''
    return None


def getMotionBlur() -> bool:
    '''
    Returns the current motion blur state of the camera.
    '''
    return None


def getNearClippingDistance() -> float:
    '''
    Returns the distance of the near clipping plane.
    '''
    return None


def getOrthographicSize() -> float:
    '''
    Returns the orthographic size.
    '''
    return None


def getPerspectiveMatch() -> vrdPerspectiveMatch:
    '''
    Gets the camera perspective match object.
    '''
    return None


def getPrincipalPointOffset() -> QVector2D:
    '''
    Returns the principal point offset.
    '''
    return None


def getProjectionMode() -> CameraProjectionMode:
    '''
    Returns the projection mode used for the camera.
    '''
    return None


def getRoll() -> float:
    '''
    Returns the camera roll.
    '''
    return None


def getSensorSize() -> QVector2D:
    '''
    Returns the sensor size.
    '''
    return None


def getShutterSpeed() -> float:
    '''
    Returns the shutter speed.
    '''
    return None


def getSkew() -> float:
    '''
    Returns the skew factor of the camera.
    '''
    return None


def getStereoEyeSeparation() -> float:
    '''
    Returns the stereo eye separation used during omnidirectional stereo rendering.
    '''
    return None


def getStereoLayout() -> CameraStereoLayout:
    '''
    Returns the stereo layout.
    '''
    return None


def getStereoPolarMergeAngle() -> float:
    '''
    Returns the polar merge angle used during omnidirectional stereo rendering.
    '''
    return None


def getTonemapper() -> vrdTonemapper:
    '''
    Returns the tone mapper.
    '''
    return None


def getViewpointTransition() -> bool:
    '''
    Returns if viewpoint transitions are enabled.
    '''
    return None


def getViewpointTransitionDuration() -> float:
    '''
    Returns the duration of viewpoint transitions.
    '''
    return None


def getVignetteFeather() -> float:
    '''
    Returns the vignette feather.
    '''
    return None


def getVignetteRadius() -> float:
    '''
    Returns the vignette radius.
    '''
    return None


def getVignetteRoundness() -> float:
    '''
    Returns the vignette roundness.
    '''
    return None


def getWireframeRendering() -> bool:
    '''
    Returns the state of wireframe rendering.
    '''
    return None


def isEditable() -> bool:
    '''
    Returns if the node is in a locked state or can be edited.
    '''
    return None


def isEqual(camera: vrdCameraBaseNode) -> bool:
    '''
    Determines if two camera nodes are internally using the same camera.
    '''
    return None


def isOrthographic() -> bool:
    '''
    Returns if the camera is using orthographic projection.
    '''
    return None


def loadBlendMap(fileName: str, eye: CameraEye) -> bool:
    '''
    Loads an image from a file and sets it as blending map for either the left or the right eye.
    '''
    return None


def loadDistortionMap(fileName: str, eye: CameraEye) -> bool:
    '''
    Loads an image from a file and sets it as distortion map for either the left or the right eye.
    '''
    return None


def mirrorView(axis: CameraAxis):
    '''
    Mirrors the camera view along one of the major axis.
    '''
    pass


def resetView():
    '''
    Zeros all values in the camera viewing matrix.
    '''
    pass


def setApplyColorCorrectionToBackground(enabled: bool):
    '''
    Enable / disable the color correction for the background.
    '''
    pass


def setApplyColorCorrectionToForeground(enabled: bool):
    '''
    Enable / disable the color correction for the foreground.
    '''
    pass


def setBlendAmount(value: float):
    '''
    Sets the amount of blending to use.
    '''
    pass


def setBlendMapLeftEye(image: vrdImage):
    '''
    Sets the blending map for the left eye of the camera.
    '''
    pass


def setBlendMapRightEye(image: vrdImage):
    '''
    Sets the blending map for the right eye of the camera.
    '''
    pass


def setBlendMode(mode: BlendMode):
    '''
    Sets and enables / disables the blending mode.
    '''
    pass


def setColorCorrectionBrightness(value: float):
    '''
    Sets the color correction brightness.
    '''
    pass


def setColorCorrectionContrast(value: float):
    '''
    Sets the color correction contrast.
    '''
    pass


def setColorCorrectionHueOffset(value: float):
    '''
    Sets the color correction hue offset.
    '''
    pass


def setColorCorrectionSaturation(value: float):
    '''
    Sets the color correction saturation.
    '''
    pass


def setCustomFrustumEnabled(enabled: bool):
    '''
    Enable / disable the use of a custom frustum.
    '''
    pass


def setCustomProjectionMatrix(matrix: QMatrix4x4):
    '''
    Sets a custom 4x4 projection matrix.
    '''
    pass


def setDepthOfField(enabled: bool):
    '''
    Enables / disables depth of field for the camera.
    '''
    pass


def setDistanceFog(enable: bool):
    '''
    Enables / disables distance-fog.
    '''
    pass


def setDistanceFogColor(color: QColor):
    '''
    Sets the color of the distance-fog.
    '''
    pass


def setDistanceFogDensity(density: float):
    '''
    Set the density of distance-fog.
    '''
    pass


def setDistanceFogEnableNoiseSizeUniform(enable: bool):
    '''
    Enables / disables uniform noise size for distance-fog.
    '''
    pass


def setDistanceFogFalloff(value: FogFalloffMode):
    '''
    Sets the falloff type of distance-fog.
    '''
    pass


def setDistanceFogNoise(intensity: float):
    '''
    Set the intensity of noise for distance-fog.
    '''
    pass


def setDistanceFogNoiseOffset(offset: QVector3D):
    '''
    Set the offset of noise for distance-fog.
    '''
    pass


def setDistanceFogNoiseSize(size: QVector3D):
    '''
    Set the size of noise for distance-fog.
    '''
    pass


def setDistanceFogRange(nearDistance: float):
    '''
    Sets where distance-fog begins.
    '''
    pass


def setDistortion(enabled: bool):
    '''
    Enable / disable distortion.
    '''
    pass


def setDistortionMapLeftEye(image: vrdImage):
    '''
    Sets the distortion map for the left eye of the camera.
    '''
    pass


def setDistortionMapRightEye():
    '''
    Documentation missing
    '''
    pass


def setFarClippingDistance(value: float):
    '''
    Sets the distance of the far clipping plane.
    '''
    pass


def setFocalLength(value: float):
    '''
    Sets the focal length.
    '''
    pass


def setFocusDistance(distance: float):
    '''
    Sets the focus distance.
    '''
    pass


def setFov(value: float):
    '''
    Sets the field of view.
    '''
    pass


def setFovMode(mode: FovMode):
    '''
    Sets the field of view mode.
    '''
    pass


def setFromAtUp(fromAtUp: vrCameraFromAtUp):
    '''
    Sets the from, at and up vectors in local space.
    '''
    pass


def setFromAtUpWorld(fromAtUp: vrCameraFromAtUp):
    '''
    Sets the from, at and up vectors in world space.
    '''
    pass


def setFrustum(frustum: QVector4D):
    '''
    Sets the custom frustum.
    '''
    pass


def setFrustumBottom(value: float):
    '''
    Sets the size of the bottom side of the frustum.
    '''
    pass


def setFrustumLeft(value: float):
    '''
    Sets the size of the left side of the frustum.
    '''
    pass


def setFrustumRight(value: float):
    '''
    Sets the size of the right side of the frustum.
    '''
    pass


def setFrustumTop(value: float):
    '''
    Sets the size of the top side of the frustum.
    '''
    pass


def setFStop(value: float):
    '''
    Sets the FStop of the camera.
    '''
    pass


def setGlare(enabled: bool):
    '''
    Enables / disables glare for the camera.
    '''
    pass


def setGlareIntensity(value: float):
    '''
    Sets the glare intensity.
    '''
    pass


def setGlareRotation(value: float):
    '''
    Sets the glare rotation.
    '''
    pass


def setGlareSize(value: float):
    '''
    Sets the glare size.
    '''
    pass


def setGlareStreaks(value: int):
    '''
    Sets the number of glare streaks.
    '''
    pass


def setGlareThreshold(value: float):
    '''
    Sets the glare threshold.
    '''
    pass


def setGlow(enabled: bool):
    '''
    Enables / disables glow for the camera.
    '''
    pass


def setGlowFalloff(value: float):
    '''
    Sets the glow falloff.
    '''
    pass


def setGlowIntensity(value: float):
    '''
    Sets the glow intensity.
    '''
    pass


def setGlowSize(value: float):
    '''
    Sets the glow size.
    '''
    pass


def setGlowThreshold(value: float):
    '''
    Sets the glow threshold.
    '''
    pass


def setHeightFog(enable: bool):
    '''
    Enables / disables height-fog.
    '''
    pass


def setHeightFogBlend(blend: float):
    '''
    Set the transition distance between fog and no fog.
    '''
    pass


def setHeightFogColor(color: QColor):
    '''
    Sets the color of the height-fog.
    '''
    pass


def setHeightFogDensity(density: float):
    '''
    Set the density of height-fog.
    '''
    pass


def setHeightFogEnableNoiseSizeUniform(enable: bool):
    '''
    Enables / disables uniform noise size for height-fog.
    '''
    pass


def setHeightFogFalloff(value: FogFalloffMode):
    '''
    Set the falloff of height-fog.
    '''
    pass


def setHeightFogNoise(intensity: float):
    '''
    Set the intensity of noise for height-fog.
    '''
    pass


def setHeightFogNoiseOffset(offset: QVector3D):
    '''
    Set the offset of noise for height-fog.
    '''
    pass


def setHeightFogNoiseSize(size: QVector3D):
    '''
    Set the size of noise for height-fog.
    '''
    pass


def setHeightFogRange(range: QVector2D):
    '''
    Sets where height-fog begins and where it ends.
    '''
    pass


def setLensFlare(enabled: bool):
    '''
    Enables / disables the visibility of lens flares for this camera.
    '''
    pass


def setMotionBlur(enabled: bool):
    '''
    Enables / disables motion blur for the camera.
    '''
    pass


def setNearClippingDistance(value: float):
    '''
    Sets the distance of the near clipping plane.
    '''
    pass


def setOrthographicSize(size: float):
    '''
    Sets the orthographic size.
    '''
    pass


def setPrincipalPointOffset(offset: QVector2D):
    '''
    Sets the principal point offset.
    '''
    pass


def setProjectionMode(mode: CameraProjectionMode):
    '''
    Sets the projection mode for the camera.
    '''
    pass


def setRoll(value: float):
    '''
    Sets the camera roll.
    '''
    pass


def setSensorSize(size: QVector2D):
    '''
    Sets the sensor size.
    '''
    pass


def setShutterSpeed(value: float):
    '''
    Sets the shutter speed used for motion blur.
    '''
    pass


def setSkew(value: float):
    '''
    Sets the skew factor of the camera.
    '''
    pass


def setStereoEyeSeparation(value: float):
    '''
    Sets eye separation used during omnidirectional stereo rendering.
    '''
    pass


def setStereoLayout(layout: CameraStereoLayout):
    '''
    Sets the image layout during omnidirectional stereo rendering.
    '''
    pass


def setStereoPolarMergeAngle(value: float):
    '''
    Sets the polar merge angle used during omnidirectional stereo rendering.
    '''
    pass


def setToCurrentView():
    '''
    Applies the current viewport transformation to the camera.
    '''
    pass


def setViewpointTransition(enabled: bool):
    '''
    Enables / disables a transition animation between viewpoints.
    '''
    pass


def setViewpointTransitionDuration(seconds: float):
    '''
    Sets the duration of viewpoint transitions.
    '''
    pass


def setVignetteFeather(value: float):
    '''
    Sets the vignette feather.
    '''
    pass


def setVignetteRadius(value: float):
    '''
    Sets the radius of the vignette used for blending.
    '''
    pass


def setVignetteRoundness(value: float):
    '''
    Sets the vignette roundness.
    '''
    pass


def setWireframeRendering(enabled: bool):
    '''
    Enables / disables wireframe rendering.
    '''
    pass

