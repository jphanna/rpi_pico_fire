from fire import Fire

my_fireplace = Fire(16, "fireplace")

try:
    while True:
        my_fireplace.flicker()

except KeyboardInterrupt:
    my_fireplace.cleanup()
