'''
vrImageService
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Service for     vrdImage related functions.
'''

from typing import List


class vrdImage():
    pass


class string():
    pass


def createImage() -> vrdImage:
    '''
    Creates an empty image.
    '''
    return None


def loadImage(filename: string) -> vrdImage:
    '''
    Loads an image.
    '''
    return None


def readImageInformation(filename: string) -> string:
    '''
    Reads an image information.
    '''
    return None


def saveImage(image: vrdImage, filename: string) -> bool:
    '''
    Saves an image.
    '''
    return None


def saveImageSequence(image: vrdImage, directory: string) -> bool:
    '''
    Saves an image sequence.
    '''
    return None

