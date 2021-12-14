### Tasks
#   Hello World
#   Create a DriveTrain Subsystem
#   Iniatialize Motors, Control Motors
#   Take in JoyStick Input
## Create Drive Command

### Import Libraries
import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre

### Import our Classes
from oi.controller import controller
from subsystems.drivetrain import DriveTrain

class santaBot(wpilib.TimedRobot):
    def robotInit(self):
        # Runs once when the robot is enabled
        print("Delivering Toys")
        self.drivetrain = DriveTrain()
        self.oi = controller()
    def teleopPeriodic(self):
        # Runs every 20 ms when TeleOperated Enabled
        self.drivetrain.tank_drive(self.oi.get_y(), self.oi.get_turn())
    

if __name__ == "__main__":
    wpilib.run(santaBot)
