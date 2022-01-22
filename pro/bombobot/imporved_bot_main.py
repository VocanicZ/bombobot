import cv2 as cv
from src.ai import *
import ctypes
import math
import numpy as  np
import winsound
from src.imgbot import ison_curscreen
from src.fl import get_img_path

key_pos = {'back':(0, 0), 'map': (0, 0), 'hero':(0, 0), 'all':(0, 0), 'close':(0, 0)}

screen = 2 #working screen for bots defult 1
scale = 9 #number of grid of your screen must be fit in NxN form
bar = 4 #bottom = 2 top = 8 left = 4 right = 6 none = 5 defult 2

screensize = 0
hight = 0
width = 0

def conv(key, scr):
        return (key_pos[key][0]+ width*scr-1, key_pos[key][1]+ hight*scr-1)

def remap(scr):
        return

def output_screen_pos():
        img = cv.cvtColor(np.array(gui.screenshot()), cv.COLOR_RGB2BGR)
        while 1:
                cv.imshow('screenshot', img)

def main():
        global width, hight, screensize
        
        screensize = int(ctypes.windll.user32.GetSystemMetrics(78)), int(ctypes.windll.user32.GetSystemMetrics(79))
        #print(screensize)
        hight = ((screensize[1]-(100 if bar == 2 or bar == 8 else 0))/math.sqrt(scale))
        width = ((screensize[0]/screen-(100 if bar == 4 or bar == 6 else 0))/math.sqrt(scale))
        pos = int(width)+(2880*(screen-1))+(100 if bar == 4 or bar == 6 else 0), int(hight)+(100 if bar == 2 or bar == 8 else 0)
        print(pos)
        moveto(pos)

def increment(data, x=0, y=0):
        data = list(data)
        data[0] += x
        data[1] += y
        return tuple(data)
        
def dof(n, data, nx=0,ny=0):
        for k in n:
                print('clicking {}',k)
                if isinstance(k, int):
                        if k == 0:
                                click()
                        elif k == 1:
                                sleep(1)
                        elif isinstance(k, str):
                                click(increment(data[k], x=nx, y=ny))
                if ison_curscreen(get_img_path('disconnect')):
                        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

def temporary_main():
        dis_x = 619
        dis_y = 360
        dis_num = 3
        data = {'back': (3099,128), 'map': (3422,318), 'hero': (3425,522), 'work': (3362,207), 'close': (3468,171)}
        script = [['close', 'back', 'map'], ['hero', 0, 'work', 1, 'close']]
        remap = 4
        cycle = 1000
        for i in range(1, cycle):
                for n in range(dis_num):
                        print('debug')
                        if n < 3:
                                x = n*dis_x
                        y = 0
                        i == 10
                        if (i*remap)%40 == 0:
                                dof(script[1], data, nx=x, ny=y)
                        dof(script[0], data, nx=x, ny=y)
                sleep(mtos(remap))

#cur_pos()   #(5760, 1620)
#output_screen_pos()

#===================================================================================================================
#-------------------------A LOT OF BUGS-----------------------------------------------------------------------------
#======================VOCANICZ PLEASE FIX==========================================================================

if __name__ == '__main__':
        temporary_main()
        #main()