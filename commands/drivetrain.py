import commands2
from subsystems.drivetrain import DriveTrain


class drive(commands2.CommandBase):
    def init(self):
        self.subsystem = DriveTrain()
        super().__init__(self.subsystem)
    def execute(self, speed_y: float, speed_turn: float):
        self.subsystem.tank_drive(speed_y, speed_turn)
    def isFinished(self) -> bool:
        return True

commands2.CommandScheduler.getInstance().schedule(drive.execute(1,1))