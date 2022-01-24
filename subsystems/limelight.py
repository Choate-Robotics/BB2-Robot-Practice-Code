from math import degrees, pi
from networktables import NetworkTables
import math

class Limelight():
    
    table = NetworkTables.getTable("limelight")
    tx = table.getNumber('tx',None)
    ty = table.getNumber('ty',None)
    ta = table.getNumber('ta',None)
    ts = table.getNumber('ts',None)
    
    
    def calculate_distance(self):
        # values for calculation
        cam_height = 1 # units inches
        cam_angle = pi/4 # units radians
        h_hub_height = 104 # units inches
        h_hub_angle = math.radians(self.table.getNumber('ty',None))
        
        distance =  (h_hub_height - cam_height) / math.tan(cam_angle + h_hub_angle)
        return distance
    

