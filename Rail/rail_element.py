# RailElement.py - class file
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from Shapes.swept import Swept
from Shapes.line import Line
from Shapes.arc import Arc


# NOTES
# generate whole path and separate where are the straight and where are the curved elements?
# if straight elem length is above max-length, divide it.
# Path is pure geometry, railelement is max maxlenght and is more feasible
# Make straight lines, then if 



class RailElement:

    IPE_profile_list = {
        200: [200, 100, 5.6, 8.5],
        220: [220, 110, 5.9, 9.2]  # h, w, m_thikness, ul_thikness
    }

    def __init__(self, params):
        if(len(params) == 3):
            # Line: (x0,y0,z0), (x1,y1,z1)
            self.type = "line"
            self.x0 = params[0][0]
            self.y0 = params[0][1]
            self.z0 = params[0][2]
            self.x1 = params[1][0]
            self.y1 = params[1][1]
            self.z1 = params[1][2]
            self.ipe_profile = params[2]
            self.getPath()
            self.displayRail()

        if(len(params) == 5):
            # Arc: (startAng, endAng, radius, (xc, yc, zc))
            self.tyoe = "arc"
            self.startAng = params[0]
            self.endAng = params[1]
            self.radius = params[2]
            center = params[3]
            self.x0 = center[0]
            self.y0 = center[1]
            self.z0 = center[2]    
            self.ipe_profile = params[3]    

    def getPath(self):
        path = None
        if self.type == "line":
            self.path = Line(self.x0, self.y0, self.z0, self.x1, self.y1, self.z1)
            self.end_point = [self.x1, self.y1, self.z1]
        if self.type == "arc":
            # Arc((center), (xDirection), (yDirection), radius, startAngle, endAngle)
            self.path = Arc(-self.radius, 0, 0,
                       (1, 0, 0),
                       (0, 0, 1),
                       self.radius, self.startAng, self.endAng)
            # self.end_point = [TODO]
        return self.path

    def displayRail(self):
        Swept([self.path], self.get_cross_section_xz())

    def get_end_point(self):
        return self.end_point
         
    def get_cross_section_xz(self):
        ipe = self.IPE_profile_list.get(self.ipe_profile)

        h = ipe[0]
        b = ipe[1]
        s = ipe[2]
        t = ipe[3]
        
        # Make cross section. Move to different method?
        # Starting in bottom left corner going right. z pointing into plane, x to right and y up.
        line1 = Line(self.x0, self.z0, self.y0, self.x0 + b, self.z0, self.y0)
        line2 = Line(self.x0 + b, self.z0, self.y0, self.x0 + b, self.z0, self.y0 + t)
        line3 = Line(self.x0 + b, self.z0, self.y0 + t, self.x0 + (b+s)/2, self.z0, self.y0 + t)
        line4 = Line(self.x0 + (b+s)/2, self.z0, self.y0 + t, self.x0 + (b+s)/2, self.z0, self.y0 + h-t)
        line5 = Line(self.x0 + (b+s)/2, self.z0, self.y0 + h-t, self.x0 + b, self.z0, self.y0 + h-t)
        line6 = Line(self.x0 + b, self.z0, self.y0 + h-t, self.x0 + b, self.z0, self.y0 + h)
        line7 = Line(self.x0 + b, self.z0, self.y0 + h, self.x0 + 0, self.z0, self.y0 + h)
        line8 = Line(self.x0, self.z0, self.y0 + h, self.x0 + 0, self.z0, self.y0 + h-t)
        line9 = Line(self.x0, self.z0, self.y0 + h-t, self.x0 + (b-s)/2, self.z0, self.y0 + h-t)
        line10 = Line(self.x0 + (b-s)/2, self.z0, self.y0 + h-t, self.x0 + (b-s)/2, self.z0, self.y0 + t)
        line11 = Line(self.x0 + (b-s)/2, self.z0, self.y0 + t,self.x0, self.z0, self.y0 + t)
        line12 = Line(self.x0, self.z0, self.y0 + t, self.x0, self.z0, self.y0)

        return [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]
         

        
    # def get_cross_section_xy(self):
    #     ipe = self.IPE_profile_list.get(self.ipe_profile)

    #     h = ipe[0]
    #     b = ipe[1]
    #     s = ipe[2]
    #     t = ipe[3]

    #     # Make cross section. Move to different method?
    #     # Starting in bottom left corner going right. z pointing into plane, x to right and y up.
    #     line1 = Line(self.x0, self.y0, self.z0, self.x0 + b, self.y0, self.z0)
    #     line2 = Line(self.x0 + b, self.y0, self.z0, self.x0 + b, self.y0 + t, self.z0)
    #     line3 = Line(self.x0 + b, self.y0 + t, self.z0, self.x0 + (b+s)/2, self.y0 + t, self.z0)
    #     line4 = Line(self.x0 + (b+s)/2, self.y0 + t, self.z0, self.x0 + (b+s)/2, self.y0 + h-t, self.z0)
    #     line5 = Line(self.x0 + (b+s)/2, self.y0 + h-t, self.z0, self.x0 + b, self.y0 + h-t, self.z0)
    #     line6 = Line(self.x0 + b, self.y0 + h-t, self.z0, self.x0 + b, self.y0 + h, self.z0)
    #     line7 = Line(self.x0 + b, self.y0 + h, self.z0, self.x0 + 0, self.y0 + h, self.z0)
    #     line8 = Line(self.x0, self.y0 + h, self.z0, self.x0 + 0, self.y0 + h-t, self.z0)
    #     line9 = Line(self.x0, self.y0 + h-t, self.z0, self.x0 + (b-s)/2, self.y0 + h-t, self.z0)
    #     line10 = Line(self.x0 + (b-s)/2, self.y0 + h-t, self.z0, self.x0 + (b-s)/2, self.y0 + t, self.z0)
    #     line11 = Line(self.x0 + (b-s)/2, self.y0 + t, self.z0, self.x0, self.y0 + t, self.z0)
    #     line12 = Line(self.x0, self.y0 + t, self.z0, self.x0, self.y0, self.z0)

    #     return [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]

    # def get_cross_section_yx(self):
    #     ipe = self.IPE_profile_list.get(self.ipe_profile)

    #     b = ipe[0]
    #     h = ipe[1]
    #     t = ipe[2]
    #     s = ipe[3]

    #     # Make cross section. Move to different method?
    #     # Starting in bottom left corner going right. z pointing into plane, x to right and y up.
    #     line1 = Line(self.x0, self.y0, self.z0, self.x0 + b, self.y0, self.z0)
    #     line2 = Line(self.x0 + b, self.y0, self.z0, self.x0 + b, self.y0 + t, self.z0)
    #     line3 = Line(self.x0 + b, self.y0 + t, self.z0, self.x0 + (b+s)/2, self.y0 + t, self.z0)
    #     line4 = Line(self.x0 + (b+s)/2, self.y0 + t, self.z0, self.x0 + (b+s)/2, self.y0 + h-t, self.z0)
    #     line5 = Line(self.x0 + (b+s)/2, self.y0 + h-t, self.z0, self.x0 + b, self.y0 + h-t, self.z0)
    #     line6 = Line(self.x0 + b, self.y0 + h-t, self.z0, self.x0 + b, self.y0 + h, self.z0)
    #     line7 = Line(self.x0 + b, self.y0 + h, self.z0, self.x0 + 0, self.y0 + h, self.z0)
    #     line8 = Line(self.x0, self.y0 + h, self.z0, self.x0 + 0, self.y0 + h-t, self.z0)
    #     line9 = Line(self.x0, self.y0 + h-t, self.z0, self.x0 + (b-s)/2, self.y0 + h-t, self.z0)
    #     line10 = Line(self.x0 + (b-s)/2, self.y0 + h-t, self.z0, self.x0 + (b-s)/2, self.y0 + t, self.z0)
    #     line11 = Line(self.x0 + (b-s)/2, self.y0 + t, self.z0, self.x0, self.y0 + t, self.z0)
    #     line12 = Line(self.x0, self.y0 + t, self.z0, self.x0, self.y0, self.z0)

    #     return [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]