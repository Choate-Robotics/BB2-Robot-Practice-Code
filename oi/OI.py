import commands2
from oi.controller import controller
from subsystems.drivetrain import DriveTrain
from subsystems.shooter import Shooter
import command

class OI:
    def __init__(self):
        pass
    def map_commands(self): # TODO
        controller.get_left_bumper().whenPressed(command.shooter_commands.increase_speed_increment())
        controller.get_right_bumper().whenPressed(command.shooter_commands.decrease_speed_increment())