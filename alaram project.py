import os
import datetime
from playsound import playsound
#from appkit import NSSound
os.system('clear')
alaramH=int(input('what hour do you want the alaram to ring: '))
alaramm=int(input('what minutes do you want the alaram to ring: '))
ampm=input('enter am or pm: ')
os.system('clear')
print('wating for alaram',alaramH,alaramm,ampm)
if ampm=='pm':
    alaramH=alaramH + 12
while(1==1):
    if (alaramH==datetime.datetime.now().hour and
        alaramm==datetime.datetime.now().minute):
        print('time to wake up')
        playsound('')
        break
    
