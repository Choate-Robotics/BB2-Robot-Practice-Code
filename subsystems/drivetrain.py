import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre

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

        self.max_turn_radius = 100
        self.robot_width = 2

    def sign(num):
        if num<0:
            return -1
        else:
            return 1

    def tank_drive(self, speed_y:float, speed_turn:float):
            
        if speed_turn < .1 and speed_turn > -.1:
            sL = speed_y
            sR = speed_y
        elif speed_y == 0:
            if speed_turn > .1:
                sL = speed_turn
                sR = -speed_turn
            elif speed_turn < -.1:
                sL = -speed_turn
                sR = speed_turn
        else:
            rT = (1/speed_turn) * 3
            print(rT)
            vDiff = abs((speed_y*2)/rT)
            rL = rT + .5 * self.robot_width
            rR = rT - .5 * self.robot_width
            if abs(rL) > abs(rR):
                sL = speed_y
                sR = speed_y - vDiff
            else:
                sL = speed_y - vDiff
                sR = speed_y

        self.motor_L0.set(ctre.ControlMode.PercentOutput, sL)
        self.motor_R0.set(ctre.ControlMode.PercentOutput, -sR)
        

    def periodic(self):
        pass