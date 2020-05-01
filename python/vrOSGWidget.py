'''
vrOSGWidget
------------------------------------------
API version: v1 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------

'''

from typing import List


def getHeightAboveGround(index):
    '''
    Returns the height above the ground.
    '''
    pass


def getHeightAboveGround(node, index):
    '''
    Returns the height above the ground.
    '''
    pass


def getSceneIntersection(rayOrigin, rayDirection, index):
    '''
    Returns the intersection of the given ray with the scene.
    '''
    pass


def getSceneIntersection(xCoord, yCoord, index):
    '''
    Returns the intersection of the view ray of the active camera through the given pixel coordinates in the render window.
    '''
    pass


def getUserCameraMatrix(cameraName, userId):
    '''
    Gets the user projection camera world matrix (column-wise).
    '''
    pass


def getUserCameraMatrix(windowId, userId):
    '''
    Gets the user projection camera world matrix (column-wise).
    '''
    pass


def setCameraHeightAboveGround(relativeHeight, index):
    '''
    Set camera "relativeHeight" above the ground
    '''
    pass


def setCameraHeightAboveGround(keepAt, relativeHeight, index):
    '''
    Set camera "relativeHeight" above the ground
    '''
    pass


def setCameraHeightAboveGround(groundNode, relativeHeight, index):
    '''
    Set camera "relativeHeight" above the ground.
    '''
    pass


def zoomTo(node):
    '''
    Zooms to node.
    '''
    pass


def zoomTo(use_at, node):
    '''
    Zooms to node.
    '''
    pass


def adaptZeroParallaxDistance(index):
    '''
    Automatically adjusts the zero parallax distance.
    '''
    pass


def addRenderOverlay():
    '''
    Documentation missing
    '''
    pass


def cancelAntialiasing():
    '''
    Cancels the still anti-aliasing.
    '''
    pass


def clearRecordedStatistics(index):
    '''
    Deletes all recorded statistics of the given render window.
    '''
    pass


def compressTextures():
    '''
    Compresses all the textures.
    '''
    pass


def createBackplate():
    '''
    Deprecated.
    '''
    pass


def createRenderWindow():
    '''
    Creates a new render window.
    '''
    pass


def createScreenshot(filename):
    '''
    Creates a screenshot of the render window and writes out a image file.
    '''
    pass


def deleteBackplate():
    '''
    Deprecated.
    '''
    pass


def destroyRenderWindow(index):
    '''
    Destroys a render window.
    '''
    pass


def enableAntialiasing(switch):
    '''
    Sets anti-aliasing.
    '''
    pass


def enableDrawAction(state, index):
    '''
    Enables draw action.
    '''
    pass


def enableHeadlight(switch):
    '''
    Sets the headlight state.
    '''
    pass


def enablePowerwall(window, state):
    '''
    Enables local powerwall mode.
    '''
    pass


def enableRaytracing(state):
    '''
    Enables or disables raytracing.
    '''
    pass


def enableRaytracingDownscale(switch):
    '''
    Sets raytracing downscale.
    '''
    pass


def enableRender(switch):
    '''
    Sets rendering state.
    '''
    pass


def enableRenderRegion(s):
    '''
    Sets region rendering.
    '''
    pass


def enableStereo(zp, passive, window, mode, state, es):
    '''
    Enables stereo.
    '''
    pass


def getAntialiasingEnabled():
    '''
    Checks, if anti-aliasing is enabled.
    '''
    pass


def getAspect():
    '''
    Gets the aspect ratio.
    '''
    pass


def getAt(index):
    '''
    Returns "at" point.
    '''
    pass


def getAuxiliaryNodesVisibleDuringAntialiasing():
    '''
    Returns the visibility state of the auxiliary nodes during antialiasing.
    '''
    pass


def getAverageFPS():
    '''
    Returns the average number of frames per second.
    '''
    pass


def getBackplateMaterial():
    '''
    Deprecated.
    '''
    pass


def getCamNode(index):
    '''
    Gets the camera node.
    '''
    pass


def getCameraPivotAlwaysVisible():
    '''
    Returns the visibility state of the the camera pivot while not navigating.
    '''
    pass


