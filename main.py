from machine import Pin
from time import sleep
from fan_control import control_fan, fan_on, fan_off
from ifttt_handler import send_ifttt_event
from web_server import update_web_page_status, generate_html
def read_ds_sensor():
    try:
        roms = ds_sensor.scan()
        print('Found DS devices: ', roms)
        print('Temperatures: ')
        ds_sensor.convert_temp()
        for rom in roms:
            temp = ds_sensor.read_temp(rom)
            control_fan(temp)
            if isinstance(temp, float):
                msg = round(temp, 2)
                print(temp, end=' ')
                print('Valid temperature')
                return msg    
        return b'0.0'
    except OSError as e:
        return 'Failed to read sensor.'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('Content = %s' % request)
        response = generate_html(read_ds_sensor())
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')

