'''
Autogenerated Method-Stub for:
module vrRenderSettings
------------------------------------------

API version: v1
Generation Date: 2020-04-24

VRED-Py: Visual Studio Code Tools for Autodesk VRED
'''

from typing import List



def addPreset(name):
    '''
    Add preset to Render Queue.
    '''
    pass



def applyPreset(name):
    '''
    Apply preset in Render Queue .
    '''
    pass



def clearRenderVariantSetGroups():
    '''
    Removes all variant set groups.
    '''
    pass



def disableRaytracingOverrides():
    '''
    Disables the raytracing override settings in all materials.
    '''
    pass



def generateRayFile(numPhotons, filename, maxDepth):
    '''
    Generates a rayfile in ASCII format.
    '''
    pass



def getDenoiseFilter():
    '''
    Returns the denoise filter used.
    '''
    pass



def getDenoiseFilterThreshold():
    '''
    Returns the denoise filter threshold value
    '''
    pass



def getEnableDenoiseFilter():
    '''
    Deprecated, use getDenoiseFilter instead: Returns whether the CPU denoise filter for raytracing is enabled or not.
    '''
    pass



def getIlluminant():
    '''
    Returns the illuminant id used.
    '''
    pass



def getNURBSRaytracing():
    '''
    Returns whether NURBS raytracing is on or off.
    '''
    pass



def getRaytracingAAImageFilterHeight():
    '''
    Returns the height of the pixel filter in use.
    '''
    pass



def getRaytracingAAImageFilterType():
    '''
    Returns the pixel filter type in use.
    '''
    pass



def getRaytracingAAImageFilterWidth():
    '''
    Returns the width of the pixel filterin use.
    '''
    pass



def getRaytracingAAThresholdQuality():
    '''
    Returns the adaptive antialiasing quality level.
    '''
    pass



def getRaytracingClampValue():
    '''
    Returns the clamping value.
    '''
    pass



def getRaytracingClampingEnable():
    '''
    Returns whether clamping is enabled or disabled.
    '''
    pass



def getRaytracingCores():
    '''
    Returns the number of cores to be used during raytracing.
    '''
    pass



def getRaytracingFinalGatherRadius():
    '''
    Returns the final gather lookup radius.
    '''
    pass



def getRaytracingImageSamples():
    '''
    Returns the number of anti-aliasing samples.
    '''
    pass



def getRaytracingInteractiveFinalGatherQuality():
    '''
    Returns the interactive final gather quality level.
    '''
    pass



def getRaytracingInteractiveIBLQuality():
    '''
    Returns the interacitve ibl quality level in use.
    '''
    pass



def getRaytracingInteractivePhotonCount():
    '''
    Returns the interactive photon count.
    '''
    pass



def getRaytracingInteractiveQuality():
    '''
    Returns the interactive quality level in use.
    '''
    pass



def getRaytracingInteractiveQualityMode():
    '''
    Returns the interactive quality mode in use.
    '''
    pass



def getRaytracingInteractiveTextureSharpness():
    '''
    Returns the sharpness scale factor for texture sampling during interacitve mode.
    '''
    pass



def getRaytracingInteractiveTraceDepth():
    '''
    Returns the interactive trace depth in use.
    '''
    pass



def getRaytracingLightEvaluationThreshold():
    '''
    Returns the threshold used for culling lights.
    '''
    pass



def getRaytracingMode():
    '''
    Returns the raytracing mode.
    '''
    pass



def getRaytracingPhotonLookupCount():
    '''
    Returns the photon lookup count.
    '''
    pass



def getRaytracingPhotonMapFreezeMode():
    '''
    Gets the freeze mode for updating photon map.
    '''
    pass



def getRaytracingPhotonMapRefreshMode():
    '''
    Returns final gathering refresh mode.
    '''
    pass



def getRaytracingPhotonMode():
    '''
    Returns the photon mode.
    '''
    pass



def getRaytracingPhotonRadius():
    '''
    Returns the photon lookup radius.
    '''
    pass



def getRaytracingSampleOffset():
    '''
    Returns the sample offset to start the rendering.
    '''
    pass



def getRaytracingSamplesThreshold():
    '''
    Returns the samples threshold.
    '''
    pass



def getRaytracingStillFrameFinalGatherQuality():
    '''
    Returns the stillframe final gather quality level.
    '''
    pass



def getRaytracingStillFrameIBLQuality():
    '''
    Returns the stillframe ibl quality level in use.
    '''
    pass



