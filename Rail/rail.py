# Path is given into here. This class is what chops the path into different rail elements

class Rail:

    stdLenght = 4000;

    def __init__(self, path):
        self.path = path
        self.generateRails(self.path)

    def generateRails(self, path):
        # Creates the rail elements based on path.
        # Line (x0,y0,z0), (x1,y1,z1)
        # Curve (startAng, endAng, radius, (xc, yc, zc))
        # Try first with the lines, then the arc. 
        pass

    # Toy can make just for visualixation purposes so only use a single part, push whole path inside
    # Keep other interesting parameteres for later manufacturing .