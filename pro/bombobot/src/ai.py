from asyncio.windows_events import NULL
from logging import NullHandler
import pyautogui as gui
import time

def sleep(s):
	time.sleep(s)

def moveto(pos):
	gui.moveTo(pos)

def click(pos=NULL):
	if pos == NULL:
		gui.leftClick()
	else:
		moveto(pos)
		sleep(1)
		click()

def scroll(n=1):
	for _ in range(n):
		gui.scroll(-100)