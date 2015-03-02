from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.AirbiquityDevice.Definition import *

class AirbiquityTrunkMap(SnmpPlugin):
    
    compname = "os"
    constr = Construct(AirbiquityDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpGetTableMaps = (
        GetTableMap('trunkStateTable', '.1.3.6.1.4.1.7735.2.2.4.1', {
            '.1': 'snmpindex',
            '.2': 'busyOutState',
            }),
        )

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        log.debug("%s tabledata = %s", device.id, tabledata)
        maps = []
        rm = self.relMap()
        trunktable = tabledata.get("trunkStateTable")
        for trunk in trunktable.values():
            om = self.objectMap(trunk)
            name = "%s_%s" % (self.baseid,str(om.snmpindex))
            om.id = self.prepId(name)
            om.title = name
            om.trunkID = om.snmpindex
            rm.append(om)
        maps.append(rm)
        return maps

