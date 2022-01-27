import wpilib
from commands2 import CommandBase, SubsystemBase, _impl
from robotpy_toolkit_7407.oi import XBoxController, LogitechController, JoystickAxis, DefaultButton

c = LogitechController


class controller():
    def __init__(self):
        self.driver_controller = wpilib.Joystick(0)
    def get_y(self): ...
        # Get y-axis Value
        #return -self.driver_controller.getRawAxis(1) # Multiply by negative 1 so "UP" is Positive
    def get_turn(self): ...
        # Get right joystick x-axis value (Speed)
        #return self.driver_controller.getRawAxis(4)
    def get_left_trigger(self):
        return self.driver_controller.getRawAxis(1)
    def get_right_trigger(self):
        return self.driver_controller.getRawAxis(3)
    
    GET_LEFT_BUMPER = DefaultButton(0, 5)
        #return _impl.button.Button.JoystickButton(self.driver_controller, 5) # TODO
    #def get_right_bumper(self):
    #    return _impl.button.Button.JoystickButton(self.driver_controller, 6) # TODO