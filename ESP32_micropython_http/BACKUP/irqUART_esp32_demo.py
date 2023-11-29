'''
    irqUART demo for esp32

    Author: shaoziyang
    Date:   2020.6

    http://www.micropython.org.cn
'''
from machine import Pin, UART
import machine
from irqUART import irqUART
import time

led = machine.Pin(2, machine.Pin.OUT)
strmsg = ''
# ESP32
u1=UART(2, 115200)


cnt = 0
def U1_RX_IRQ(t):
    global u1
    print(u1.any())
    



def U1_RX_FRAME_IRQ(t):
    global cnt
    global strmsg
    print('FRAME end')
    
ui = irqUART(u1, Pin(16), U1_RX_IRQ, U1_RX_FRAME_IRQ)
ui.uart.init(115200)


while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)