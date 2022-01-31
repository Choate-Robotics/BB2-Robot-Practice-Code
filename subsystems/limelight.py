from math import degrees, pi
from networktables import NetworkTables
import math

class Limelight():
    
    
    '''
    tx = table.getNumber('tx',None)  # horizontal angle away from center (-27 to 27 degrees)
    ty = table.getNumber('ty',None)  # vertical angle away from the center (-20.5 to 20.5 degrees)
    ta = table.getNumber('ta',None)  # Area in percentage of image of the reflective surface that the limelight detects (pixels?)
    ts = table.getNumber('ts',None)  # skew or rotation of the reflective surface from (-90 to 0 degrees)
    '''
    
    def __init__(self):
        NetworkTables.initialize()
        self.table = NetworkTables.getTable("limelight")
        
    def calculate_distance(self):
        # values for calculation
        cam_height = 1  # units inches (height from ground to camera)
        cam_angle = pi/4  # units radians (angle from horizontal)
        h_hub_height = 104  # units inches (where is the upper hub from ground) 8 feet 8 inches
        ty=self.table.getNumber('ty',None)
        if ty is None:
            return -1
        
        h_hub_angle = math.radians(self.table.getNumber('ty',None))  # convert to radians
        
        distance =  (h_hub_height - cam_height) / math.tan(cam_angle + h_hub_angle)
        return distance
    

