'''
vrCluster
------------------------------------------
API version: v1 | Generation Date: 2020-09-13 | VRED-Py: Visual Studio Code Tools for Autodesk VRED | Autogenerated Method-Stubs

------------------------------------------

'''

from __future__ import annotations
from typing import List


def getClusterRunning():
    '''
    Return true if the Cluster is running
    '''
    pass


def hasClusterLicense():
    '''
    Return true if the Cluster has valid licenses
    '''
    pass


def loadCluster(filename):
    '''
    Loads the cluster configuration.
    '''
    pass


def loginToClusterManager(password, user, server):
    '''
    Login to cluster manager.
    '''
    pass


def logoffFromClusterManager():
    '''
    Logoff from cluster manager.
    '''
    pass


def renderOnClusterQueue(queue):
    '''
    Start rendering on cluster queue
    '''
    pass


def renderQueueOnClusterQueue(queue):
    '''
    Start rendering the queue on cluster queue
    '''
    pass


def renderSequencesOnClusterQueue(queue):
    '''
    Start rendering sequences on cluster queue
    '''
    pass


def setClusterEyeSeparation(es):
    '''
    Sets the cluster eye separation.
    '''
    pass


def setClusterNetworkSpeed():
    '''
    Used to change cluster network speed hint
    '''
    pass


def setClusterNetworkType():
    '''
    Used to change cluster network interface
    '''
    pass


def setClusterNodes(hosts):
    '''
    Sets the list of compute nodes.
    '''
    pass


def setClusterZeroParallax(zp):
    '''
    Sets the cluster zero parallax.
    '''
    pass


def startBookedRaytracingCluster(server, user, bookingId, password):
    '''
    Start the raytracing cluster.
    '''
    pass


def startCluster():
    '''
    Activates the cluster mode.
    '''
    pass


def startRaytracingCluster(hostnames):
    '''
    Start the raytracing cluster.
    '''
    pass


def stopCluster():
    '''
    Deactivates the cluster mode.
    '''
    pass



def getHPCRunning():
    '''
    DEPRECATED.
    '''
    pass


def loadHPC(filename):
    '''
    DEPRECATED.
    '''
    pass


def setClusterAdvanced():
    '''
    DEPRECATED.
    '''
    pass


def setClusterConnectionDelay():
    '''
    DEPRECATED.
    '''
    pass


def setClusterProjectionPlane():
    '''
    DEPRECATED.
    '''
    pass


def setHPCAdvanced():
    '''
    DEPRECATED.
    '''
    pass


def setHPCNetworkSpeed():
    '''
    DEPRECATED.
    '''
    pass


def setHPCNetworkType():
    '''
    DEPRECATED.
    '''
    pass


def setHPCNodes(hosts):
    '''
    DEPRECATED.
    '''
    pass


def startHPC():
    '''
    DEPRECATED.
    '''
    pass


def startHPCRaytracing(hosts):
    '''
    DEPRECATED.
    '''
    pass


def stopHPC():
    '''
    DEPRECATED.
    '''
    pass

