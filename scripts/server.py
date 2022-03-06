
import time
from networktables import NetworkTables

def ping_return_callback(entry, key, value, is_new):
    print("ping: %0.4fs" % (time.time() - value))

NetworkTables.startServer("coprocessorserver.ini", "127.0.0.1", 5800)
NetworkTables.setUpdateRate(0.01)
table = NetworkTables.getTable("ROS")
ping_return_entry = table.getEntry("ping_return")
ping_entry = table.getEntry("ping")
ping_return_entry.addListener(ping_return_callback, NetworkTables.NotifyFlags.NEW | NetworkTables.NotifyFlags.UPDATE)
counter_entry = table.getEntry("counter")


timer = time.time()
while True:
    value = time.time()
    if value - timer > 1.0:
        ping_entry.setValue(value)
        timer = value
        print("counter: %s" % counter_entry.getNumber(0))
