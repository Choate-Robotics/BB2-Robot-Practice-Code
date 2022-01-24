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

        # User Define Tank Drive Variables
        self.robot_width = 22/12    # Width of the Robot in Feet
        self.max_speed = 1.0     # Max Speed of the Robot
        self.wheel_diameter = 4
        
        # Self-Define Tank Drive Variables
        self.robot_turn_circumference = math.pi*self.robot_width
        self.wheel_circumference = math.pi*self.wheel_diameter

        # Motor Variables
        sensor_units_per_radian = 0 # TODO Need to calculate sensor units

    def auto_angle(self, left_angle, right_angle, speed=1):  # Input as Degrees

        # Sensor Units Version

        left_rad = left_angle*(math.pi/180)
        right_rad = right_angle*(math.pi/180)

        left_dist = (left_rad/(2*math.pi))*self.robot_turn_circumference
        right_dist = (right_rad/(2*math.pi))*self.robot_turn_circumference

        left_revolutions = left_dist/self.wheel_circumference
        right_revolutions = right_dist/self.wheel_circumference   

    def gyro_angle(self, angle:float):
        pass


    def tank_drive(self, speed_y:float, speed_turn:float):
            
        if speed_turn < .1 and speed_turn > -.1:    # If the Turn speed is between -.1 and 1, just go forward at the velocity
            sL = speed_y
            sR = speed_y
        elif speed_y < .1 and speed_y> -.1:         # If the Velocity is not active, just turn at the turn speed
            if speed_turn > .1 or speed_turn < -.1:
                sL = speed_turn
                sR = -speed_turn
        else:                                       # Actual Driving: If both Velocity and Turn Active
            rT = (1/speed_turn) * 2.5           # Calculate Turn Radius
            vDiff = abs((speed_y*2)/rT)         # Calculate Velocity Differential
            rL = rT + .5 * self.robot_width     # Calculate Left Wheel Velocity
            rR = rT - .5 * self.robot_width     # Calculate Right wheel Velocity
            if abs(rL) > abs(rR):               # Set Speeds based on vDiff and whether Left or Right radius is bigger
                sL = speed_y
                sR = speed_y - vDiff
            else:
                sL = speed_y - vDiff
                sR = speed_y

        self.motor_L0.set(ctre.ControlMode.PercentOutput, sL*self.max_speed)        # Run Wheels based on Speeds
        self.motor_R0.set(ctre.ControlMode.PercentOutput, -(sR*self.max_speed))
        

    def periodic(self):
        pass