def getCameraPivotVisible():
    '''
    Returns the visibility state of the the camera pivot .
    '''
    pass


def getDollySpeed():
    '''
    Get the scalefactor of the navigator dolly speed.
    '''
    pass


def getFPS():
    '''
    Returns the current number of frames per second.
    '''
    pass


def getFar():
    '''
    Gets the far clipping plane.
    '''
    pass


def getFov():
    '''
    Gets the field of view.
    '''
    pass


def getFrom(index):
    '''
    Returns "from" point.
    '''
    pass


def getGenlockingFrameCount():
    '''
    Returns current genlocking frame count.
    '''
    pass


def getInteractionMode():
    '''
    Get the interaction mode.
    '''
    pass


def getInternalBackplateMaterial():
    '''
    Deprecated.
    '''
    pass


def getLastPickingMaterial():
    '''
    Returns the last picked material.
    '''
    pass


def getLastPickingNode():
    '''
    Returns the last picked node.
    '''
    pass


def getLastPickingPosition():
    '''
    Returns the last picked position.
    '''
    pass


def getMotionFactor():
    '''
    Returns the current motion factor.
    '''
    pass


def getMousePosition(index):
    '''
    Returns the current pixel coordinates of the mouse over the given render window.
    '''
    pass


def getNavigationPivot(index):
    '''
    Returns navigation pivot.
    '''
    pass


def getNavigationSpeedMode():
    '''
    Get the navigation speed mode.
    '''
    pass


def getNear():
    '''
    Gets the near clipping plane.
    '''
    pass


def getNodeMaterial(node):
    '''
    Returns the temporary override material a node uses in OpenGL.
    '''
    pass


def getOculusRiftTrackingOrigin():
    '''
    Returns the Oculus Rift tracking reference origin.
    '''
    pass


def getOculusRiftTrackingOriginType():
    '''
    Windows only: Retrieves the tracking origin type for the oculus rift.
    '''
    pass


def getPanningSpeed():
    '''
    Get the scalefactor of the navigator panning speed.
    '''
    pass


def getRaytracingEnabled():
    '''
    Checks, if raytracing is enabled.
    '''
    pass


def getRenderRoot(index):
    '''
    Gets the render root.
    '''
    pass


def getRenderRoots(index):
    '''
    Gets the render roots.
    '''
    pass


def getRenderWindowCount():
    '''
    Returns number of render windows.
    '''
    pass


def getRenderWindowHeight(i):
    '''
    Returns the render window height.
    '''
    pass


def getRenderWindowWidth(i):
    '''
    Returns the render window width.
    '''
    pass


def getRoll(index):
    '''
    Get navigator roll.
    '''
    pass


def getSAAWindow():
    '''
    Returns the still anti-aliasing window.
    '''
    pass


def getShadowPlane(shadowPlaneNameRegexp, rootNode):
    '''
    Get the Shadow Plane given a regexp.
    '''
    pass


def getShowASides():
    '''
    Returns the state of the A Side rendering flag.
    '''
    pass


def getShowBSides():
    '''
    Returns the state of the B Side rendering flag.
    '''
    pass


def getSuperSampling():
    '''
    Checks, if super sampling is enabled.
    '''
    pass


def getSuperSamplingQuality():
    '''
    Returns the current realtime antialiasing quality.
    '''
    pass


def getUp(index):
    '''
    Returns "up" vector.
    '''
    pass


def getUseBindless():
    '''
    Returns whether bindless graphics should be used or not.
    '''
    pass


def getUseCommandList():
    '''
    Returns whether command list extension should be used or not.
    '''
    pass


def getUseMulticastSLI():
    '''
    Returns whether multicast SLI should be used or not.
    '''
    pass


def getUsePivotBasedPanning():
    '''
    Get the panning mode of the navigator.
    '''
    pass


def getUseSinglePassStereo():
    '''
    Returns whether single pass stereo is activated for stereo rendering or not
    '''
    pass


def getUseVariableRateShading():
    '''
    Documentation missing
    '''
    pass


def getUserMatrix(id):
    '''
    Gets the user projection transform matrix (column-wise).
    '''
    pass


def getUserNode():
    '''
    Deprecated.
    '''
    pass