def getRaytracingStillFramePhotonCount():
    '''
    Returns the stillframe photon count.
    '''
    pass



def getRaytracingStillFrameQuality():
    '''
    Returns the still frame reflection/refraction quality level in use.
    '''
    pass



def getRaytracingStillFrameQualityMode():
    '''
    Returns the stillframe quality mode in use.
    '''
    pass



def getRaytracingStillFrameSupersampling():
    '''
    Returns the stillframe supersampling factor.
    '''
    pass



def getRaytracingStillFrameTextureSharpness():
    '''
    Returns the sharpness scale factor for texture sampling during stillframe mode.
    '''
    pass



def getRaytracingStillFrameTraceDepth():
    '''
    Returns the stillframe trace depth in use.
    '''
    pass



def getRaytracingUseFinalGatherForGlossy():
    '''
    Returns whether the final gather map should be used for glossy reflections.
    '''
    pass



def getRaytracingUseHighQualityTextureFiltering():
    '''
    Returns whether anisotropic texture filtering is allowed or not.
    '''
    pass



def getRenderAlpha():
    '''
    Returns whether an alpha should be exported.
    '''
    pass



def getRenderAnimation():
    '''
    Returns whether animation export is turned on or off.
    '''
    pass



def getRenderAnimationClip():
    '''
    Returns the name of the clip to render.
    '''
    pass



def getRenderAnimationClips():
    '''
    Returns the names of the available clips in a scene.
    '''
    pass



def getRenderAnimationFormat():
    '''
    Returns the output format.
    '''
    pass



def getRenderAnimationType():
    '''
    Returns the type of the animation to render.
    '''
    pass



def getRenderBackgroundColor():
    '''
    Returns the background color.
    '''
    pass



def getRenderFilename():
    '''
    Returns the current image filename.
    '''
    pass



def getRenderFps():
    '''
    Returns the frames per second for rendering and animation.
    '''
    pass



def getRenderFrameStep():
    '''
    Returns the frame step for rendering and animation.
    '''
    pass



def getRenderICCProfile():
    '''
    Returns the ICC Profile Id.
    '''
    pass



def getRenderMetaDataFlags():
    '''
    Returns the meta data flags bitmask.
    '''
    pass



def getRenderOutputFilenames():
    '''
    Returns all filenames that will be created when rendering is started, i.e.
    '''
    pass



def getRenderPNGQuality():
    '''
    Returns the current quality for writing PNG files.
    '''
    pass



def getRenderPasses():
    '''
    Returns the names of the current active renderpasses.
    '''
    pass



def getRenderPixelHeight():
    '''
    Returns height of the image in pixels.
    '''
    pass



def getRenderPixelPerInch():
    '''
    Returns the number of pixels per inch.
    '''
    pass



def getRenderPixelWidth():
    '''
    Returns width of the image in pixels.
    '''
    pass



def getRenderPremultiply():
    '''
    Returns whether premultiplied alpha should be used.
    '''
    pass



def getRenderPrintHeight():
    '''
    Returns height of the image in centimeter.
    '''
    pass



def getRenderPrintWidth():
    '''
    Returns width of the image in centimeter.
    '''
    pass



def getRenderRegionEndX():
    '''
    Returns the right x-coordinate of the render region.
    '''
    pass



def getRenderRegionEndY():
    '''
    Returns the top y-coordinate of the render region.
    '''
    pass



def getRenderRegionStartX():
    '''
    Returns the left x-coordinate of the render region.
    '''
    pass



def getRenderRegionStartY():
    '''
    Returns the lower y-coordinate of the render region.
    '''
    pass



def getRenderStartFrame():
    '''
    Returns the startframe for rendering an animation.
    '''
    pass



def getRenderStopFrame():
    '''
    Returns the stop frame for rendering an animation.
    '''
    pass



def getRenderSupersampling():
    '''
    Gets the image supersampling setting.
    '''
    pass



def getRenderTimeInSeconds():
    '''
    Returns the maximum render time in seconds.
    '''
    pass



def getRenderTonemapHDR():
    '''
    Returns whether the image should be tonemapped when rendering to a HDR image format.
    '''
    pass



def getRenderUseClipRange():
    '''
    Returns whether the clip range should be used.
    '''
    pass



def getRenderVariantSetGroups():
    '''
    Returns the names of all variant set groups used in the render settings.
    '''
    pass



