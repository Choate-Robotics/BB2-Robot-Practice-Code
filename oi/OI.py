import commands2.button
import wpilib
from oi.controller import controller
from subsystems.drivetrain import DriveTrain
from subsystems.shooter import Shooter
import command.shooter_commands

class OI:
    @staticmethod
    def map_commands(shooter): # TODO
        print("commands mapped")
        commands2.button.JoystickButton(wpilib.Joystick(0), 5).whenPressed(lambda: print("helo"))
        #controller.get_right_bumper().whenPressed(command.shooter_commands.decrease_speed_increment())