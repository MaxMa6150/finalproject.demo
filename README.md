# finalproject.demo
# the Whack a Mole:
https://youtu.be/9epRLCVayiY

# code:
      
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
# problems
We use the  [neotrellis.simpletest.py](https://github.com/adafruit/Adafruit_CircuitPython_NeoTrellis/blob/main/examples/neotrellis_simpletest.py) 
Since the cable is not available, we solder the cable with copper pins. 
![1551d4fc2dba9cf7454fcc54bca023e](https://user-images.githubusercontent.com/113209201/205519974-c958b217-2fb5-4a26-ac36-9b393b230299.jpg)
# circuit diagram
![4952cf835d45d4de3d077f0bec4ef9a](https://user-images.githubusercontent.com/113209201/205527555-4c39911b-fb37-4d23-89e1-d4f304852c9b.jpg)

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

# circuit diagram:
![4952cf835d45d4de3d077f0bec4ef9a](https://user-images.githubusercontent.com/113209201/205527600-5bcd38d2-2480-4058-9eba-8b182687626f.jpg)

# demo2
The 4 steps sequencer:
we use 4/4 time signature. 
![10fc630b4f2c8406bac2706b8bfcd4b](https://user-images.githubusercontent.com/113209201/205418094-1c88b3c4-5eb0-494a-baac-6569413cd4b1.jpg)
The drums are assigned with different color, and each button on y axis represents a quarter of a period. You can produce different combination of drums by pressing down those drum button and create drum beats.
![bd59270a8f012a40c5f49dafbe0900b](https://user-images.githubusercontent.com/113209201/205418163-4cc14d23-2ab0-4c8f-b9df-3c60070a3c02.jpg)
