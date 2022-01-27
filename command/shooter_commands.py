import commands2
from subsystems.shooter import Shooter


class increase_speed_increment(commands2.CommandBase):
    def __init__(self):
        self.subsystem = Shooter()
        self.change_increment = .0001
        super().__init__(self.subsystem)
    def initialize(self):
        self.subsystem.increment += self.change_increment
        print("INCREASED INCREMENT TO:", self.subsystem.increment)
    def isFinished(self) -> bool:
        return True

class decrease_speed_increment(commands2.CommandBase):
    def __init__(self):
        self.subsystem = Shooter()
        self.change_increment = -.0001
        super().__init__(self.subsystem)
    def initialize(self):
        self.subsystem.increment += self.change_increment
        print("DECREASED INCREMENT TO:", self.subsystem.increment)
    def isFinished(self) -> bool:
        return True