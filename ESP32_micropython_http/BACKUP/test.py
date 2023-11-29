import machine
led = machine.Pin(2, machine.Pin.OUT)
uart = machine.UART(2, 115200)

strmsg = ''

while True:
    if uart.any() > 0:
        strmsg = uart.read()
        print(strmsg)
        
        if 'on' in strmsg:
            led.on()
            uart.write('Turning ON led')
            print('Turning ON led')
        elif 'off' in strmsg:
            led.off()
            uart.write('Turning OFF led')
            print('Turning OFF led')
        else:
            uart.write('Invalid command.')
            print('Invalid command.')
