import time
import numpy as np
from networktables import NetworkTables

NetworkTables.startClient(("127.0.0.1", 5800))
NetworkTables.setUpdateRate(1.0 / 60.0)
table = NetworkTables.getTable("ROS")

timer = time.time()
buffer = []
prev_value = 0.0
while True:
    value = table.getEntry("something").getDouble(0.0)
    if value != 0.0 and prev_value != value:
        prev_value = value
        buffer.append(value)
        if len(buffer) > 20:
            buffer.pop(0)
        if time.time() - timer > 1.0:
            print(1.0 / np.mean(np.diff(buffer)))
            timer = time.time()
        
    time.sleep(1.0 / 60.0)
