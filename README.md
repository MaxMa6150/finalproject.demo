# finalproject.demo

# the Whack a Mole:

https://youtu.be/9epRLCVayiY

# code

The code for the code for whack-a-mole mode is in first half of code.py.

```
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
```

# troubleshooting
We use the  [neotrellis.simpletest.py](https://github.com/adafruit/Adafruit_CircuitPython_NeoTrellis/blob/main/examples/neotrellis_simpletest.py) 
Since the cable is not available, we solder the cable with copper pins. 
![1551d4fc2dba9cf7454fcc54bca023e](https://user-images.githubusercontent.com/113209201/205519974-c958b217-2fb5-4a26-ac36-9b393b230299.jpg)
# circuit diagram
![4952cf835d45d4de3d077f0bec4ef9a](https://user-images.githubusercontent.com/113209201/205527555-4c39911b-fb37-4d23-89e1-d4f304852c9b.jpg)
We will use PIO in pico4ml to rp2040. 
# demo1

The hole was randomly generated:
![0e44561f16b1917239642e189afe396](https://user-images.githubusercontent.com/113209201/205417980-ccd6b806-9c1c-4ca9-b883-0b86a4d445ff.jpg)

If you hit it in time, it will show no light, or you may hit wrong which shows red light, and the rat will escape after 0.5 second. 
![1fb9372dd3fc49cf10cbd6e4c82d438](https://user-images.githubusercontent.com/113209201/205418051-4dfb38aa-c2ff-424c-bb64-eb0b75730781.jpg)

hit right gain +2, hit wrong gain -1, hit none gain 0 credits. 

![1591f55f30e0efb9959507cbaad0104](https://user-images.githubusercontent.com/113209201/205418071-c22ed010-0436-4fa4-b551-a5c84b25396e.png)

after you got below 0 score, game over!
![b1dd96557909350e81a502d35c14e64](https://user-images.githubusercontent.com/113209201/205418063-43d84f5d-1f88-475b-adac-9487aaf1e8e9.jpg)

# the 4-steps Drumer 
https://youtu.be/yeAbvyMj_us
# code

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

# circuit diagram:
![4952cf835d45d4de3d077f0bec4ef9a](https://user-images.githubusercontent.com/113209201/205527600-5bcd38d2-2480-4058-9eba-8b182687626f.jpg)
# trouble shooting:
1. the original code we used have the audioio module which didn't implement on qtpy2040, so we use audiopwmio instead and it has a lower resolution of audio out. In the next step, we will use a I2S drived audio AMP to drive the speaker. 

# demo2
The 4 steps sequencer:
we use 4/4 time signature. 
![10fc630b4f2c8406bac2706b8bfcd4b](https://user-images.githubusercontent.com/113209201/205418094-1c88b3c4-5eb0-494a-baac-6569413cd4b1.jpg)
The drums are assigned with different color, and each button on y axis represents a quarter of a period. You can produce different combination of drums by pressing down those drum button and create drum beats.
![bd59270a8f012a40c5f49dafbe0900b](https://user-images.githubusercontent.com/113209201/205418163-4cc14d23-2ab0-4c8f-b9df-3c60070a3c02.jpg)

# In progress
LCD on Pico4ML display:

we will show the credits on LCD screen which will read the data from RP2040 through PIO in/out. 

![gswto-8gi1d](https://user-images.githubusercontent.com/113209201/205536461-e9dffa7d-6352-4bbb-873e-25df8729c929.gif)

We will use the LCD display to record the score of Whack a Mole and display the patterns in the 4 steps drumer. 
