#Patrick Weglinski

from vpython import *

#scene configuration
#---------------------------------
scene.background = vector(1,1,1)
scene.width = 600
scene.height = 450
scene.center = vector(0,-.4,0) 
scene.userspin = False
scene.fov = 0.01
  

#variables for simulation operation. Physics constants, such as G and time. Also the 
#variables associated with each planet's position, velocity and mass
#---------------------------------
G = 4*(pi)**2
tolerance = .025
t = 0
running = True

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

#shapes configuration
#---------------------------------
planet1 = sphere(radius=.1, pos=vector(x1,0,0), color=color.red, make_trail=False, interval=10, trail_type="points")
planet2 = sphere(radius=.15, pos=vector(x2,0,0), color=color.blue, make_trail=False, interval=10,  trail_type="points")
sun = sphere(radius=.4, pos=vector(0,0,0), color=color.yellow)

#functions
#---------------------------------
#pause play function and button
def pauseResume():
    global running
    
    if running == True: #if sim is running pause
        running = False
        
    elif running == False: #else if sim isn't running play
        running = True
        
button(text = "Start/Stop", bind=pauseResume)
scene.append_to_caption("\n\n")

#text readouts to view values throught the simulation loop
energy = wtext(text= "\n")
timeReadout = wtext(text= "")

#energy function 
def totalE():
    
    #storing distances in variables to simplify equations
    Dx = x2 - x1
    Dy = y2 - y1 
                                                                                                                
    return .5*mass1*(vx1**2 + vy1**2) - G*mass1/sqrt(x1**2 + y1**2) + .5*mass2*(vx2**2 + vy2**2) - G*mass2/sqrt(x2**2 + y2**2) - G*mass1*mass2/sqrt(Dx**2+Dy**2)
                                                                                                            #PE due the planets gravitational pull on eachother^
#acceleration function
def accel():
    global ax1, ay1, ax2, ay2
    
    Dx = x2 - x1
    Dy = y2 - y1 
    
    #acceleration values for each respective planet
    ax1 = G*(-x1/pow((x1**2 + y1**2),1.5) + mass2*Dx/pow(Dx**2 + Dy**2, 1.5))
    ay1 = G*(-y1/pow((x1**2 + y1**2),1.5) + mass2*Dy/pow(Dx**2 + Dy**2, 1.5))
    
    ax2 = -G*(x2/pow((x2**2 + y2**2),1.5) + mass1*Dx/pow(Dx**2 + Dy**2, 1.5))
    ay2 = -G*(y2/pow((x2**2 + y2**2),1.5) + mass1*Dy/pow(Dx**2 + Dy**2, 1.5))

#Verlet Algorithm
#---------------------------------

#initial acceleration per Verlet algorithm instructions
accel()

while t <= 500:
    
    rate(300)
    
    if running:
        
        #adaptive timestep to improve performance while also reducing truncation errors as
        #the planet approaches the host star. It is dependent on the inverse value of acceleration
        #of the planet with the highest acceleration.
        dt = tolerance * 1/max(sqrt(ax1**2 + ay1**2), 
                            sqrt(ax2**2 + ay2**2))
        
        x1 += (vx1 * dt) + (ax1*.5)*(dt**2)
        y1 += (vy1 * dt) + (ay1*.5)*(dt**2)
        
        x2 += (vx2 * dt) + (ax2*.5)*(dt**2)
        y2 += (vy2 * dt) + (ay2*.5)*(dt**2)
        
        
        vx1 += (.5* ax1) * dt
        vy1 += (.5* ay1) * dt
        
        vx2 += (.5* ax2) * dt
        vy2 += (.5* ay2) * dt
        
        accel() #updating accleration and then velocity again per instructions to the verlet algorithm 
        
        vx1 += (.5* ax1) * dt
        vy1 += (.5* ay1) * dt
        
        vx2 += (.5* ax2) * dt
        vy2 += (.5* ay2) * dt
        
        t += dt
        
        # energy.text = "energy=" + round(totalE(),4) + "\n"
        # timeReadout.text = "time=" + round(t,1)
        
        planet1.pos = vector(x1, y1, 0)
        planet2.pos = vector(x2, y2, 0)
        



