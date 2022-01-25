import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre

class Shooter(SubsystemBase):
    def __init__(self):
        super().__init__()

        # Define Motors
        self.motor_L = ctre.TalonFX(7)
        self.motor_R = ctre.TalonFX(8) # TODO

        self.current_speed = 0
        
        self.change_coefficient = .005

    #def roller_info(self): #Can set Speed_V if necessary
    #    trajectoryVelocity = self.motor_L.getActiveTrajectoryVelocity()
    #    outputPercent = self.motor_L.getMotorOutputPercent()
    #    outputVoltage = self.motor_L.getMotorOutputVoltage()
    #    return trajectoryVelocity, outputPercent, outputVoltage
    def limit(self, value):
        if value>1:
            return .5
        elif value<0:
            return 0
        else:
            return value
    def set_speed(self, speed:float):
        self.motor_L.set(ctre.ControlMode.PercentOutput, -speed)
        #self.motor_R.set(ctre.ControlMode.PercentOutput, speed)
        self.current_speed = speed
        #print(self.motor_L.getActiveTrajectoryVelocity())
        #print(self.motor_R.getActiveTrajectoryVelocity())
        print("Speed:", self.current_speed)
    def alter_speed(self, speed:float):
        speed = self.limit(speed+self.current_speed)
        self.set_speed(speed)
    def stop(self):
        self.set_speed(0)
    def controller_based(self, left_trigger:float, right_trigger:float):
        if left_trigger:
            self.alter_speed(-.0005)
        if right_trigger:
            self.alter_speed(.0005)

        

