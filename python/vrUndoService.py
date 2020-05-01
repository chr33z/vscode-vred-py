'''
vrUndoService
------------------------------------------
API version: v2 | Generation Date: 2020-05-01 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------
Service that provides access to undo / redo functionality.
'''

from typing import List


def beginBlockUndo():
    '''
    Prefix call. Temporarily blocks undo for all the commands that are created between beginBlockUndo and endBlockUndo.
    '''
    pass


def beginMultiCommand(name: str, description: str, mergeEnabled: bool):
    '''
    Prefix call. Used to wrap subsequent undo-able service calls to one grouped command.
    '''
    pass


def beginUndo():
    '''
    Prefix call. Enables undo for all commands that are added to the undo stack.
    '''
    pass


def endBlockUndo():
    '''
    Suffix call to         vrUndoService.beginBlockUndo().
    '''
    pass


def endMultiCommand():
    '''
    Suffix call to beginMultiCommand.
    '''
    pass


def endUndo():
    '''
    Suffix call to         vrUndoService.beginUndo(). Note: To temporarily block undo, you can also use beginBlockUndo, endBlockUndo.
    '''
    pass


def undoBlocked() -> bool:
    '''
    Indicates if undo is currently blocked.
    '''
    return None


def undoEnabled() -> bool:
    '''
    Indicates if undo is currently active. This means,         vrUndoService.beginUndo() has been called.
    '''
    return None

