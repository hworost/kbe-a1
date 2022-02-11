from Rail.rail_element import RailElement

# RailElement 
# Arc: (startAng, endAng, radius, (xc, yc, zc))
type = "arc"
startAng = 0
endAng = 90
radius = 1000
xc = 0
yc = 0
zc = 0
ipe_profile = 200

params1 = [type, startAng, endAng, radius, [xc, yc, zc], ipe_profile]

rail_elem1 = RailElement(params1)

# rail_elem1 = RailElement([[0, 0, 0], [0, 10000, 0], 200])