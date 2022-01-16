from src.ai import *

script = [['close', 'back', 'map'], ['hero', 'hero', 1 , 'all', 1, 'close', 1, 0]]
data = {\
        '1_back':(3230, 200), '2_back':(4630, 200), '3_back':(4630,1000),\
        '1_map':(3700,500), '2_map':(5000,500), '3_map':(5000,1200),\
        '1_hero':(3670,747), '2_hero':(5073,747), '3_hero':(5073,1555),\
        '1_all':(3590,327), '2_all':(4985,327), '3_all':(4985,1137),\
        '1_close':(3729,278), '2_close':(5120,278), '3_close':(5120,1086)
        }

def dof(sc, s):
        for i in range(1, 1+int(len(data)/5)):
                for x in sc[s]:
                        if isinstance(x, int):
                                if x == 0:click()
                                elif x < 10:sleep(x)
                        else:click(data[str(i)+'_'+x])

def main(sc):
        for i in range(1000):
                dof(sc, 0)
                if i%10 == 0:dof(sc, 1)
                else:sleep(mtos(4))
#cur_pos()
main(script)