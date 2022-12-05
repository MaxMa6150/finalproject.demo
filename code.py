# SPDX-FileCopyrightText: 2022 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
'''
# Whack-a-mole mode

import time
import board
import busio
import digitalio
from adafruit_neotrellis.neotrellis import NeoTrellis
import adafruit_trellism4
import random
import audiocore
import audiopwmio
import digitalio

# create the i2c object for the trellis
i2c_bus = busio.I2C(board.SCL1, board.SDA1)  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# create the trellis
trellis = NeoTrellis(i2c_bus)

# Set the brightness value (0 to 1.0)
trellis.brightness = 0.5



# some color definitions
OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

Credit = []

# this will be called when button events are received
def blink(event):
    # turn the LED on when a rising edge is detected
    #if event.edge == NeoTrellis.EDGE_RISING:
        #trellis.pixels[event.number] = BLUE
    # turn the LED off when a falling edge is detected
    #elif event.edge == NeoTrellis.EDGE_FALLING:
        #trellis.pixels[event.number] = OFF


    if event.edge == NeoTrellis.EDGE_RISING:
        if trellis.pixels[event.number] == CYAN:

        #trellis.pixels[r] = random.choice([RED, YELLOW, CYAN, GREEN, BLUE, PURPLE])
            trellis.pixels[event.number] = OFF
            print("Catch it!")
            a.play(wav)
            Credit.append(2)
        elif trellis.pixels[event.number] == OFF:
            print("Oops")
            trellis.pixels[event.number] = RED
            Credit.append(-1)




    # turn the LED off when a falling edge is detected





color=random.choice([RED, YELLOW, GREEN, CYAN, BLUE, PURPLE])
for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink


    # cycle the LEDs on startup

    trellis.pixels[i] = color
    time.sleep(0.05)

for i in range(16):
    trellis.pixels[i] = OFF
    time.sleep(0.05)



trellis.pixels[5] = CYAN
start = time.time()

speaker_enable = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
speaker_enable.switch_to_output(value=True)

data = open("Christmas_Soundboard_welcome.wav", "rb")
wav = audiocore.WaveFile(data)
a = audiopwmio.PWMAudioOut(board.A0)




i = 0
while i<=50:
    trellis.sync()

    # the trellis can only be read every 17 millisecons or so

    i=i+1
    if i ==50:
        for i in range(16):
            if trellis.pixels[i] == CYAN:
                print("The rat escaped")
                Credit.append(0)
        trellis.pixels.fill(0)
        i = 0
        print(sum(Credit))
        if sum(Credit) < 0:
            trellis.pixels.fill(0xFF0000)
            time.sleep(0.2)
            trellis.pixels.fill(0)
            time.sleep(0.2)
            trellis.pixels.fill(0xFF0000)
            time.sleep(0.2)
            trellis.pixels.fill(0)
            time.sleep(0.2)
            print("GAME OVER!")
            print("_________________________________________________________________________________")
            break
        r = random.randint(0,15)
        trellis.pixels[r] = CYAN

    time.sleep(0.02)

'''

# SPDX-FileCopyrightText: 2018 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Lauchpad drum mode

import time
import board
import busio
import audiopwmio
import audiocore
import audiomixer
from adafruit_neotrellis.neotrellis import NeoTrellis
import adafruit_trellism4



tempo = 180  # Starting BPM

# You can use the accelerometer to speed/slow down tempo by tilting!
ENABLE_TILT_TEMPO = True
MIN_TEMPO = 100
MAX_TEMPO = 300

SAMPLE_FOLDER = "/samples/"  # the name of the folder containing the samples
# You get 4 voices, they must all have the same sample rate and must
# all be mono or stereo (no mix-n-match!)
VOICES = [SAMPLE_FOLDER+"voice01.wav",
          SAMPLE_FOLDER+"voice02.wav",
          SAMPLE_FOLDER+"voice03.wav",
          SAMPLE_FOLDER+"voice04.wav"]

