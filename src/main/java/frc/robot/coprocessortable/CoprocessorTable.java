package frc.robot.coprocessortable;

import edu.wpi.first.networktables.EntryListenerFlags;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableInstance;

public class CoprocessorTable {
    private NetworkTableInstance instance;
    private NetworkTable root_table;
    private NetworkTableEntry pingEntry;
    private NetworkTableEntry pingReturnEntry;
    private NetworkTableEntry counterEntry;
    private int counter = 0;

    public CoprocessorTable() {
        instance = NetworkTableInstance.create();
        instance.startClient("127.0.0.1", 5800);
        instance.setUpdateRate(0.01);

        root_table = instance.getTable("ROS");
        pingEntry = root_table.getEntry("ping");
        pingReturnEntry = root_table.getEntry("ping_return");
        counterEntry = root_table.getEntry("counter");

        pingEntry.addListener((notification) -> {
            pingReturnEntry.setDouble(notification.getEntry().getDouble(0.0));
        }, EntryListenerFlags.kNew | EntryListenerFlags.kUpdate);
    }

    public void update() {
        counterEntry.setNumber(counter);
        counter++;
    }
}
