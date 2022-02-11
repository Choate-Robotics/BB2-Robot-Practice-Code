from robotpy_toolkit_7407.utils import logger

import command
from oi.keymap import Keymap
from robot_systems import Robot


class OI:
    @staticmethod
    def map_controls():  # TODO
        print("---Mapping controls...---")

        Keymap.Shooter.RB().whenPressed(
            command.ShooterIncrementDown(Robot.shooter, True)
        )
        Keymap.Shooter.RT().whenPressed(
            command.ShooterIncrementDown(Robot.shooter, False)
        )
        Keymap.Shooter.LB().whenPressed(
            command.ShooterIncrementUp(Robot.shooter, True)
        )
        Keymap.Shooter.LT().whenPressed(
            command.ShooterIncrementUp(Robot.shooter, False)
        )

        print("---Controls mapped.---")
        print("_______________________")
