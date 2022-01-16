from src.ai import *
import asyncio

pos = {'map':(4328,840), 'm_back':(3000,90), 'm_nextmap':(4572,1257), 'm_hero':(4322,1555), 'm_close_hero':(4333,299), 'm_hero_top':(4100,500), 'm_hero_bottom':(4000,1333), 'bot_bar': (3925,1100)}
cycle = 50 #minutes
max = 29 #cycle

def mtos(m):
	return m*60

def stom(s):
	return s/60

def countdown(s):
	count = 0
	while count < s:
		sleep(1)
		count+=1

def printpos():
	print(gui.position())


for j in range(max):
	print('bigcy{}'.format(j))
	for i in range(int(cycle/5)):
		print("cycle{}/{}".format(i,int(cycle/5)))
		if i+1==int(cycle/5):
			print('workall...')
			click(pos['m_hero'])
			sleep(1)
			click()
			sleep(2)
			moveto(pos['map'])
			sleep(2)
			scroll(40)
			for _ in range(15):
				click(pos['m_hero_bottom'])
			click(pos['m_close_hero'])
			click(pos['map'])
		click(pos['m_nextmap'])
		sleep(2)
		print('remap..')
		click(pos['m_back'])
		sleep(1)
		click(pos['map'])
		sleep(mtos(5))