# four colors for the 4 voices, using 0 or 255 only will reduce buzz
OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
DRUM_COLOR = (CYAN,
              GREEN,
              YELLOW,
              RED)
# For the intro, pick any number of colors to make a fancy gradient!

# the color for the sweeping ticker bar
TICKER_COLOR = WHITE

# Our keypad + neopixel driver
i2c_bus = busio.I2C(board.SCL1, board.SDA1)  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# create the trellis
trellis = NeoTrellis(i2c_bus)

# Set the brightness value (0 to 1.0)
trellis.brightness = 0.5



# Our accelerometer




# Parse the first file to figure out what format its in
with open(VOICES[0], "rb") as f:
    wav = audiocore.WaveFile(f)
    print("%d channels, %d bits per sample, %d Hz sample rate " %
          (wav.channel_count, wav.bits_per_sample, wav.sample_rate))

    # Audio playback object - we'll go with either mono or stereo depending on
    # what we see in the first file
    if wav.channel_count == 1:
        audio = audiopwmio.PWMAudioOut(board.A0)
    elif wav.channel_count == 2:
        audio = audiopwmio.PWMAudioOut(board.A0)
    else:
        raise RuntimeError("Must be mono or stereo waves!")
    mixer = audiomixer.Mixer(voice_count=4,
                          sample_rate=wav.sample_rate,
                          channel_count=wav.channel_count,
                          bits_per_sample=wav.bits_per_sample,
                          samples_signed=True)
    audio.play(mixer)

samples = []
# Read the 4 wave files, convert to stereo samples, and store
# (show load status on neopixels and play audio once loaded too!)
for v in range(4):
    #trellis.pixels[v+4*0] = DRUM_COLOR[y]
    wave_file = open(VOICES[v], "rb")
    # OK we managed to open the wave OK
    for x in range(4):
        trellis.pixels[v+4*x] = DRUM_COLOR[v]
    sample = audiocore.WaveFile(wave_file)
    # debug play back on load!
    mixer.play(sample, voice=0)

    trellis.pixels[v+3*4] = DRUM_COLOR[v]
    samples.append(sample)

# Clear all pixels
trellis.pixels.fill(0)

# Our global state
current_step = 3 # we actually start on the last step since we increment first
# the state of the sequencer
beatset = [[False] * 8, [False] * 8, [False] * 8, [False] * 8]
# currently pressed buttons

def blink(event):

    # turn the LED on when a rising edge is detected
    if event.edge == NeoTrellis.EDGE_RISING:
        print("Button "+str(event.number)+" pushed")
        y = event.number%4
        x = event.number//4
        beatset[y][x] = not beatset[y][x] # enable the voice
        if beatset[y][x]:
            color = DRUM_COLOR[y]
        else:
            color = 0
        trellis.pixels[event.number] = color
    # turn the LED off when a falling edge is detected

for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink





while True:
    stamp = time.monotonic()
    # redraw the last step to remove the ticker bar (e.g. 'normal' view)
    for y in range(4):
        color = 0
        if beatset[y][current_step]:
            color = DRUM_COLOR[y]
        trellis.pixels[current_step] = color

    # next beat!
    current_step = (current_step + 1) % 4

    # draw the vertical ticker bar, with selected voices highlighted
    for y in range(4):
        if beatset[y][current_step]:
            r, g, b = DRUM_COLOR[y]
            color = (r//2, g//2, b//2)  # this voice is enabled
            #print("Playing: ", VOICES[y])
            mixer.play(samples[y], voice=y)
        else:
            color = TICKER_COLOR     # no voice on
        trellis.pixels[current_step] = color

    # handle button presses while we're waiting for the next tempo beat
    # also check the accelerometer if we're using it, to adjust tempo
    while time.monotonic() - stamp < 60/tempo:
        # Check for pressed buttons
        trellis.sync()
        time.sleep(0.02)


