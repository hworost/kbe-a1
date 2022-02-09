# Path is given into here. This class is what chops the path into different rail elements

from Rail.rail_element import RailElement; 

class Rail:
    
    stdLenght = 4000;

    def __init__(self, path):
        for x in path:
            if len(path) == 3:
                self.type = "line"
                self.x0 = path[0][0]
                self.y0 = path[0][1]
                self.z0 = path[0][2]
                self.x1 = path[1][0]
                self.y1 = path[1][1]
                self.z1 = path[1][2]
                self.ipe_profile = path[2]
                
        self.generateRails(path)

    def generateRails(self, path):
        return RailElement(path);
        # Creates the rail elements based on path.
        # Line (x0,y0,z0), (x1,y1,z1)
        # Curve (startAng, endAng, radius, (xc, yc, zc))
        # Try first with the lines, then the arc. 

        # Split path into rail element sections
        

    #def setStandardLength(self, stdLength):
     #   self.stdLength = stdLength

    # You can make just for visualixation purposes so only use a single part, push whole path inside
    # Keep other interesting parameteres for later manufacturing .