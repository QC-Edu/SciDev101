import pygame as pg
import math
import numpy as np
from core.base_object import *


    
class Platform(Base_Rectangle):

    def __init__(self,screen,object_type ="platform",mass=math.inf,width=100,height=10, static=True):
        super().__init__(screen,object_type=object_type,mass=mass,static=static,width=width,height=height)
        
        self.width = width
        self.height = height
        self.vx = 0
        self.vy = 0
        self.mass = mass
    
    def draw(self):
        pg.draw.rect(self.screen,"blue",(self.x,self.y,self.width,self.height))

class Launchpad(Platform):

    def __init__(self,screen, width=100,height=10):
        super().__init__(screen,object_type="launchpad")
        self.width = width
        self.height = height


        self.x = 0 + 0.5 * self.width
        self.y = screen.get_height() - 0.5*self.width
 
    def draw(self):
        pg.draw.rect(self.screen,"green",(self.x,self.y,self.width,self.height))

class Landingpad(Base_object):

    def __init__(self,screen,mass=math.inf,x=None,y=None,width=100,height=10):
        super().__init__(screen,"landingpad",mass,static=True)
        self.width = width
        self.height = height
        self.vx = 0
        self.vy = 0
        self.mass = mass
        if x and y:
            self.x = x- 2 * self.width
            self.y = y- 0.5*self.width
        else:

            self.x = screen.get_width() - 2 * self.width
            self.y = screen.get_height() - 0.5*self.width
 
    def draw(self):
        pg.draw.rect(self.screen,"red",(self.x,self.y,self.width,self.height))