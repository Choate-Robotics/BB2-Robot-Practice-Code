import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre
import math

class DriveTrain(SubsystemBase):
    def __init__(self):
        super().__init__()
        # Define Motors
        self.motor_L0 = ctre.TalonSRX(0)
        self.motor_L1 = ctre.VictorSPX(1)
        self.motor_L2 = ctre.VictorSPX(2)
        self.motor_R0 = ctre.TalonSRX(3)
        self.motor_R1 = ctre.VictorSPX(4)
        self.motor_R2 = ctre.VictorSPX(5)
        
        # Set Motors to follow in groups
        self.motor_L1.follow(self.motor_L0)
        self.motor_L2.follow(self.motor_L0)
        self.motor_R1.follow(self.motor_R0)
        self.motor_R2.follow(self.motor_R0)

    def tank_drive(self, speed_x, speed_y):
        # Turn right: right motors scale down adjust according amount of speed_x pressed
        p = math.sin(math.pi * speed_x - math.pi / 2)
        theta = math.atan2(speed_y, speed_x)
        
        
        # Calculate how much power we should apply Domain [0, 1]
        if math.pi/4 >= theta >= -1 *math.pi/4:
            # The x_value is going to reach 1 first
            
            if speed_x != 0:
                magnitude = math.sqrt(pow(speed_x, 2) + pow(speed_y, 2)) / math.sqrt(pow((speed_y/speed_x), 2) + 1)
            else:
                magnitude = abs(speed_y)
        else:
            # The y_value is going to reach 1 first
            
            if speed_y != 0:
                magnitude = math.sqrt(pow(speed_x, 2) + pow(speed_y, 2)) / math.sqrt(pow((speed_x/speed_y), 2) + 1)
            else:
                magnitude = abs(speed_x)
        
        
        # Clamping the absolute value of speed_y to between greater than 0.1
        if -0.1 < speed_y < 0.1:
            speed_y == 0
        
        #flip right motor, fix when y=0
        #flip everything on the left
        
        # Allows the robot to go backwards if the input on the y-axis is negative
        if speed_y < 0:
           magnitude *= -1
        
        magnitude *= 0.7
        p == (p ** (1/3) + 0.3) / 1.3
        
        if speed_x > 0.1:
            # For turning right        
            self.motor_R0.set(ctre.ControlMode.PercentOutput, magnitude * p)
            self.motor_L0.set(ctre.ControlMode.PercentOutput, magnitude)
        elif speed_x < -0.1:
            # For turning left
            self.motor_L0.set(ctre.ControlMode.PercentOutput, -magnitude * p)
            self.motor_R0.set(ctre.ControlMode.PercentOutput, -magnitude)
        else:
            # For going straight
            self.motor_R0.set(ctre.ControlMode.PercentOutput, -magnitude)
            self.motor_L0.set(ctre.ControlMode.PercentOutput, magnitude)
        

    def periodic(self):
        pass