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
        self.max_speed = 1

        self.increment = .0005

    def limit(self, value):
        if value>self.max_speed:
            return self.max_speed
        elif value<0:
            return 0
        else:
            return value

    def set_speed(self, speed:float):
        self.motor_L.set(ctre.ControlMode.PercentOutput, -speed)
        self.motor_R.set(ctre.ControlMode.PercentOutput, speed)
        self.current_speed = speed
        print("Current Speed:", self.current_speed)

    def alter_speed(self, speed:float):
        speed = self.limit(speed+self.current_speed)
        print("Altering:", speed)
        self.set_speed(speed)

    def stop(self):
        self.set_speed(0)

    def controller_based(self, left_trigger:float, right_trigger:float):
        if left_trigger>.1 or left_trigger<-.1:
            self.alter_speed(-self.increment)
        if right_trigger>.1 or left_trigger<-.1:
            self.alter_speed(self.increment)

        

