#due to slow pixel reading functions and low gpu/cpu  power
#WORKS ONLY WHEN ZOOMED inside chrome
#due some changes to make it work also for flying dragon obstacles
import pyautogui as pi
import time as tm
import keyboard as kb
st_posx=750
st_posyd=864
#st_posym=600

tm.sleep(30)

pi.press("space")
tm.sleep(2.4)

#pi.moveTo(st_posx,st_posym)
#pi.moveTo(st_posx,st_posyd)
i=0
aa=tm.time()
while(kb.is_pressed('q')==False and i<100000):
    a1,b1,c1=pi.pixel(st_posx,st_posyd)
    #a2,b2,c2=pi.pixel(st_posx,st_posym)
    if (a1==32 and b1==33 and c1==36) or (a1==255 and b1==255 and c1==255):
        d1=0
    else:
        d1=1
    '''if (a2==32 and b2==33 and c2==36) or (a2==255 and b2==255 and c2==255):
        d2=0
    else:
        d2=1'''
    if  d1==1:
        pi.keyDown("up")
        tm.sleep(.1)
    '''elif d1==0 and d2==0:
        pass
    else:
        tm.sleep(.2)
        pi.press("up")'''
    i+=1
bb=tm.time()
print(bb-aa)
    
        
    
