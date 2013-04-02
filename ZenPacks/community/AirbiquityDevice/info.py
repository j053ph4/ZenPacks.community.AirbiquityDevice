from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.AirbiquityDevice.interfaces import *

'''
args:  zenpack,compInfo,compInterface,infoProperties
'''

class AirbiquityTrunkInfo(ComponentInfo):
    implements( IAirbiquityTrunkInfo )
    trunkID = ProxyProperty('trunkID')


