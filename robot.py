### Tasks
#   Hello World
#   Create a DriveTrain Subsystem
#   Iniatialize Motors, Control Motors
#   Take in JoyStick Input
## Create Drive Command

import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre
from oi.controller import controller

from subsystems.drivetrain import DriveTrain


class Noelle(wpilib.TimedRobot):
    def robotInit(self):
        print("Hello World")
        self.drivetrain = DriveTrain()
        self.oi = controller()
    def teleopPeriodic(self):
        # Runs every 20 ms when TeleOperated Enabled
        self.drivetrain.tank_drive(self.oi.get_x(), self.oi.get_y(), self.oi.get_m())
    

if __name__ == "__main__":
    wpilib.run(Noelle)
