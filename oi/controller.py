import wpilib
from commands2 import CommandBase, SubsystemBase

class controller():
    def __init__(self):
        # Define Joysticks
        self.driver_controller = wpilib.Joystick(0)
    def get_y(self):
        # Get y-axis Value
        return -self.driver_controller.getRawAxis(1) # Multiply by negative 1 so "UP" is Positive
    def get_x(self):
        # Get x-axis Value
        return self.driver_controller.getRawAxis(4)