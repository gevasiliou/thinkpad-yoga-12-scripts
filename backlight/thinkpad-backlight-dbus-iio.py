# You must initialize the gobject/dbus support for threading
# before doing anything.
import gobject
import time
import os.path
import sys

gobject.threads_init()

from dbus import glib
glib.init_threads()

# Create a session bus.
import dbus
bus = dbus.SystemBus()

#create sensor object
sensor = bus.get_object('net.hadess.SensorProxy', "/net/hadess/SensorProxy")

#enable Light intensity reading
clamLight = sensor.ClaimLight(dbus_interface="net.hadess.SensorProxy")
#enable Accelerometer daa reading
ClaimAccelerometer = sensor.ClaimAccelerometer(dbus_interface="net.hadess.SensorProxy")


#while True:
light = sensor.Get("net.hadess.SensorProxy", "LightLevel", dbus_interface="org.freedesktop.DBus.Properties")
orientation = sensor.Get("net.hadess.SensorProxy", "AccelerometerOrientation", dbus_interface="org.freedesktop.DBus.Properties")

print light
print orientation

#light in Lux. From /sys/class/backlight/intel_backlight/brightness the range is 0 - 852 (unknown unit)
with open('/sys/class/backlight/intel_backlight/brightness', 'w') as bl_file:
	bl_file.write('%s\n' % int(light))

time.sleep(1)



ReleaseAccelerometer = sensor.ReleaseAccelerometer(dbus_interface="net.hadess.SensorProxy")
#Not working
#ReleaseLight = sensor.ReleaseLight(dbus_interface="net.hadess.SensorProxy")
