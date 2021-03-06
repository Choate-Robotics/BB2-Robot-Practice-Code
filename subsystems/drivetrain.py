import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre

class DriveTrain(SubsystemBase):
    def __init__(self):
        super().__init__()
        # Define Motors
        self.motor_L0 = ctre.TalonSRX(0)
        self.motor_L1 = ctre.VictorSPX(1)
        self.motor_L2 = ctre.VictorSPX(2)
        self.motor_R0 = ctre.TalonSRX(3)
        self.motor_R1 = ctre.VictorSPX(4)
        self.motor_R2 = ctre.VictorSPX(5)
        
        # Set Motors to follow in groups
        self.motor_L1.follow(self.motor_L0)
        self.motor_L2.follow(self.motor_L0)
        self.motor_R1.follow(self.motor_R0)
        self.motor_R2.follow(self.motor_R0)

    def tank_drive(self, speed_y, speed_x):
        self.motor_L0.set(ctre.ControlMode.PercentOutput, speed_y+speed_x)
        self.motor_R0.set(ctre.ControlMode.PercentOutput, -speed_y+speed_x)
        

    def periodic(self):
        pass