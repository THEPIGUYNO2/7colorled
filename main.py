import time
from rpi_ws281x import PixelStrip, Color

# Define the LED strip (here we use 1 LED for simplicity)
LED_COUNT = 1  # Number of LEDs
LED_PIN = 18   # GPIO pin connected to the LED
LED_FREQ_HZ = 800000  # LED signal frequency in Hz
LED_DMA = 10   # DMA channel to use
LED_BRIGHTNESS = 255  # LED brightness (0-255)
LED_INVERT = False  # True to invert the signal (common for some setups)
LED_CHANNEL = 0  # GPIO set to PWM channel

# Create the PixelStrip object
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Define the 7 colors (in RGB format)
colors = [
    Color(255, 0, 0),  # Red
    Color(255, 165, 0),  # Orange
    Color(255, 255, 0),  # Yellow
    Color(0, 255, 0),  # Green
    Color(0, 0, 255),  # Blue
    Color(75, 0, 130),  # Indigo
    Color(238, 130, 238)  # Violet
]

# Function to cycle through colors
def cycle_colors():
    while True:
        for color in colors:
            strip.setPixelColor(0, color)  # Set color on LED
            strip.show()  # Update the LED
            time.sleep(1)  # Wait for 1 second before changing color

# Start cycling through the colors
cycle_colors()
