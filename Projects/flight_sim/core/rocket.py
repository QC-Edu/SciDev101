import pygame as pg
from core import environment
from core.base_object import Base_Rectangle
import physics_engine
import numpy as np
import math


    
class Rocket(Base_Rectangle):
    def __init__(self,screen,launchsite,result = None,object_type = "rocket",dt=None,x=None,y=None,width=40,height=80):
        self.original_image = pg.image.load('linked_files/rocket-147466_960_720.png')
        self.original_image = pg.transform.scale(self.original_image, (50, 100))
        self.image = self.original_image.copy()
        self.image = pg.transform.rotate(self.image, 0)#self.tilt)
        image_rect = self.image.get_rect()
        
        self.result = result
        self.height = image_rect.height
        self.width = image_rect.width
        
        self.screen = screen

        self.x = launchsite.x+launchsite.width*.5-self.width*.5
        self.y = launchsite.y-self.height
        self.dt = dt



    def draw(self):
        
        image = self.original_image
        #image = self.original_image if self.vy >=0 else pg.transform.rotate(self.original_image, 180)
        image_rect = image.get_rect()
        image_rect.center = (self.x+self.width/2,self.y+self.height/2)
            
        pg.draw.rect(self.screen,"red",(self.x,self.y,self.width,self.height))
        self.screen.blit(image, image_rect)

    
    def erase(self):
        #handled elsewhere
        pass
        

    def compute_altitude(self):
        pass

    def check_collision(self,other,environment):
       pass
        

    def update(self,environment=None):
        #this will update forces and stuff 
        pass


 