import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre
from oi.keymap import Keymap
from toolkit import conversions


class Shooter(SubsystemBase):
    def __init__(self):
        super().__init__()
        """[Shooter class. Contains Left/Right Motors, speed values, gear ratio info, and increment info. Also contains methods for changing speed, increment, and stopping the motors.]
        """        

        # Define Motors
        self.motor_L = ctre.TalonFX(4)
        self.motor_R = ctre.TalonFX(8)  # TODO

        self.current_speed = 0
        self.max_speed = 1

        self.increment = 0.005
        self.gearRatio = 1/1

        self.current_left_speed = 0
        self.current_right_speed = 0

    def limit(self, value):
        """Limits values to between -1*max_speed and max_speed values.

        Args:
            value (float): Speed value to be limited.

        Returns:
            float: Limited speed value.
        """        
        if value > self.max_speed:
            return self.max_speed
        elif value < 0:
            return 0
        else:
            return value

    def set_speed(self, speed: float):
        """Sets the speed of BOTH shooter motors.

        Args:
            speed (float): Speed value to be set.
        """        
        self.motor_L.set(ctre.ControlMode.PercentOutput, -speed)
        self.motor_R.set(ctre.ControlMode.PercentOutput, speed)
        self.current_left_speed = speed
        self.current_right_speed = speed

    def alter_left_speed(self, speed: float):
        """Alters the speed of the left shooter motor.

        Args:
            speed (float): Speed value to alter by.
        """        
        self.current_left_speed+=speed
        self.motor_L.set(ctre.ControlMode.PercentOutput, -self.current_left_speed)

    def alter_right_speed(self, speed: float):
        """Alters the speed of the right shooter motor.

        Args:
            speed (float): Speed value to alter by.
        """        
        self.current_right_speed+=speed
        self.motor_R.set(ctre.ControlMode.PercentOutput, self.current_left_speed)

    def alter_speed(self, speed: float):
        """Alters the speed of BOTH shooter motors.

        Args:
            speed (float): Speed value to alter by.
        """
        self.alter_left_speed(speed)
        self.alter_right_speed(speed)
        
    def alter_increment(self, to_increment: float):
        """Alters increment value of controller_based shooter control.

        Args:
            to_increment (float): Amount to change increment by.
        """        
        self.increment += to_increment
        print(f"Altered Increment. New Increment: {self.increment}")

    def stop(self):
        """Stops the shooter motors.
        """        
        print("Stopped")
        self.set_speed(0)

    def controller_based(self, left_trigger: float, right_trigger: float):
        """Controller joystick based shooter control. Left and right triggers control the shooter speed values. Also displays many debugging values.

        Args:
            left_trigger (float): Value of the left triggers press level.
            right_trigger (float): Value of the right triggers press level.
        """        
        print(
            f"Current Left Speed: {self.current_left_speed} Current Right Speed: {self.current_right_speed}||| Current Increment: {self.increment} ||| LT: {left_trigger>.1} RT: {right_trigger>.1} ||| LB: {Keymap.Shooter.LB} RB: {Keymap.Shooter.RB}||| LEFTRPM: {conversions.SENStoRPM(self.gearRatio, self.motor_L.getSelectedSensorVelocity())} RIGHTRPM: {conversions.SENStoRPM(self.gearRatio, self.motor_R.getSelectedSensorVelocity())}"
        )
        if left_trigger > 0.1 or left_trigger < -0.1:
            self.alter_speed(-self.increment)
        if right_trigger > 0.1 or left_trigger < -0.1:
            self.alter_speed(self.increment)
