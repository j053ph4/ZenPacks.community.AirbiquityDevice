from ZenPacks.community.ConstructionKit.Construct import *
from Products.ZenModel.migrate.Migrate import Version
import os

class Definition():
    """
    """
    version = Version(1, 0, 0)
    zenpackroot = "ZenPacks.community" # ZenPack Root
    zenpackbase = "AirbiquityDevice" # ZenaPack Name
    
    #dictionary of components
    component = 'AirbiquityTrunk'
    componentData = {
                  'singular': 'Airbiquity Trunk',
                  'plural': 'Airbiquity Trunks',
                  'displayed': 'id', # component field in Event Console
                  'primaryKey': 'id',
                  'properties': { 
                        # Basic settings
                        'trunkID': addProperty('Trunk ID','Basic',optional='false'),
                        },
                  }
    
    packZProperties = []
    #dictionary of datasources
    addManual = False
    createDS = False
    provided = False
    cycleTime = 300
    timeout = 60
    cmdFile = None
    datapoints = []
    cwd = os.path.dirname(os.path.realpath(__file__)) # ZenPack files directory
