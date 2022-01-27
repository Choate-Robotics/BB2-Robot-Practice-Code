# BB2-Robot-Practice-Code

##Overview
essentially, the turning on this drive train is done by running one motor at the input velocity and running the other motor at a speed slower than the input velocity

## Drivetrain - tankdrive
the tankdrive method uses four variables:
1. speed_x: the magnitude of the x-axis input from the controller. Domain [-1, 1]
2. speed_y: the magnitude of the y-axis input from the controller. Domain [-1, 1]
3. p: a variable that scales the speed of the slower motor, which runs at p% the speed of the other motor. When p < 0, the motor it controls spins backward. Domain [-1, 1]
4. magnitude: the power acting on the motors. calculated by treating [speed_x, speed_y] as a vector and calculating its magnitude, then, the magnitude multiplied to the motor on the side of the turn to achieve the turn
