from Shapes.swept import Swept
from Shapes.line import Line
from Shapes.arc import Arc


# INPUT
ipe_profile = 200
rail_length = 2000  # [mm]

IPE_profile_list = {
    200: [200, 100, 5.6, 8.5],
    220: [220, 110, 5.9, 9.2]
}
ipe = IPE_profile_list.get(ipe_profile)

h = ipe[0]
b = ipe[1]
s = ipe[2]
t = ipe[3]

# Starting in bottom left corner going right. z pointing into plane, x to right and y up.
#        x, y, z, x, y, z
line1 = Line(0, 0, 0, b, 0, 0)
line2 = Line(b, 0, 0, b, t, 0)
line3 = Line(b, t, 0, (b+s)/2, t, 0)
line4 = Line((b+s)/2, t, 0, (b+s)/2, h-t, 0)
line5 = Line((b+s)/2, h-t, 0, b, h-t, 0)
line6 = Line(b, h-t, 0, b, h, 0)
line7 = Line(b, h, 0, 0, h, 0)
line8 = Line(0, h, 0, 0, h-t, 0)
line9 = Line(0, h-t, 0, (b-s)/2, h-t, 0)
line10 = Line((b-s)/2, h-t, 0, (b-s)/2, t, 0)
line11 = Line((b-s)/2, t, 0, 0, t, 0)
line12 = Line(0, t, 0, 0, 0, 0)

line = Line(0, 0, 0, 0, 0, rail_length)

#        Arc((center), (xDirection), (yDirection), radius, startAngle, endAngle)
# ToDo make it so center of arc always hits end of line
# arc_g1 = Arc(0, 0, rail_length,
#              (1, 0, 0),
#              (0, 0, 1),
#              rail_length/2, 0, 180)

swept = Swept([line, ], [line1, line2, line3, line4, line5,
              line6, line7, line8, line9, line10, line11, line12])
