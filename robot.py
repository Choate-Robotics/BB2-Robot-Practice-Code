# Tasks
#   Hello World
#   Create a DriveTrain Subsystem
#   Iniatialize Motors, Control Motors
#   Take in JoyStick Input
# Create Drive Command

# Import Libraries
import wpilib
from commands2 import CommandBase, SubsystemBase, CommandScheduler
import ctre
from oi.OI import OI

# Import our Classes
from oi.controller import controller
from subsystems.drivetrain import DriveTrain
from subsystems.shooter import Shooter
import command.shooter_commands


class santaBot(wpilib.TimedRobot):
    def robotInit(self):
        # Runs once when the robot is enabled
        print("Delivering Toys")
        self.drivetrain = DriveTrain()
        self.oi = controller()
        self.shooter = Shooter()

        # OI.map_commands(self.shooter)

    def teleopInit(self) -> None:
        self.shooter.set_speed(1)
        # CommandScheduler.getInstance().schedule(command.shooter_commands.stop(self.shooter))
        pass

    def teleopPeriodic(self):
        #self.oi.GET_LEFT_BUMPER.whenPressed(lambda: print("helo"))
        # Runs every 20 ms when TeleOperated Enabled
        #self.drivetrain.tank_drive(self.oi.get_y(), self.oi.get_turn())
        self.shooter.controller_based(-self.oi.get_left_trigger(), -
                                      self.oi.get_right_trigger())
        print("Current Speed: ", self.shooter.current_speed)
        # print(self.shooter.current_speed)


if __name__ == "__main__":
    wpilib.run(santaBot)
