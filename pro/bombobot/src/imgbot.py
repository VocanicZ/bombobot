import mss
from PIL import Image
import cv2 as cv
import numpy as np
import pyautogui as gui
from src.ai import *
from src.fl import *
from PIL import Image

gui.FAILSAFE = False

sct = mss.mss()
monitor = sct.monitors[1]
width = monitor["width"]
height = monitor["height"]
mon = {'top': 0, 'left':width, 'width':width, 'height':height}

def screenshot():
	return np.array(gui.screenshot())

def get_curscreen():
	sct_img = sct.grab(mon)
	img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
	img_bgr = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
	return img_bgr

def ison_curscreen(img_path):
	if gui.locateOnScreen(img_path):
		return True
	return False

def get_pos(img_path):
	if ison_curscreen(img_path):
		return gui.locateCenterOnScreen(img_path)

def get_loc(target, cur='curscreen'):
	set_img('curscreen', get_curscreen())
	cur = get_img(cur)
	target = get_img(target)
	result = cv.matchTemplate(cur, target, cv.TM_CCOEFF_NORMED)
	_, val, _, loc = cv.minMaxLoc(result)
	if val > 0.9:
		return loc
	return False

def conv_loc(loc, x=20, y=20):
	i = list(loc)
	i[0] += (2*width-x)
	i[1] += y
	return tuple(i)

def click_img(name, delay=0, cur='curscreen', x=20, y=20):
	loc = get_loc(name,cur=cur)
	if loc:
		loc = conv_loc(loc,x=x,y=y)
		click(loc)
		sleep(delay)
  
def get_not_black(img):
        img = Image.open(get_img_path(img)).convert('RGB')
        for i in range(width):
                for j in range(height):
                        #print('line {},{} -> {}'.format(i,j,img[i][j]))
                        if img.getpixel((i,j)) != (0,0,0):
                                print('FOUND! {}<{}'.format(i,j))
                                return (i+1980,j)
def moving_pos():
        tmp =  get_curscreen()
        sleep(0.01)
        cur = get_curscreen()
        set_img('diff',np.abs(tmp - cur))
        moveto(get_not_black('diff'))