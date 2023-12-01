from machine import Pin

fan_status = 'Ventilador Apagado'

def update_web_page_status(status):
    global fan_status
    fan_status = status

def generate_html(temperature):
    html = """<html>
<head>
   <meta http-equiv="refresh" content="10">
  <title>MicroPython DS18B20 ESP Web Server</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <link rel="icon" href="data:,">
  <style>
    html {font-family: Arial; display: inline-block; text-align: center;}
    p { font-size: 1.2rem;}
    body {  margin: 0;}
    .top_nav { overflow: hidden; background-color: #da0a0a; color: white; font-size: 1rem; }
    .content { padding: 30px; }
    .card { background-color: white; box-shadow: 2px 2px 12px 1px rgba(140,140,140,.5); }
    .cards { max-width: 800px; margin: 0 auto; display: grid; grid-gap: 2rem; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
    .value { font-size: 3rem; }
    .symbol { font-size: 2rem; }
  </style>
</head>
<body>
  <div class="top_nav">
    <h1>DS18B20 Web Server</h1>
  </div>
  <div class="content">
    <div class="cards">
      <div class="card">
        <p><i class="fas fa-thermometer-half fa-3x" style="color:#da0a0a;"></i><span class="symbol">Temperature</span></p><p><span class="value"><span id="temp">""" + str(temperature) + """</span> &deg;C</span></p>
      </div>
      <div class="card">
        <p><i class="fas  fa-thermometer-half fa-3x" style="color:#da0a0a;"></i> <span class="symbol">Temperature</span></p><p><span class="value"><span id="hum">""" + str(round(temperature * (9/5) + 32.0, 2)) + """</span> &deg;F</span></p>
      </div>
    </div>
  </div>
</body>
</html>"""
    return html


