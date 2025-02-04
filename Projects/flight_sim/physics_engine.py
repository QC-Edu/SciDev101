#def check_collision
import math
import numpy as np
import pygame as pg
def resulting_force(forces):

    pass

def calculate_gravity(object,environment):
    pass

def calculate_acceleration(force,mass):
    pass

def calculate_collision_force(object1,object2):
    pass

def colforce(object1,object2):
    pass



def closest_point_on_line(p1, p2, point):

    x1, y1 = p1
    x2, y2 = p2
    px, py = point
    
    # Vector from p1 to p2 (edge of the polygon)
    dx, dy = x2 - x1, y2 - y1
    # Vector from p1 to the circle's center (point)
    px1, py1 = px - x1, py - y1
    
    # Project the point (circle center) onto the line defined by the edge of the polygon
    line_len_sq = dx * dx + dy * dy
    if line_len_sq == 0:  # Prevent division by zero if the edge is a single point (p1 == p2)
        return p1
    
    # t is the projection factor (normalized between 0 and 1, where 0 is p1 and 1 is p2)
    t = max(0, min(1, (px1 * dx + py1 * dy) / line_len_sq))
    
    # Closest point on the edge segment
    closest = (x1 + t * dx, y1 + t * dy)
    return closest

def line_circle_collision(cx,cy,r,p1,p2):

    closest_point = closest_point_on_line(p1,p2,(cx,cy))
    distance = math.sqrt((closest_point[0]-cx)**2 + (closest_point[1]-cy)**2)
    return distance<=r



def draw_rect(screen,color,x,y,width,height,rotation):
    print(x,y,width,height,color,rotation)
    base_y= y+height#/2

    connect = math.sqrt((width/2)**2 + (height/2)**2)
    angle_x = math.atan((width/2)/(height/2))
    corner_angles = [angle_x,math.pi-angle_x,math.pi+angle_x,2*math.pi-angle_x]
    rotation =  math.radians(rotation)
    new_points = []
    for i in range(4):
        x_new = x + connect*math.cos(corner_angles[i]+rotation)
        y_new = y + -1*connect*math.sin(corner_angles[i]+rotation)
        new_points.append((x_new,y_new))
    y_min = max([p[1] for p in new_points])
    print(y_min,base_y)
    new_points = [(p[0],p[1]+abs((base_y-y_min))) for p in new_points]
    pg.draw.polygon(screen,color,new_points)
