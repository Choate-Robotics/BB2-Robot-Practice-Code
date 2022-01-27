import commands2
from oi.controller import controller
from subsystems.drivetrain import DriveTrain
from subsystems.shooter import Shooter
import command

class OI:
    @staticmethod
    def __init__():
        pass
    @staticmethod
    def map_commands(): # TODO
        controller.GET_LEFT_BUMPER().whenPressed(command.shooter_commands.stop())
        #controller.get_right_bumper().whenPressed(command.shooter_commands.decrease_speed_increment())