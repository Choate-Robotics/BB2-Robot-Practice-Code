from robotpy_toolkit_7407.command import SubsystemCommand

from subsystem import Shooter


class ShooterIncrementUp(SubsystemCommand[Shooter]):
    def __init__(self, subsystem: Shooter, increase: bool) -> None:
        super().__init__(subsystem)
        if increase:
            self.change = .001
        else:
            self.change = -.001

    def initialize(self) -> None:
        self.subsystem.alter_increment(self.change)

    def isFinished(self) -> bool:
        return True


class ShooterStop(SubsystemCommand[Shooter]):
    def __init__(self, subsystem: Shooter) -> None:
        super().__init__(subsystem)

    def initialize(self) -> None:
        self.subsystem.stop()

    def isFinished(self) -> bool:
        return True
