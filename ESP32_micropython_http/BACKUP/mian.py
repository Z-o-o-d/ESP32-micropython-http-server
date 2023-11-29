import network
import ujson
from urouter import uRouter,context


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
    return """<!DOCTYPE html>
<html>
  <head>
    <title>发送数据到Python程序</title>
  </head>
  <body>
    <h1>数据输入</h1>


    <!-- <form>
      <label for="Frequency1">CH1_frequency：</label>
      <input type="text" id="Frequency1"><br><br>
      <button type="button" onclick="sendData('Frequency1')">提交</button>
    </form>

    <form>
      <label for="Frequency2">CH2_frequency：</label>
      <input type="text" id="Frequency2"><br><
      >
      <button type="button" onclick="sendData('Frequency2')">提交</button>
    </form> -->


<!--     
     <br> HTML <br> 元素 在文本中生成一个换行（回车）符号。
 -->

    <form>
      <div>
        <h2>DS1104Z Status</h2>

        <p>Channel 1: <span id="channel1"></span></p>
        <p>Channel 2: <span id="channel2"></span></p>
      </div>

      <label for="Frequency1">CH1频率：</label><br>
      <input type="text" id="Frequency1"><br>
      <label for="Frequency2">CH2频率：</label><br>
      <input type="text" id="Frequency2"><br>
      
      <label for="FreqUnit">单位：</label>
      <input type="radio" id="hz" name="freqUnit" value="hz" checked>
      <label for="hz">Hz</label>
      <input type="radio" id="khz" name="freqUnit" value="khz">
      <label for="khz">kHz</label>
      <input type="radio" id="mhz" name="freqUnit" value="mhz">
      <label for="mhz">MHz</label>

      <br><br>

      <label for="Amplitude1">CH1振幅：</label><br>
      <input type="text" id="Amplitude1"><br>
      <label for="Amplitude2">CH2振幅：</label><br>
      <input type="text" id="Amplitude2">
      <br>
      <label for="AmpUnit">单位：</label>
      <input type="radio" id="mv" name="ampUnit" value="mv" checked>
      <label for="mv">mV</label>
      <input type="radio" id="v" name="ampUnit" value="v">
      <label for="v">V</label>
      
      <br><br>

      <label for="AmplitudeOFFS1">CH1偏移电压：</label><br>
      <input type="text" id="AmplitudeOFFS1"><br>
      <label for="AmplitudeOFFS2">CH2偏移电压：</label><br>
      <input type="text" id="AmplitudeOFFS2">
      <br>
      <label for="AmpOFFSUnit">单位：</label>
      <input type="radio" id="mv" name="ampOFFSUnit" value="mv" checked>
      <label for="mv">mV</label>
      <input type="radio" id="v" name="ampOFFSUnit" value="v">
      <label for="v">V</label>

      <br>
      <button type="button" onclick="sendData()">提交</button>


      
      <br>
      <h2>---TEST AREA---</h2>
<!-- 

          <form method="GET">
        <input type="text" name="text" value="{{ text }}">
        <input type="submit" value="Submit" style="background-color: red; border-radius: 50px; padding: 10px 20px; color: white;">
    </form> -->
      <h2>---TEST AREA---</h2>
      <br>






      <!-- TEST AREA -->
    </form>


    <script>
      function sendData() {
      const Frequency1 = document.getElementById("Frequency1").value;
      const Frequency2 = document.getElementById("Frequency2").value;
      const freqUnit = document.querySelector('input[name="freqUnit"]:checked').value;
      const Amplitude1 = document.getElementById("Amplitude1").value;
      const Amplitude2 = document.getElementById("Amplitude2").value;
      const ampUnit = document.querySelector('input[name="ampUnit"]:checked').value;
      const AmplitudeOFFS1 = document.getElementById("AmplitudeOFFS1").value;
      const AmplitudeOFFS2 = document.getElementById("AmplitudeOFFS2").value;
      const ampOFFSUnit = document.querySelector('input[name="ampOFFSUnit"]:checked').value;

      fetch('/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          Frequency1: Frequency1,
          Frequency2: Frequency2,
          freqUnit: freqUnit,
          Amplitude1: Amplitude1,
          Amplitude2: Amplitude2,
          ampUnit: ampUnit,
          AmplitudeOFFS1: AmplitudeOFFS1,
          AmplitudeOFFS2: AmplitudeOFFS2,
          ampOFFSUnit: ampOFFSUnit
        })
      })
      .then(response => {
        console.log('Success:', response);
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }





    function updateStatus() {
  fetch('/status')
    .then(response => response.json())
    .then(data => {
      document.getElementById('channel1').innerText = data.channel1;
      document.getElementById('channel2').innerText = data.channel2;
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
</html>"""
YIGEBIANLIANG="asdqwe"


@app.route('/status')
def get_status():
    global YIGEBIANLIANG
    status = {
        # 'timebase': DG1022Z_109_12.write("SOUR1:APPL?"),
        # 'trigger': DG1022Z_109_12.write("SOUR1:APPL?"),
        'channel1': "32131fsd",
        'channel2':YIGEBIANLIANG
        # Add more status information as needed
    }
    jsontemp=ujson.dumps(status).encode("utf-8")
    return jsontemp



app.serve_forever()