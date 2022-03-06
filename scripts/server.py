
import time
from networktables import NetworkTables

NetworkTables.startServer("coprocessorserver.ini", "127.0.0.1", 5800)
NetworkTables.setUpdateRate(1.0 / 60.0)
table = NetworkTables.getTable("ROS")

while True:
    value = time.time()
    table.getEntry("something").setValue(value)
    time.sleep(1.0 / 60.0)
