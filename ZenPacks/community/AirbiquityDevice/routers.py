from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul

'''
args: routername,adaptername,routerMethodName, createMethodName
'''

class AirbiquityDeviceRouter(DirectRouter):
    def _getFacade(self):
    	return Zuul.getFacade('AirbiquityDeviceAdapter', self.context)
    


    def addAirbiquityTrunkRouter(self, **kwargs):
    	from Products.ZenUtils.Ext import DirectResponse
    	facade = self._getFacade()
    	ob = self.context
    	success, message = facade.addAirbiquityTrunk(ob, **kwargs)
    	if success:
    		return DirectResponse.succeed(message)
    	else:
    		return DirectResponse.fail(message)

