import mss
from PIL import Image
import cv2 as cv
import numpy as np
import pyautogui as gui
from src.ai import *
from src.fl import *

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
