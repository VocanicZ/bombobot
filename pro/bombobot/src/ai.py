from asyncio.windows_events import NULL
from logging import NullHandler
import pyautogui as gui
import time

def sleep(s):
        #print('sleep {}s'.format(s))
        time.sleep(s)

def mtos(m):
        return m*60

def moveto(pos):
        #print('moveto {}'.format(pos))
        gui.moveTo(pos)

def cur_pos():
        while 1:
                print(get_cur())

def click(pos=NULL):
        if pos == NULL:
                #print('leftclick')
                gui.leftClick()
        else:
                moveto(pos)
                sleep(1)
                click()

def multi_click(n):
        for _ in range(n):
                click()
                sleep(1)
                
def scroll(n=1):
        #print('scrolling {}'.format(n))
        for _ in range(n):
                gui.scroll(-100)

def get_cur():
        return gui.position()