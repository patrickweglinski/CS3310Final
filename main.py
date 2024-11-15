from template import pauseResume
from vpython import *

scene.background = vector(1,1,1)
scene.width = 600
scene.height = 450
scene.center = vector(0,-.4,0) 
scene.userspin = False
scene.fov = 0.01

#planet 1 variables
mass1 = 1e-8
y1 = 0
x1 = 3.3  #Halley's closest distance to the sun  
vx1 = 0 
vy1 = (2*pi*sqrt(1/x1))

#planet 2 variables
mass2 = 1e-3
y2 = 0
x2 = 5.2   
vx2 = 0 
vy2 = (2*pi*sqrt(1/x2))

planet1 = sphere(radius=.1, pos=vector(x1,0,0), color=color.red, make_trail=False, interval=10, trail_type="points")
planet2 = sphere(radius=.15, pos=vector(x2,0,0), color=color.blue, make_trail=False, interval=10,  trail_type="points")
sun = sphere(radius=.4, pos=vector(0,0,0), color=color.yellow)


print("hello")
