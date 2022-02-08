# RailElement.py - class file
from Shapes.swept import Swept
from Shapes.line import Line
from Shapes.arc import Arc


class RailElement:

    IPE_profile_list = {
        200: [200, 100, 5.6, 8.5],
        220: [220, 110, 5.9, 9.2]  # h, w, m_thikness, ul_thikness
    }

    def __init__(self, radius, angle, pIndex, length, x0, y0, z0, xdir, ydir):
        self.radius = radius
        self.angle = angle
        self.pIndex = pIndex
        self.length = length
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.xdir = xdir
        self.ydir = ydir
        self.displayRail()

    def displayRail(self):
        ipe = self.IPE_profile_list.get(self.pIndex)

        h = ipe[0]
        b = ipe[1]
        s = ipe[2]
        t = ipe[3]

        # Make cross section. Move to different method?
        # Starting in bottom left corner going right. z pointing into plane, x to right and y up.
        line1 = Line(self.x0, self.y0, self.z0, self.x0 + b, self.y0, self.z0)
        line2 = Line(self.x0 + b, self.y0, self.z0, self.x0 + b, self.y0 + t, self.z0)
        line3 = Line(self.x0 + b, self.y0 + t, self.z0, self.x0 + (b+s)/2, self.y0 + t, self.z0)
        line4 = Line(self.x0 + (b+s)/2, self.y0 + t, self.z0, self.x0 + (b+s)/2, self.y0 + h-t, self.z0)
        line5 = Line(self.x0 + (b+s)/2, self.y0 + h-t, self.z0, self.x0 + b, self.y0 + h-t, self.z0)
        line6 = Line(self.x0 + b, self.y0 + h-t, self.z0, self.x0 + b, self.y0 + h, self.z0)
        line7 = Line(self.x0 + b, self.y0 + h, self.z0, self.x0 + 0, self.y0 + h, self.z0)
        line8 = Line(self.x0, self.y0 + h, self.z0, self.x0 + 0, self.y0 + h-t, self.z0)
        line9 = Line(self.x0, self.y0 + h-t, self.z0, self.x0 + (b-s)/2, self.y0 + h-t, self.z0)
        line10 = Line(self.x0 + (b-s)/2, self.y0 + h-t, self.z0, self.x0 + (b-s)/2, self.y0 + t, self.z0)
        line11 = Line(self.x0 + (b-s)/2, self.y0 + t, self.z0, self.x0, self.y0 + t, self.z0)
        line12 = Line(self.x0, self.y0 + t, self.z0, self.x0, self.y0, self.z0)

        path = None
        if self.radius == 0:
            path = Line(0, 0, 0, 0, 0, self.length)
            self.end_point = [0, 0, self.length]
        else:
            # Arc((center), (xDirection), (yDirection), radius, startAngle, endAngle)
            path = Arc(-self.radius, 0, 0,
                       (1, 0, 0),
                       (0, 0, 1),
                       self.radius, 0, self.angle)
            # self.end_point = [TODO]

        swept = Swept([path], [line1, line2, line3, line4, line5,
                               line6, line7, line8, line9, line10, line11, line12])

    def get_end_point(self):
        return self.end_point
