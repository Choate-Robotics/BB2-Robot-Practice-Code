import wpilib


class Noelle(wpilib.TimedRobot):
    def robotInit(self):
        print("Hello World")


if __name__ == "__main__":
    wpilib.run(Noelle)
