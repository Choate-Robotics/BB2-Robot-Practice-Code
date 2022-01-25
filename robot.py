### Tasks
#   Hello World
#   Create a DriveTrain Subsystem
#   Iniatialize Motors, Control Motors
#   Take in JoyStick Input
## Create Drive Command

### Import Libraries
import wpilib
from commands2 import CommandBase, SubsystemBase, CommandScheduler
import ctre

### Import our Classes
from oi.controller import controller
from subsystems.drivetrain import DriveTrain
from subsystems.shooter import Shooter

class santaBot(wpilib.TimedRobot):
    def robotInit(self):
        # Runs once when the robot is enabled
        print("Delivering Toys")
        self.drivetrain = DriveTrain()
        self.oi = controller()
        self.shooter = Shooter()

    def teleopInit(self) -> None:
        #self.shooter.set_speed(.2)
        pass
    def teleopPeriodic(self):
        # Runs every 20 ms when TeleOperated Enabled
        #self.drivetrain.tank_drive(self.oi.get_y(), self.oi.get_turn())
        print(self.oi.get_left_trigger(), self.oi.get_right_trigger())
        self.shooter.controller_based(-self.oi.get_left_trigger(), -self.oi.get_right_trigger())
        
    

if __name__ == "__main__":
    wpilib.run(santaBot)
