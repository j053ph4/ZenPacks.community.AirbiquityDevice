import os,re
import logging
log = logging.getLogger('zen.AirbiquityDeviceFacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from AirbiquityTrunk import *
from .interfaces import *

class AirbiquityDeviceFacade(ZuulFacade):
    implements(IAirbiquityDeviceFacade)
 

    def addAirbiquityTrunk(self, ob, **kwargs):
    	target = ob
    
        from Products.ZenUtils.Utils import prepId
        from ZenPacks.community.AirbiquityDevice.AirbiquityTrunk import AirbiquityTrunk
        import re
        cid = 'airbiquitytrunk' 
        for k,v in kwargs.iteritems():
            if type(v) != bool:
                cid += str(v)
        cid = re.sub('[^A-Za-z0-9]+', '_', cid)
        id = prepId(cid)
        component = AirbiquityTrunk(id)
        relation = target.os.airbiquityTrunks
        relation._setObject(component.id, component)
        component = relation._getOb(component.id)
        for k,v in kwargs.iteritems():
            setattr(component,k,v) 
        
    
    
    

    	return True, _t("Added Airbiquity Trunk for device " + target.id)

