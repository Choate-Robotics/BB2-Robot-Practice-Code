from networktables import NetworkTables
import wpilib
from commands2 import CommandBase, SubsystemBase
import ctre
import math

table = NetworkTables.getTable("limelight")
tx = table.getNumber('tx',None)
ty = table.getNumber('ty',None)
ta = table.getNumber('ta',None)
ts = table.getNumber('ts',None)

class LimeLight(SubsystemBase):
    def __init__(self):
        super().__init__()