import urllib.request
import base64
from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY

# Settings for the domoticz server
domoticzserver   = "127.1.1.1:8080"

# Sensor IDs
idx_temp  = "100"
idx_lux   = "101"
idx_moist = "102"
idx_bat   = "103"
idx_cond  = "104"

############

#base64string = base64.encodestring(('%s:%s' % (domoticzusername, domoticzpassword)).encode()).decode().replace('\n', '')

def domoticzrequest (url):
  request = urllib.request.Request(url)
 # request.add_header("Authorization", "Basic %s" % base64string)
  response = urllib.request.urlopen(request)
  return response.read()

poller = MiFloraPoller("AB:CD:12:34:56:78")
#print("FW: {}".format(poller.firmware_version()))
#print("Name: {}".format(poller.name()))
#print("Temperature: {}".format(poller.parameter_value("temperature")))
#print("Moisture: {}".format(poller.parameter_value(MI_MOISTURE)))
#print("Light: {}".format(poller.parameter_value(MI_LIGHT)))
#print("Conductivity: {}".format(poller.parameter_value(MI_CONDUCTIVITY)))
#print("Battery: {}".format(poller.parameter_value(MI_BATTERY)))

val_temp = "{}".format(poller.parameter_value("temperature"))
domoticzrequest("http://" + domoticzserver + "/json.htm?type=command&param=udevice&idx=" + idx_temp + "&svalue=" + val_temp)

val_lux = "{}".format(poller.parameter_value(MI_LIGHT))
domoticzrequest("http://" + domoticzserver + "/json.htm?type=command&param=udevice&idx=" + idx_lux + "&svalue=" + val_lux)

val_moist = "{}".format(poller.parameter_value(MI_MOISTURE))
domoticzrequest("http://" + domoticzserver + "/json.htm?type=command&param=udevice&idx=" + idx_moist + "&svalue=" + val_moist)

val_cond = "{}".format(poller.parameter_value(MI_CONDUCTIVITY))
domoticzrequest("http://" + domoticzserver + "/json.htm?type=command&param=udevice&idx=" + idx_cond + "&svalue=" + val_cond)

val_bat = "{}".format(poller.parameter_value(MI_BATTERY))
domoticzrequest("http://" + domoticzserver + "/json.htm?type=command&param=udevice&idx=" + idx_bat + "&svalue=" + val_bat)
