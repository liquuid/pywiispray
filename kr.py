import time
import cwiid

print "Aperte 1 e 2 no controle" 
w = cwiid.Wiimote()

def nuns():
    for i in [1,2,4,8,4,2]:
        print i
	w.led= i
        time.sleep(.1)

while True:
	nuns()
