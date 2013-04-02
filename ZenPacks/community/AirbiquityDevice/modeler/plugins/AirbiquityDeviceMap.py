"""
AirbiquityDeviceMap
Creates components based on T3 Service Status table in SNMP
"""
import re
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap

class AirbiquityDeviceMap(SnmpPlugin):

    maptype = "AirbiquityDeviceMap"

    columns = {
             '.1.3.6.1.4.1.7735.2.1.5.0' : 'totalModemsProvisioned',
             }
    snmpGetMap = GetMap(columns)

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        if not self.checkColumns(getdata, self.columns, log):
            return
        om = self.objectMap(getdata)

        return om


