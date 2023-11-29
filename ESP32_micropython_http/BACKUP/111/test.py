import machine
import time

def uart_callback(uart_obj):
    # 读取串口接收缓冲区中的数据
    data = uart_obj.read(uart_obj.any())
    if data:
        # 将读取到的数据转换为字符串并打印出来
        print("Received data: " + str(data.decode()))

# 定义串口对象
uart = machine.UART(1, baudrate=115200, rx=26, tx=27)

# 配置串口中断，当接收到回车符时触发中断
uart.irq(trigger=machine.UART.RX_ANY, handler=uart_callback)

# 主循环中不断检查是否有中断发生，并打印当前时间
while True:
    print("Time: " + str(time.time()))
    time.sleep(1)