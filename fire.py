import machine
import utime
import urandom

class Fire(object):
    def __init__(self, pin, fire_type="standard"):
        self.led = machine.PWM(machine.Pin(pin))
        self.led.freq(980) # 490 or 980
        self.fire_type = fire_type
        self.flicker_speed = self.get_flicker_speed()
        self.brightness = self.get_brightness()
        self.current_millis = 0
        self.previous_millis = 0
        
        
    def get_flicker_speed(self):
        return urandom.randrange(100) # 100
    
    
    def get_brightness(self):
        if self.fire_type == "lantern":
            return urandom.randrange(25000, 65535)
        elif self.fire_type == "candle":
            return urandom.randrange(2000, 8000)
        else:
            return urandom.randrange(34695, 65535)
        
        
    def Flicker(self):
        self.current_millis = utime.ticks_ms()
        if self.current_millis - self.previous_millis >= self.flicker_speed:
            self.previous_millis = self.current_millis
            self.led.duty_u16(self.brightness)
            self.flicker_speed = self.get_flicker_speed()
            self.brightness = self.get_brightness()
            
            
