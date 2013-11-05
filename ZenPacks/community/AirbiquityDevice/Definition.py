from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

AirbiquityDefinition = type('AirbiquityDefinition', (BasicDefinition,), {
        'version' : Version(1, 1, 0),
        'zenpackbase': "AirbiquityDevice",
        'component' : 'AirbiquityTrunk',
        'componentData' : {
                          'singular': 'Airbiquity Trunk',
                          'plural': 'Airbiquity Trunks',
                          'properties': {'trunkID': addProperty('Trunk ID','Basic',optional='false'),},
                          },
        }
)