def getRenderVariantSets():
    '''
    Returns the names of the variant sets used in this group.
    '''
    pass



def getRenderView():
    '''
    Returns the name of the active view.
    '''
    pass



def getSpectralRaytracing():
    '''
    Returns whether spectral raytracing is on or off.
    '''
    pass



def getUseInfiniteRenderInViewport():
    '''
    Returns whether infinite rendering in renderview is on or off.
    '''
    pass



def getUseRenderPasses():
    '''
    Returns whether the render passes export is active or not.
    '''
    pass



def getUseRenderRegion():
    '''
    Returns whether the render region is active or not.
    '''
    pass



def getUseRenderTimeLimit():
    '''
    If true, the render time limit is used.
    '''
    pass



def getUseRenderVariantSets():
    '''
    Returns whether variant sets are used when rendering images.
    '''
    pass



def getUseRenderViewFromVariantSets():
    '''
    Returns whether views can be changed by selecting variant sets.
    '''
    pass



def removeRenderVariantSetGroup(groupName):
    '''
    Removes a variant set group.
    '''
    pass



def setActiveGPUMask(mask):
    '''
    Sets the bitmask for gpus to use for gpu raytracing.
    '''
    pass



def setDenoiseFilter(filterType):
    '''
    Sets the denoise filter to use for raytracing.
    '''
    pass



def setDenoiseFilterThreshold(value):
    '''
    Sets the denoise filter threshold.
    '''
    pass



def setEnableDenoiseFilter(on):
    '''
    Deprecated, use setDenoiseFilter instead: Sets the CPU denoise filter for raytracing to on or off.
    '''
    pass



def setIlluminant(illuminant):
    '''
    Sets illuminant to be used as white for spectral raytracing.
    '''
    pass



def setNURBSRaytracing(on):
    '''
    Sets NURBS raytracing on or off.
    '''
    pass



def setRaytracingAAAdaptiveSamples():
    '''
    This function is deprecated.
    '''
    pass



def setRaytracingAAImageFilter(width, id, height):
    '''
    Sets the pixel filter to use during stillframe antialiasing.
    '''
    pass



def setRaytracingAAInitialSamples():
    '''
    This function is deprecated.
    '''
    pass



def setRaytracingAAThreshold():
    '''
    This function is deprecated.
    '''
    pass



def setRaytracingAAThresholdQuality(threshold):
    '''
    Sets the adaptive antialiasing quality level.
    '''
    pass



def setRaytracingCausticPhotonRadius(radius):
    '''
    Deprecated! Used to set the caustic photon lookup radius but it is no longer used.
    '''
    pass



def setRaytracingClampValue(value):
    '''
    Sets the reflection clamping for raytracing.
    '''
    pass



def setRaytracingClampingEnable(state):
    '''
    Enables output value clamping.
    '''
    pass



def setRaytracingCores(numCores):
    '''
    Sets the number of cores to use for raytracing.
    '''
    pass



def setRaytracingDOFEnable():
    '''
    Deprecated, Depth of Field is always on on a global level.
    '''
    pass



def setRaytracingFinalGatherRadius(radius):
    '''
    Sets the final gather radius.
    '''
    pass



def setRaytracingFinalGathering(quality):
    '''
    Sets the interactive and still frame final gathering quality to use.
    '''
    pass



def setRaytracingImageSamples(samples):
    '''
    Sets the number of anti-aliasing samples.
    '''
    pass



def setRaytracingIndirectPhotonRadius(radius):
    '''
    Deprecated! Sets the indirect photon lookup radius.
    '''
    pass



def setRaytracingInteractiveFinalGatherQuality(quality):
    '''
    Sets the interactive final gathering quality to use.
    '''
    pass



def setRaytracingInteractiveIBLQuality(quality):
    '''
    Sets the interactive ibl sampling quality level for raytracing.
    '''
    pass



def setRaytracingInteractivePhotonCount(count):
    '''
    Sets the number of photons emitted during interactive rendering.
    '''
    pass



def setRaytracingInteractiveQuality(quality):
    '''
    Sets the interactive quality level for raytracing.
    '''
    pass



def setRaytracingInteractiveQualityMode(mode):
    '''
    Sets the interactive quality mode for raytracing.
    '''
    pass



def setRaytracingInteractiveTextureSharpness(sharpness):
    '''
    Sets the sharpness factor for texture sampling in interactive mode (advanced feature).
    '''
    pass



