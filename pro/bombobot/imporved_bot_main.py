from src.ai import *
import ctypes
import math

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
        
def main():
        global width, hight, screensize
        
        screensize = int(ctypes.windll.user32.GetSystemMetrics(78)), int(ctypes.windll.user32.GetSystemMetrics(79))
        #print(screensize)
        hight = ((screensize[1]-(100 if bar == 2 or bar == 8 else 0))/math.sqrt(scale))
        width = ((screensize[0]/screen-(100 if bar == 4 or bar == 6 else 0))/math.sqrt(scale))
        pos = int(width)+(2880*(screen-1))+(100 if bar == 4 or bar == 6 else 0), int(hight)+(100 if bar == 2 or bar == 8 else 0)
        print(pos)
        moveto(pos)
#cur_pos()   #(5760, 1620)
if __name__ == '__main__':
        main()