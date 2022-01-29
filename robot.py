import wpilib
import commands2
from robotpy_toolkit_7407 import Subsystem

from oi.OI import OI
from robot_systems import Robot

from oi.keymap import Keymap


class _Robot(wpilib.TimedRobot):

    def robotInit(self):

        print("Initializing robot...")

        self.oi = Keymap()

        OI.map_controls()

        print("Robot initialized.")

    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    def teleopInit(self) -> None:
        # commands2.CommandScheduler.getInstance().schedule(DriveSwerve(Robot.drivetrain))
        Robot.shooter.set_speed(.2)

    def teleopPeriodic(self) -> None:
        Robot.shooter.controller_based(-self.oi.Shooter.LEFT_JOY(),
                                       -self.oi.Shooter.RIGHT_JOY())

    def autonomousInit(self) -> None: ...

    def autonomousPeriodic(self) -> None: ...

    def disabledInit(self) -> None: ...

    def disabledPeriodic(self) -> None: ...

    def _simulationInit(self) -> None: ...

    def _simulationPeriodic(self) -> None: ...


if __name__ == "__main__":
    wpilib.run(_Robot)
