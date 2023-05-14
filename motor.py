import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DirRV=17 # GPIO 17 is pin 11
PwmRV=27 # GPIO 27 is pin 13
GPIO.setup(PwmRV,GPIO.OUT)
GPIO.setup(DirRV,GPIO.OUT)
rv=GPIO.PWM(PwmRV,100)

DirR=22 # pin 15
PwmR=10 # pin 19
GPIO.setup(DirR,GPIO.OUT)
GPIO.setup(PwmR,GPIO.OUT)
r=GPIO.PWM(PwmR,100)

DirL=9 # 21
PwmL=11 # 23
GPIO.setup(DirL,GPIO.OUT)
GPIO.setup(PwmL,GPIO.OUT)
l=GPIO.PWM(PwmL,100)

DirLV=5 # 29
PwmLV=6 # 31
GPIO.setup(DirLV,GPIO.OUT)
GPIO.setup(PwmLV,GPIO.OUT)
lv=GPIO.PWM(PwmLV,100)

def RV(w):
    if(w<=0):
        GPIO.output(DirRV,GPIO.HIGH)
        rv.start(abs(w))
    if(w>0):
        GPIO.output(DirRV,GPIO.LOW)
        rv.start(abs(w))

def R(x):
    if(x<=0):
        GPIO.output(DirR,GPIO.HIGH)
        r.start(abs(x))
    if(x>0):
        GPIO.output(DirR,GPIO.LOW)
        r.start(abs(x))

def LV(y):
    if(y>=0):
        GPIO.output(DirLV,GPIO.HIGH)
        lv.start(abs(y))
    if(y<0):
        GPIO.output(DirLV,GPIO.LOW)
        lv.start(abs(y))
def L(z):
    if(z<=0):
        GPIO.output(DirL,GPIO.HIGH)
        l.start(abs(z))
    if(z>0):
        GPIO.output(DirL,GPIO.LOW)
        l.start(abs(z))

speed = 100

RV(speed)
R(speed)
LV(speed)
L(speed)

time.sleep(50)

RV(0)
R(0)
LV(0)
L(0)
