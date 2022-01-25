import commands2
from subsystems.shooter import Shooter

"""
class increase_speed_increment(commands2.CommandBase):
    def init(self):
        self.subsystem = Shooter()
        self.change_increment = .0001
        super().__init__(self.subsystem)
    def execute(self, left_bumper, right_bumper):
        self.subsystem.increment += self.change_increment
    def isFinished(self) -> bool:
        return False
"""