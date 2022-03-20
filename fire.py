import machine
import utime
import urandom


class Fire(object):
    def __init__(self, pin, fire_type="standard"):
        self.led = machine.PWM(machine.Pin(pin))
        self.led.freq(490)  # 490 or 980 Hz
        self.fire_type = fire_type
        self.flicker_speed = self._get_flicker_speed()
        self.brightness = self._get_brightness()
        self.current_millis = utime.ticks_ms()

    def _get_flicker_speed(self):
        return urandom.randrange(100)  # 100ms

    def _get_brightness(self):
        if self.fire_type == "lantern":
            return urandom.randrange(25000, 65535)
        elif self.fire_type == "candle":
            return urandom.randrange(2000, 8000)
        else:
            return urandom.randrange(34695, 65535)

    def flicker(self):
        if (
            utime.ticks_diff(utime.ticks_ms(), self.current_millis)
            >= self.flicker_speed
        ):
            self.led.duty_u16(self.brightness)
            self.flicker_speed = self._get_flicker_speed()
            self.brightness = self._get_brightness()
            self.current_millis = utime.ticks_ms()
