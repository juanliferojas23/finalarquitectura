from machine import Pin

fan_pin = Pin(12, Pin.OUT)
fan_threshold_on = 31.0  
fan_threshold_off = 31.0

def control_fan(temperature):
    if temperature >= fan_threshold_on and not fan_pin.value():
        fan_on()
    elif temperature < fan_threshold_off and fan_pin.value():
        fan_off()

def fan_on():
    fan_pin.on()

def fan_off():
    fan_pin.off()


