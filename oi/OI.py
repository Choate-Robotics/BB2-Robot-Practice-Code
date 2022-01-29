from robotpy_toolkit_7407.utils import logger

import command
from oi.keymap import Keymap
from robot_systems import Robot


class OI:
    @staticmethod
    def map_controls():  # TODO
        print("---Mapping controls...---")

        Keymap.Shooter.RB.whenPressed(
            command.ShooterIncrementUp(Robot.shooter, True)
        )
        Keymap.Shooter.LB.whenPressed(
            command.ShooterIncrementUp(Robot.shooter, False)
        )

        print("---Controls mapped.---")
        print("_______________________")
