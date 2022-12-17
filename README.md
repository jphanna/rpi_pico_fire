
# rpi_pico_fire
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Raspbery Pi Pico module to quickly set up a through-hole LED to flicker, simulating a candle, lantern or fire light in a diorama.

> This won't work for Neopixels at the moment. This may be something I will try to implement.

## Parameters for Fire(pin, fire_type)
| Arg | Notes |
|---- | ----- |
| pin | This can be any pin allowed by the Pico that can be set as a PWM output pin. **Please, understand the pulse-width modulaton block on the Pico.**|
| fire_type | As of right now the types are: "*candle*", "*lantern*", and standard default type. More will be added if requested.|

## Usage
1. Download fire.py
2. Upload it to your Raspberry Pi Pico.
3. Import the module into your script (i.e. main.py):

```python
from fire import Fire
```

4. Create your object. This requires:
    1. The GPIO pin you're going to use.
    2. The type of light you want. If the type is left blank, it will just default to a built in choice.

```python
my_lantern = Fire(15, "lantern")
```

5. Using a `while True:` loop, run the `flicker()` method:

```python
while True:
    my_lantern.flicker()
```
6. Run your micropython script on the Pico!


> **Always use a current limiting resistor in your LED circuit design.**

---
### Tip
If you want a larger effect, use two, or three LEDs. Each one on it's own pin and put them close together as this article by TheArduinoGuy shows:  
[Realistic Flickering Flame Effect With Arduino and LEDs](https://www.instructables.com/Realistic-Fire-Effect-with-Arduino-and-LEDs/)

This module is a re-write of, and built upon, the idea in the Arduino "Blink Without Delay" project from the Arduino IDE, and the article above.  It was created for my personal use.
