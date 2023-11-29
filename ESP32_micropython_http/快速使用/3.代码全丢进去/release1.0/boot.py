# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import machine
from machine import Pin, UART
import gc
from irqUART import irqUART
import network
import ujson
from urouter import uRouter,context


led = machine.Pin(2, machine.Pin.OUT)
strmsg = ""
channel1 = ""
channel2 = ""
listx = [1,2]
u1=UART(2, 115200)
cnt = 0

def U1_RX_IRQ(t):
    global u1
    global strmsg
    while u1.any():
        strmsg = u1.read()
        
    

def U1_RX_FRAME_IRQ(t):
    global cnt
    global strmsg
    global listx
    global channel1
    global channel2


    listx = strmsg.split()
    try:
        channel1 = listx[0]
        channel2 = listx[1]
    except:
        channel1 = "error"
        channel2 = "error"
    print('FRAME end')
    
ui = irqUART(u1, Pin(16), U1_RX_IRQ, U1_RX_FRAME_IRQ)
ui.uart.init(115200)

#start AP
ap = network.WLAN(network.AP_IF)
ap.config(essid="test", authmode=network.AUTH_WPA_WPA2_PSK, password="12345678")
ap.config(max_clients=10)
ap.active(True)         
print(ap.ifconfig())

#uRouter
app = uRouter()

@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html>
  <head>
    <title>发送数据到Python程序</title>
    <style>
      /* 添加表格边框样式 */
      table {
        border: 1px solid black;
        border-collapse: collapse;
      }
      
      td, th {
        border: 1px solid black;
        padding: 6px;
      }
    </style>
  </head>
  <body>
    <h1>数据输入</h1>
    <form>
      <div>
        <h2> </h2>

        <p>Data 1: <span id="channel1"></span></p>
        <p>Data 2: <span id="channel2"></span></p>
        <p>ESP32 Free memory: <span id="channel3"></span> 字节（Byte）</p>
        <p>ESP32 Allocated memory: <span id="channel4"></span> 字节（Byte）</p>
        <p>ESP32 Total memory: <span id="channel5"></span> 字节（Byte）</p>
      </div>
      <h1>History</h1>

      <table>
        <thead>
          <tr>
            <th>Title:</th>
            <th>Context:</th>
          </tr>
        </thead>
        <tbody id="data-body">
        </tbody>
      </table>
      <!-- TEST AREA -->
    </form>


    <script>
      const dataMap = new Map(); // 用于存储数据

      function updateStatus() {
        fetch('/status')
          .then(response => response.json())
          .then(data => {
            const channel1 = data.channel1;
            const channel2 = data.channel2;
            const channel3 = data.channel3;
            const channel4 = data.channel4;
            const channel5 = data.channel5;

            const tableBody = document.getElementById('data-body');
            let row = null;
            let cell1 = null;
            let cell2 = null;
            let cell3 = null;
            let cell4 = null;
            let cell5 = null;

            // 如果标题已经存在，则更新对应的内容
            if (dataMap.has(channel1)) {
              row = tableBody.querySelector(`tr[data-channel="${channel1}"]`);
              cell1 = row.querySelector('td:nth-child(1)');
              cell2 = row.querySelector('td:nth-child(2)');
              cell2.innerText = channel2;
            } else { // 否则添加新的标题和内容
              row = tableBody.insertRow();
              cell1 = row.insertCell();
              cell2 = row.insertCell();
              row.setAttribute('data-channel', channel1);
              cell1.innerText = channel1;
              cell2.innerText = channel2;
              dataMap.set(channel1, true);
            }

            document.getElementById('channel1').innerText = channel1;
            document.getElementById('channel2').innerText = channel2;
            document.getElementById('channel3').innerText = channel3;
            document.getElementById('channel4').innerText = channel4;
            document.getElementById('channel5').innerText = channel5;
            // Update more elements as needed
          })
          .catch(error => {
            console.error('Error:', error);
          });
      }

      // Call updateStatus() every 1 second
      setInterval(updateStatus, 1000);
    </script>
  </body>
</html>


"""


@app.route('/status')
def get_status():
    global listx
    global channel1
    global channel2
    free_mem = gc.mem_free()
    alloc_mem = gc.mem_alloc()
    total_mem = free_mem + alloc_mem
    status = {
    # 'timebase': DG1022Z_109_12.write("SOUR1:APPL?"),
    # 'trigger': DG1022Z_109_12.write("SOUR1:APPL?"),
    'channel1': channel1,
    'channel2': channel2,
    'channel3': free_mem,
    'channel4': alloc_mem,
    'channel5': total_mem
    # Add more status information as needed
    }  
    jsontemp=ujson.dumps(status).encode("utf-8")
    return jsontemp



app.serve_forever()