def getVariableRateShadingMode():
    '''
    Documentation missing
    '''
    pass


def getVariableRateShadingQuality():
    '''
    Documentation missing
    '''
    pass


def getViewAt(index):
    '''
    Returns "ViewAt" point.
    '''
    pass


def getViewRay(xCoord, yCoord, index):
    '''
    Returns a ray that starts at the active camera and goes through the pixel at the given coordinates (x, y) in the render window.
    '''
    pass


def hideBanner():
    '''
    Hides a banner.
    '''
    pass


def moveRenderWindow(yPos, xPos, index):
    '''
    Moves a render window.
    '''
    pass


def moveStatistic(y, x):
    '''
    Sets the position of the render statistic.
    '''
    pass


def refreshAllGLObjects():
    '''
    Refreshs all existing GL objects.
    '''
    pass


def reinitializeAllGLObjects():
    '''
    Reinitialize all OpenGL objects to speed up rendering.
    '''
    pass


def resetGenlockingFrameCount():
    '''
    Resets genlocking frame count.
    '''
    pass


def resetHMDPose():
    '''
    While using a HMD display mode, resets the tracking to the current pose of the headset.
    '''
    pass


def resetIsolateView(index):
    '''
    Resets the isolate view on the render window.
    '''
    pass


def resetNodeMaterial(node):
    '''
    Resets the temporary node material override.
    '''
    pass


def resetNodeMaterials():
    '''
    Resets all temporary node material overrides.
    '''
    pass


def resetOculusRiftOrientation():
    '''
    Resets the tracking origin according to the current headset location and sets the yaw orientation to the current headset yaw value.
    '''
    pass


def resetRenderRoots():
    '''
    Resets render root.
    '''
    pass


def resizeRenderWindow(height, width, index):
    '''
    Resizes a render window.
    '''
    pass


def setAORendering(state):
    '''
    Enables or disables ambient occlusion rendering.
    '''
    pass


def setAOShadowsVisible(state):
    '''
    Enables or disables ambient occlusion shadows for OpenGL.
    '''
    pass


def setActiveRenderPass(passID, index):
    '''
    Sets the renderpass for the specified window.
    '''
    pass


def setAllGradientBackgrounds(colors, ints):
    '''
    Sets gradient background for all render windows.
    '''
    pass


def setAllNavigationsEnabled(state):
    '''
    Activates Navigation for all MGLW.
    '''
    pass


def setAnalyticRendering(state):
    '''
    Enables or disables analytic rendering.
    '''
    pass


def setAspect(aspect):
    '''
    Sets the aspect ratio.
    '''
    pass


def setAt(y, z, x, point, index):
    '''
    Set camera "at" point.
    '''
    pass


def setAutoFrustum(switch):
    '''
    Sets the auto frustum.
    '''
    pass


def setAuxiliaryNodesVisibleDuringAntialiasing(state):
    '''
    Enable/disable display of auxiliary nodes during antialiasing.
    '''
    pass


def setBackfaceCulling(switch):
    '''
    Renders the whole scene with backface culling.
    '''
    pass


def setBackplate():
    '''
    Deprecated.
    '''
    pass


def setCameraBeacon():
    '''
    Deprecated.
    '''
    pass


def setCameraConstraint(camera_constraint, min_dist):
    '''
    Sets camera constraint and optionally the minimum distance.
    '''
    pass


def setCameraPanning(y, x):
    '''
    Panning of the camera.
    '''
    pass


def setCameraPivotAlwaysVisible(state):
    '''
    Enable/disable display of the camera pivot while not navigating.
    '''
    pass


def setCameraPivotVisible(state):
    '''
    Enable/disable display of the camera pivot during navigation.
    '''
    pass


def setCameraRotation(y, x):
    '''
    Rotates the camera.
    '''
    pass


def setCameraScale(y, z, x):
    '''
    Scales the camera, e.g for vertical flipping (1, -1, 1).
    '''
    pass


def setCameraZUp(state):
    '''
    Sets camera z up.
    '''
    pass


def setCameraZoom(distance):
    '''
    Zooms the camera.
    '''
    pass


