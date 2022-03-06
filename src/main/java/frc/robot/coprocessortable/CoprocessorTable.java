package frc.robot.coprocessortable;

import edu.wpi.first.networktables.NetworkTableInstance;

public class CoprocessorTable {
    public CoprocessorTable() {
        NetworkTableInstance instance = NetworkTableInstance.create();
        instance.startClient("coprocessor", 5800);
        instance.setUpdateRate(1.0 / 30.0);
    }
}
