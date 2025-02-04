import numpy as np
import physics_engine
import pygame as pg

class Base_object():
    def __init__(self,screen,dt=None,object_type="Base",mass=None,static=False,x=None,y=None):
        self.screen = screen
        if dt is None:
            self.dt = 0
        print("base")
        self.x = screen.get_width()/2 if x is None else x
        self.y = screen.get_height()/2 if y is None else y
        self.mass = 10 if mass is None else mass
        self.object_type = object_type
        self.static = static
        self.lifespan = 0

    def draw(self):
        pass
    
    def draw_trajectory(self):
        pg.draw.line(self.screen,"red",(self.x,self.y),(self.x+self.vx*10,self.y-self.vy*10),2)      
    
    def time_elapsed(self,dt):
        self.lifespan += dt


    def add_force(self,force):
        pass
    
    def sum_forces(self):
        pass
        
    def clear_forces(self):
        self.forces = []
    
class Base_Circle(Base_object):
    def __init__(self,screen,dt=None,object_type="Base",mass=None,static=False,x=None,y=None,radius=10):
        super().__init__(screen,dt,object_type,mass,static,x,y)
        self.radius = radius

    def check_boundary(self,env,walls=None, objects=None):
        if self.x+self.radius > self.screen.get_width():
            self.vx = -self.vx
        if self.x-self.radius < 0:
            self.vx = -self.vx
        if self.y+self.radius > self.screen.get_height():
            self.vy = -self.vy
        if self.y-self.radius < 0:
            self.vy = -self.vy
        
    def check_collision(self,other,environment):
        if other.__class__.__name__=="Launchpad":
            print("launchpad")
            return self.collide_with_platform(other,environment)
        if other.__class__.__name__=="Platform":    
            
            return self.collide_with_platform(other,environment)
        if other.__class__.__name__=="Landingpad":
            return self.collide_with_platform(other,environment)
        
        #This is for the terrain collision. I 
        points = environment.points_full.T.tolist()
        if self.x-self.radius-25 < 0:
            low =0
        else:
            low =  int(self.x -self.radius -25 )
        if self.x+self.radius+25 > self.screen.get_width():
            high = self.screen.get_width()
        else:
            high = int(self.x + self.radius + 25) 
        for i in range(low,high):
            
            p1 = points[i]
            p2 = points[(i+1)%len(points)]

            if physics_engine.line_circle_collision(self.x,self.y,self.radius,p1,p2):
                self.result = "Crash"
                print("crash")
                print(range(low,high))
                print(self.x)
        
        #def check_with_platform(self,other):

    def collide_with_platform(self,other,environment):
        pass

class Base_Rectangle(Base_object):
    def __init__(self,screen,dt=None,object_type="Base",mass=None,static=False,x=None,y=None,width=10,height=10):
        super().__init__(screen,dt,object_type,mass,static,x,y)
        self.width = width
        self.height = height

    def check_boundary(self,env,walls=None, objects=None):
        if self.x+self.width > self.screen.get_width():
            self.vx = -self.vx
        if self.x-self.width < 0:
            self.vx = -self.vx

    def check_collision(self,other,environment):
        pass

    def collide_with_platform(self,other,environment):
        pass

    def trajectory_angle(self):
        if self.vx == 0:    
            return 0
        return np.arctan(self.vy/self.vx)
    
