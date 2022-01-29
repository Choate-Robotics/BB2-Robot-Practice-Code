from robotpy_toolkit_7407.oi import XBoxController, LogitechController, JoystickAxis, DefaultButton
from commands2 import button
import wpilib

controller = LogitechController


class Controllers:
    DRIVER = 0
    OPERATOR = 1


class Keymap:
    class Drivetrain:
        ...
        #DRIVE_X_AXIS = JoystickAxis(Controllers.DRIVER, controller.L_JOY[0])
       #DRIVE_Y_AXIS = JoystickAxis(Controllers.DRIVER, controller.L_JOY[1])
       #DRIVE_ROTATION_AXIS = JoystickAxis(Controllers.DRIVER, controller.R_JOY[0])

    class Shooter:
        LB = button.JoystickButton(wpilib.Joystick(Controllers.DRIVER), 5)
        RB = button.JoystickButton(wpilib.Joystick(Controllers.DRIVER), 6)
        #LB = DefaultButton(Controllers.DRIVER, controller.LB)
        #RB = DefaultButton(Controllers.DRIVER, controller.RB)

        def LEFT_JOY():
            return wpilib.Joystick(Controllers.DRIVER).getRawAxis(1)

        def RIGHT_JOY():
            return wpilib.Joystick(Controllers.DRIVER).getRawAxis(3)

        #LEFT_JOY = JoystickAxis(Controllers.DRIVER, controller.L_JOY[1])
        #RIGHT_JOY = JoystickAxis(Controllers.DRIVER, controller.R_JOY[1])
