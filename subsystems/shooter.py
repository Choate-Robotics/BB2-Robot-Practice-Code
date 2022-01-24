import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre

class Shooter(SubsystemBase):
    def __init__(self):
        super().__init__()

        # Define Motors
        self.motor_L = ctre.TalonSRX(6) # TODO
        self.motor_R = ctre.TalonSRX(7) # TODO
        
        # Set Motors to follow in groups
        self.motor_R.follow(self.motor_L)

    def roller_info(self): #Can set Speed_V if necessary
        trajectoryVelocity = self.motor_L.getActiveTrajectoryVelocity()
        outputPercent = self.motor_L.getMotorOutputPercent()
        outputVoltage = self.motor_L.getMotorOutputVoltage()
        return trajectoryVelocity, outputPercent, outputVoltage

    def set_speed(self, speed:float):
        self.motor_L.set(ctre.ControlMode.PercentOutput, speed)
    def stop(self):
        self.motor_L.set(ctre.ControlMode.PercentOutput, 0)
        

