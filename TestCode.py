# import fakeDomoticz as Domoticz
import fakeDomoticz
from fakeDomoticz import Device
from fakeDomoticz import Devices
from fakeDomoticz import Images

Parameters = {}
Parameters['Mode1'] = u"auto"
Parameters['Mode2'] = u"C4:7C:8D:66:15:C5,C4:7C:8D:64:40:77,C4:7C:8D:64:3F:93,C4:7C:8D:65:B1:1D,C4:7C:8D:66:C7:1D"


def runtest(plugin):

    fakeDomoticz.Start()
    fakeDomoticz.Debugging(0)

    plugin.onStart()
    plugin.onCommand(1, '', '', '')
    plugin.onHeartbeat()
    plugin.onHeartbeat()
    plugin.onStop()