def setRaytracingInteractiveTraceDepth(depth):
    '''
    Sets the interactive trace depth for raytracing.
    '''
    pass



def setRaytracingLightEvaluationThreshold(threshold):
    '''
    Sets the threshold used for culling lights in [0.0,1.0] range.
    '''
    pass



def setRaytracingMode(mode):
    '''
    Sets raytracing mode.
    '''
    pass



def setRaytracingMotionBlurEnable():
    '''
    Deprecated, Motion Blur is always on on a global level.
    '''
    pass



def setRaytracingNURBSEpsilon(epsilon):
    '''
    Sets the self-intersection tolerance for NURBS raytracing.
    '''
    pass



def setRaytracingNURBSMaxDepthCurve(depth):
    '''
    Sets the maximum subdivision depth of the trimming curves.
    '''
    pass



def setRaytracingNURBSMaxDepthSurface(depth):
    '''
    Sets the maximum subdivision depth of the acceleration data structure for the NURBS raytracing.
    '''
    pass



def setRaytracingNURBSMinDepthCurve(depth):
    '''
    Sets the minimum subdivision depth of the trimming curves.
    '''
    pass



def setRaytracingNURBSMinDepthSurface(depth):
    '''
    Sets the minimum subdivision depth of the acceleration data structure for the NURBS raytracing.
    '''
    pass



def setRaytracingNURBSNewtonEpsilon(epsilon):
    '''
    Sets the newton iteration tolerance for NURBS raytracing.
    '''
    pass



def setRaytracingNURBSThresholdCurve(threshold):
    '''
    Sets the curvature threshold for trimming curves.
    '''
    pass



def setRaytracingNURBSThresholdSurface(threshold):
    '''
    Sets the surface curvature threshold for NURBS raytracing.
    '''
    pass



def setRaytracingNURBSUsePreclassification(enable):
    '''
    Deprecated: Enables trimming curve pre-classification.
    '''
    pass



def setRaytracingPhotonLookupCount(count):
    '''
    Sets the minimum number of photons that need to be collected during a photon lookup.
    '''
    pass



def setRaytracingPhotonMapFreezeMode(mode):
    '''
    Sets the freeze mode for updating photon map.
    '''
    pass



def setRaytracingPhotonMapRefreshMode(mode):
    '''
    Sets the final gathering refresh mode.
    '''
    pass



def setRaytracingPhotonMode(mode):
    '''
    Sets the photon mapping mode to use.
    '''
    pass



def setRaytracingPhotonRadius(radius):
    '''
    Sets the photon lookup radius.
    '''
    pass



def setRaytracingRenderRegion(xBegin, yEnd, xEnd, yBegin):
    '''
    Sets the active render region in pixel coordinates.
    '''
    pass



def setRaytracingRenderer():
    '''
    Internal function.
    '''
    pass



def setRaytracingSampleOffset(samplingOffset):
    '''
    Sets the offset for the pixel sampling id (advanced feature).
    '''
    pass



def setRaytracingSamplesThreshold(samples):
    '''
    Sets samples threshold.
    '''
    pass



def setRaytracingStillFrameFinalGatherQuality(quality):
    '''
    Sets the still frame gathering quality to use.
    '''
    pass



def setRaytracingStillFrameIBLQuality(quality):
    '''
    Sets the still frame ibl sampling quality level for raytracing.
    '''
    pass



def setRaytracingStillFramePhotonCount(count):
    '''
    Sets the number of photons emitted during still frame antialiasing.
    '''
    pass



def setRaytracingStillFrameQuality(quality):
    '''
    Sets the still frame reflection/refraction quality level for raytracing.
    '''
    pass



def setRaytracingStillFrameQualityMode(mode):
    '''
    Sets the still frame quality mode for raytracing.
    '''
    pass



def setRaytracingStillFrameSupersampling(factor):
    '''
    Enables supersampling for stillframe rendering.
    '''
    pass



def setRaytracingStillFrameTextureSharpness(sharpness):
    '''
    Sets the sharpness factor for texture sampling (advanced feature).
    '''
    pass



def setRaytracingStillFrameTraceDepth(depth):
    '''
    Sets the still frame trace depth for raytracing.
    '''
    pass



def setRaytracingUseFinalGatherForGlossy(enable):
    '''
    Turns use of final gather map for glossy reflections on or off
    '''
    pass



def setRaytracingUseHighQualityTextureFiltering(enable):
    '''
    Enables high quality anisotropic texture filtering.
    '''
    pass



