import pygame as pg
import math
import numpy as np
from core.base_object import Base_object
from core.static import *

class Environment():

    def __init__(self,screen,gravity=9.8,wind=0,objects=[],projectiles = [],start=None,end=None):
        self.gravity = gravity
        self.screen = screen
        #self.screen = screen
        self.objects = objects
        self.start = start
        self.projectiles = projectiles
        self.end = end
        self.all = objects + [start,end]+projectiles
        self.points_first,self.points_mid, self.points_last=self.generate_terrain(screen,300)
        self.points_full = np.concatenate((self.points_first,self.points_mid,self.points_last),axis=1)
        self.draw_terrain(screen)

        self.set_end(self.points_last)

    def set_end(self,points):

        init = Landingpad(self.screen,x=None,y=None)
        

        x,y = points
        
        if abs(x[-1]-x[0]) < init.width:
            raise ValueError("The landing pad is too wide for the terrain")
        
        width = init.width
        height = init.height
       # high = max()
        low = min(x[0]+0.5*width, x[-1]-0.5*width)
        #print(low,high)
        x = np.random.randint(x[0], x[-1]-width,1)
        y = y[0]-height

        init.x = x[0]
        init.y = y
        print(init.__dict__)
        self.end = init

    def place_objects(self,object):

        init = object(self.screen)

        x,y = self.points_mid

        if abs(x[-1]-x[0]) < init.width:
            raise ValueError("The object is too wide for the terrain")
        
        width = init.width
        height = init.height

        x_coord = np.random.randint(len(x)/2, x[-1]-width-20,1)

        #y_indx = np.random.randint(x[0],x[-1])
        y_indx = x_coord[0]
        init.x = x_coord[0]
        init.y = self.points_full[1][y_indx]-height
        if init.static:
            print(init.static)
            self.objects.append(init)
        else:
            print(init.static)
            self.projectiles.append(init)

    def draw_terrain(self,screen):

        points = self.points_full.T.tolist()
        points.append([self.screen.get_width(),points[-1][1]])
        points.append([self.screen.get_width(),self.screen.get_height()])
        points.append([0,self.screen.get_height()])
        for ii in range(len(points)-1):
            pg.draw.polygon(screen,(95, 72, 59),points)
        
    def draw_objects(self):
        for obj in self.objects:
            obj.draw()
            
        self.start.draw()
        self.end.draw()

    def erase_objects(self):
        pg.draw.polygon(self.screen,"black",self.points_full.T.tolist())
        
        
    def generate_terrain(self,screen,max_height,segments=10):
        x_coord = list(range(0,screen.get_width()))
        #gives the number of points in each segment
        initial_segment = self.start.x + self.start.width

        seg = (screen.get_width()-initial_segment)/(segments-1) 
        y_coord = np.repeat(np.array([self.start.y + self.start.height]),initial_segment)
        first_y = y_coord.copy()
        for ii in range(1,segments):
            y_init = np.random.randint(screen.get_height()-max_height,screen.get_height(),1)
            y_coord=np.append(y_coord,np.repeat(y_init,seg))

        if y_coord.shape[0] < screen.get_width():
            leftover = screen.get_width() - y_coord.shape[0]
            y_coord = np.append(y_coord,np.repeat(y_init,leftover))
            
        last_y = np.repeat(y_init,seg)
        last_x = x_coord[len(x_coord)-last_y.shape[0]::]

        first_x = x_coord[0:int(initial_segment)]
        #points,last_points = np.array([x_coord,y_coord]),np.array([last_x,last_y])
        
        first_points = np.array([first_x,first_y])
        mid_points = np.array([x_coord[0+int(initial_segment):len(x_coord)-last_y.shape[0]],y_coord[0+int(initial_segment):len(x_coord)-last_y.shape[0]]])
        last_points = np.array([last_x,last_y])
        
        return first_points,mid_points, last_points

