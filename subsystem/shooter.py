import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre
from oi.keymap import Keymap


class Shooter(SubsystemBase):
    def __init__(self):
        super().__init__()

        # Define Motors
        self.motor_L = ctre.TalonFX(4)
        self.motor_R = ctre.TalonFX(8)  # TODO

        self.current_speed = 0
        self.max_speed = 1

        self.increment = 0.005

    def limit(self, value):
        if value > self.max_speed:
            return self.max_speed
        elif value < 0:
            return 0
        else:
            return value

    def set_speed(self, speed: float):
        self.motor_L.set(ctre.ControlMode.PercentOutput, -speed)
        self.motor_R.set(ctre.ControlMode.PercentOutput, speed)
        self.current_speed = speed

    def alter_speed(self, speed: float):
        speed = self.limit(speed + self.current_speed)
        self.set_speed(speed)

    def alter_increment(self, to_increment: float):
        self.increment += to_increment
        print(f"Altered Increment. New Increment: {self.increment}")

    def stop(self):
        print("Stopped")
        self.set_speed(0)

    def controller_based(self, left_trigger: float, right_trigger: float):
        print(
            f"Current Speed: {self.current_speed} ||| Current Increment: {self.increment} ||| LT: {left_trigger>.1} RT: {right_trigger>.1} ||| LB: {Keymap.Shooter.LB} RB: {Keymap.Shooter.RB}||| "
        )
        if left_trigger > 0.1 or left_trigger < -0.1:
            self.alter_speed(-self.increment)
        if right_trigger > 0.1 or left_trigger < -0.1:
            self.alter_speed(self.increment)