def setRenderAlpha(state):
    '''
    Enables export of images with an alpha channel.
    '''
    pass



def setRenderAnimation(enable):
    '''
    Enables rendering of an animation sequence.
    '''
    pass



def setRenderAnimationClip(clipname):
    '''
    Sets the name of the clip to render.
    '''
    pass



def setRenderAnimationFormat(format):
    '''
    Sets the output format.
    '''
    pass



def setRenderAnimationType(type):
    '''
    Sets the type of the animation to render.
    '''
    pass



def setRenderBackgroundColor(b, g, r):
    '''
    Sets the background color.
    '''
    pass



def setRenderCurrentView():
    '''
    Sets the view to use the current position.
    '''
    pass



def setRenderFilename(filename):
    '''
    Sets the filename to render to.
    '''
    pass



def setRenderFps(fps):
    '''
    Sets the frames per second for rendering and animation.
    '''
    pass



def setRenderFrameStep(frame):
    '''
    Sets the frame step for rendering and animation.
    '''
    pass



def setRenderICCProfile(state):
    '''
    Sets the ICC Profile to use when writing to a file.
    '''
    pass



def setRenderMetaDataFlags(flags):
    '''
    Sets the type of meta data to be embedded in a file.
    '''
    pass



def setRenderPNGQuality(quality):
    '''
    Sets the compression level for PNG images.
    '''
    pass



def setRenderPasses(state):
    '''
    Sets the active renderpasses by passing a list of pass names.
    '''
    pass



def setRenderPixelResolution(pixelWidth, pixelHeight, pixelsPerInch):
    '''
    Sets the print resolution.
    '''
    pass



def setRenderPremultiply(state):
    '''
    Enables premultiplied alpha.
    '''
    pass



def setRenderPrintResolution(printHeight, printWidth, pixelsPerInch):
    '''
    Sets the print resolution.
    '''
    pass



def setRenderRegionEndX(state):
    '''
    Sets right x-coordinate of the render region.
    '''
    pass



def setRenderRegionEndY(state):
    '''
    Sets top y-coordinate of the render region.
    '''
    pass



def setRenderRegionStartX(state):
    '''
    Sets left x-coordinate of the render region.
    '''
    pass



def setRenderRegionStartY(state):
    '''
    Sets the upper y-coordinate of the render region.
    '''
    pass



def setRenderStartFrame(frame):
    '''
    Sets the start frame for rendering and animation.
    '''
    pass



def setRenderStopFrame(frame):
    '''
    Sets the stop frame for rendering and animation.
    '''
    pass



def setRenderSupersampling(state):
    '''
    Enables antialiasing.
    '''
    pass



def setRenderTimeInSeconds(timeInSeconds):
    '''
    Sets the maximum render time in seconds.
    '''
    pass



def setRenderTonemapHDR(state):
    '''
    Enables tonemapping when rendering to a HDR image format.
    '''
    pass



def setRenderUseClipRange(enable):
    '''
    Uses the range of the chosen clip instead the start and stop frame range.
    '''
    pass



def setRenderVariantSets(groupName):
    '''
    Sets the variant sets that should be used for the group.
    '''
    pass



def setRenderView(viewName):
    '''
    Sets the view with the given name.
    '''
    pass



def setSpectralRaytracing(on):
    '''
    Sets spectral raytracing on or off.
    '''
    pass



def setUseInfiniteRenderInViewport(state):
    '''
    Enables infinite rendering in the renderview.
    '''
    pass



def setUseRaySplitting(on):
    '''
    Enables raysplitting for glass and carpaint materials.
    '''
    pass



def setUseRenderPasses(state):
    '''
    Enables export of render passes when rendering to a file.
    '''
    pass



def setUseRenderRegion(state):
    '''
    Enables region rendering.
    '''
    pass



def setUseRenderTimeLimit(state):
    '''
    Enables rendering up to the maximum render time.
    '''
    pass



def setUseRenderVariantSets(enable):
    '''
    Enables rendering of variant sets.
    '''
    pass



def setUseRenderViewFromVariantSets(enable):
    '''
    Enables using of views in variant sets, i.e.
    '''
    pass



def setUseTwoSampleImportanceSampling(on):
    '''
    Enables use of two samples for multiple importance sampling.
    '''
    pass



def startRenderToFile(alwaysOverride):
    '''
    Starts rendering to file using the current render settings.
    '''
    pass