def setClusterCameraConnection(state):
    '''
    Sets the connection of the cameras in a cluster.
    '''
    pass


def setCorrectDoubleSidedLighting():
    '''
    Deprecated.
    '''
    pass


def setDefaultCameraBeacons():
    '''
    Deprecated.
    '''
    pass


def setDiscontinuityRendering(state):
    '''
    Enables or disables surface analysis rendering.
    '''
    pass


def setDisplayMode(mode):
    '''
    Sets the display mode.
    '''
    pass


def setDistance(distance, index):
    '''
    Set camera distance.
    '''
    pass


def setDollySpeed(scalefactor):
    '''
    Set the scalefactor for the navigator dolly speed.
    '''
    pass


def setDoubleSidedLighting():
    '''
    Deprecated.
    '''
    pass


def setEvaluateClipping(state):
    '''
    Enables or disables clipping plane evaluation in OpenGL.
    '''
    pass


def setEyeSeparation(es):
    '''
    Sets eye separation factor.
    '''
    pass


def setFaceNormalRendering(state):
    '''
    Enables or disables face normal rendering.
    '''
    pass


def setFar(far):
    '''
    Sets the far clipping plane.
    '''
    pass


def setFixedRenderWindowSize(height, width):
    '''
    Set a fixed size for the main render window.
    '''
    pass


def setFlyMode(switch):
    '''
    Switches between virtual trackball and fly navigation.
    '''
    pass


def setForceTransparentObjectSelection(mode):
    '''
    Enables/diables the selection of objects with a 100% transparent material in the render window.
    '''
    pass


def setFov(fov):
    '''
    Sets the field of view.
    '''
    pass


def setFreezeOcclusionCulling(freezeCulling):
    '''
    Freezes the current state of the occlusion culling for debugging purposes.
    '''
    pass


def setFrom(y, z, x, point, index):
    '''
    Set camera "from" point.
    '''
    pass


def setFromAtUp(uy, ax, fy, fz, ay, uz, at, az, up, from_, fx, ux, index):
    '''
    Set camera "from", "at" and "up".
    '''
    pass


def setFrustum(right, top, bottom, left, index):
    '''
    Set camera frustum
    '''
    pass


def setFrustumCulling(switch):
    '''
    Sets the frustum culling.
    '''
    pass


def setGenlocking(state):
    '''
    Enables or disables genlocking.
    '''
    pass


def setGradientBackground(colors, ints, index):
    '''
    Sets gradient background for a given render window.
    '''
    pass


def setGrainSize():
    '''
    Deprecated.
    '''
    pass


def setHighQualityAntialiasing(state):
    '''
    Enables or disables high quality anti-aliasing.
    '''
    pass


def setIndirectRendering(state):
    '''
    Enables or disables indirect illumination rendering.
    '''
    pass


def setInteractionMode(mode):
    '''
    Set the interaction mode.
    '''
    pass


def setIsolateView(roots, index):
    '''
    Sets the isolate view on the provided objects.
    '''
    pass


def setKeepRaytracingStructure(switch):
    '''
    Enables or disables keeping of the raytracing structure.
    '''
    pass


def setLocalLights(switch):
    '''
    Sets local light source mode.
    '''
    pass


def setMono(state, index):
    '''
    Disable stereo.
    '''
    pass


def setMotionFactor(factor):
    '''
    Sets motion factor.
    '''
    pass


def setNavMode(mode):
    '''
    Switches between different navigation modi.
    '''
    pass


def setNavOrbitMode(enabled):
    '''
    Sets navigation orbit mode to on/off.
    '''
    pass


def setNavigationSpeedMode(mode):
    '''
    Set the navigator speed mode for two axis and trackball navigation modes.
    '''
    pass


def setNear(near):
    '''
    Sets the near clipping plane.
    '''
    pass


def setNodeMaterial(mat, node):
    '''
    Sets a temporary override for the material a node uses for rendering in OpenGL.
    '''
    pass


def setOcclusionCulling(switch):
    '''
    Sets the occlusion culling state.
    '''
    pass


def setOcclusionCullingMode(mode):
    '''
    Sets the occlusion culling mode.(experimental)
    '''
    pass


def setOculusRiftHmdCaps():
    '''
    Deprectated
    '''
    pass


def setOculusRiftTracking(s):
    '''
    Windows only: Enables/Disables tracking of the oculus rift.
    '''
    pass


def setOculusRiftTrackingOrigin(position):
    '''
    Sets the tracking reference origin for oculus rift tracking.
    '''
    pass


def setOculusRiftTrackingOriginType(originType):
    '''
    Windows only: Sets the tracking origin type for the oculus rift.
    '''
    pass


def setOpenGLDebugging(s):
    '''
    Enables/Disables OpenGL Debugging.
    '''
    pass


def setPanningSpeed(scalefactor):
    '''
    Set the scalefactor for the navigator panning speed when pivot based panning or linear navigation is turned on.
    '''
    pass


def setPivot(y, z, x, point, index):
    '''
    Set navigator rotation pivot.
    '''
    pass


def setPostprocessAntialiasingMode(on):
    '''
    Enables/Disables postprocessing antialiasing.
    '''
    pass


def setPowerwallWindow():
    '''
    Sets the size of the virtual powerwall window in world coordinates.
    '''
    pass


def setRaytracingDownscaleFactor(factor):
    '''
    Sets the raytracing downscale factor.
    '''
    pass


def setRealisticRendering(state):
    '''
    Enables or disables realistic rendering.
    '''
    pass


def setRenderFullscreen(state):
    '''
    Maximizes/minimizes the render widget.
    '''
    pass


def setRenderQuality(quality):
    '''
    Sets the render quality.
    '''
    pass


def setRenderRegion(endY, startY, on, endX, startX):
    '''
    Sets render region parameters.
    '''
    pass


def setRenderRoot(root, index):
    '''
    Sets render root.
    '''
    pass


def setRenderRoots(roots, index):
    '''
    Sets render roots.
    '''
    pass


def setRenderWindowDocked(state, flags, index):
    '''
    Docks a render window.
    '''
    pass


def setRoll(roll, index):
    '''
    Set navigator roll.
    '''
    pass


def setSAAWindow(id):
    '''
    Sets the still anti-aliasing window, -1 means use window with focus.
    '''
    pass


def setScreenspaceAO(state):
    '''
    Enables or disables screen space ambient occlusion in OpenGL.
    '''
    pass


def setSelectionMode(mode):
    '''
    Sets the selection mode.
    '''
    pass


def setShadeTileSize():
    '''
    Deprecated.
    '''
    pass


def setShadow(switch):
    '''
    Sets shadow state.
    '''
    pass


def setShowABSides(showBSides, showASides):
    '''
    Enable/disable the rendering of A and B Sides.
    '''
    pass


def setSnapshotFrame(height, width, state):
    '''
    Show snapshot frame.
    '''
    pass


def setSortTrans(switch):
    '''
    Sets transparent sorting.
    '''
    pass


def setSpaceMouseHeight(height):
    '''
    Sets a fixed height in spacemouse mode.
    '''
    pass


def setSpaceMousePivotMode(i):
    '''
    Sets the spacemouse pivot mode.
    '''
    pass


def setSpaceMouseTwoAxis(s):
    '''
    Sets the two axis mode for the spacemouse.
    '''
    pass


def setSpaceMouseViewMode(i):
    '''
    Sets the spacemouse view mode.
    '''
    pass


def setSpecTexLighting():
    '''
    Deprecated.
    '''
    pass


def setStillDOF(focaldistance, radius, state):
    '''
    Enables depth of field.
    '''
    pass


def setSuperSampling(state):
    '''
    Enables or disables super sampling.
    '''
    pass


def setSuperSamplingOnCameraMovement(state):
    '''
    Enables/Disables super sampling on camera movements.
    '''
    pass


def setSuperSamplingQuality(quality):
    '''
    Sets the super sampling quality.
    '''
    pass


def setTransformNodeSelectionPressed(node):
    '''
    Select a transform node by mouse press event.
    '''
    pass


def setTransformNodeSelectionReleased(node):
    '''
    Deselect of a transform node by mouse release event.
    '''
    pass


def setTwoSidedLighting():
    '''
    Deprecated.
    '''
    pass


def setUp(y, z, x, vector, index):
    '''
    Set camera "up" vector.
    '''
    pass


def setUseBindless(bindlessEnable):
    '''
    Windows only, Experimental: Enables/Disables the use of bindless graphics extension if available.
    '''
    pass


def setUseCommandList(commandlistEnable):
    '''
    Windows only, Experimental: Enables/Disables use of command list extension.
    '''
    pass


def setUseLastDrawTree(s):
    '''
    Re-use old draw tree.
    '''
    pass


def setUseMulticastSLI(multicastEnable):
    '''
    Windows only: Enables/Disables use of multicast SLI for stereo rendering if present.
    '''
    pass


def setUsePivotBasedPanning(on):
    '''
    Set the navigator panning mode to be based on the pivot.
    '''
    pass


def setUseSinglePassStereo(on):
    '''
    Windows only: Enables/Disables use of single pass stereo if supported.
    '''
    pass


def setUseSpaceMouseHeight(value):
    '''
    Sets whether a fixed height is used or not.
    '''
    pass


def setUseVariableRateShading(state):
    '''
    Enable or disable variable rate shading.
    '''
    pass


def setUserMatrix(id, matrix):
    '''
    Sets the user projection transform matrix (column-wise).
    '''
    pass


def setVSyncInterval(interval):
    '''
    Sets the V-Sync swap interval.
    '''
    pass


def setVariableRateShadingMode(mode):
    '''
    Set shading rate mode.
    '''
    pass


def setVariableRateShadingQuality(quality):
    '''
    Set a predefined shading quality for uniform and foveated rendering.
    '''
    pass


def setViewportCamera(cameraNode, index):
    '''
    Sets the active camera for the given render window to the camera of the given camera node.
    '''
    pass


def setVolumeDrawing(switch):
    '''
    Sets volume drawing mode.
    '''
    pass


def setWireframe(switch):
    '''
    Sets wireframe rendering mode.
    '''
    pass


def setWireframeSelection(switch):
    '''
    Sets wireframe selection mode.
    '''
    pass


def setZWriteTrans(switch):
    '''
    Sets z write transparency.
    '''
    pass


def setZeroParallaxDistance(zp):
    '''
    Sets zero parallax distance.
    '''
    pass


def showADSKLogo(state):
    '''
    Enable/disable Autodesk logo.
    '''
    pass


def showBanner(height, text, t, bcolor, width):
    '''
    Shows a banner on all render widgets.
    '''
    pass


def showCoordinateSystem(switch):
    '''
    Sets display of the render coordinate systems.
    '''
    pass


def showInitialView():
    '''
    Show initial view.
    '''
    pass


def showOculusRiftPerformanceHUD(mode):
    '''
    Sets oculus rift performance HUD .
    '''
    pass


def showPIVRLogo(state):
    '''
    Enable/disable Autodesk logo.
    '''
    pass


def showProgressCursor(s):
    '''
    Show progress cursor.
    '''
    pass


def showStatistic(switch):
    '''
    Sets display of the render statistic.
    '''
    pass


def showVRECLogo(state):
    '''
    Enable/disable Autodesk logo.
    '''
    pass


def showViewCube(s):
    '''
    Show view cube.
    '''
    pass


def showWholeScene():
    '''
    Shows the whole scene.
    '''
    pass


def startStatisticsRecording(index):
    '''
    Starts (resumes) recording statistical data of the given render window.
    '''
    pass


def stopStatisticsRecording(index):
    '''
    Stops (pauses) recording statistical data of the given render window.
    '''
    pass


def subRenderOverlay():
    '''
    Documentation missing
    '''
    pass


def toggleFullscreen(multiDisplayFullscreen, index):
    '''
    switched between fullscreen and normal mode.
    '''
    pass


def toggleRaytracing(state):
    '''
    Toggle RayTracing on/off
    '''
    pass


def updateAllMGLW():
    '''
    Updates all MGLW.
    '''
    pass


def updateAllMGLWAll():
    '''
    Updates all MGLW.
    '''
    pass


def writeRecordedStatistics(path, index):
    '''
    Write all recorded statistics of the given render window to a csv file.
    '''
    pass

