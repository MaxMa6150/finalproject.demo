# Final Project Demo

## Components:
QT PY 2040:
![80ab10b70a9447a0f1a1582951cff5e](https://user-images.githubusercontent.com/114200453/205554661-9bcd5967-a685-4f00-b26a-81e221a2b419.jpg)
Neotrellis keypad
![7488a3e7cad00aaf71475441a50a5d3](https://user-images.githubusercontent.com/114200453/205554711-53b2792c-b613-4fd8-928a-2f4bef98ae39.jpg)
Pico4ML:
![e67e6e920a570e3ee0892871c5ad916](https://user-images.githubusercontent.com/114200453/205554769-cc1fe12c-257b-42be-95f1-6ad6bd800a8f.jpg)
Stemma Speaker:
![2c44309be171846018c9e0021a1df9c](https://user-images.githubusercontent.com/114200453/205554787-44aea21a-ab14-4ae4-9037-837f4ea5dcaf.jpg)

### The components we will use:
MAX98357A I2S board:
![de3e8d731a78b61cdf41b02fe5280e3](https://user-images.githubusercontent.com/114200453/205554886-be96f45e-865e-47d1-92a9-9d0fca34395f.png)

# the Whack a Mole:

# code

The code for the code for whack-a-mole mode is in first half of [code.py](https://github.com/MaxMa6150/finalproject.demo/blob/main/code.py).

# design

![636b7ca723a340c71f5bbcdf99d054b](https://user-images.githubusercontent.com/114200453/205553588-4998bc56-a30c-4892-9ede-2b20ec399142.jpg)


# troubleshooting

We use the  [neotrellis.simpletest.py](https://github.com/adafruit/Adafruit_CircuitPython_NeoTrellis/blob/main/examples/neotrellis_simpletest.py) 
Since the cable is not available, we solder the cable with copper pins. 
![1551d4fc2dba9cf7454fcc54bca023e](https://user-images.githubusercontent.com/113209201/205519974-c958b217-2fb5-4a26-ac36-9b393b230299.jpg)

# System diagram

![4952cf835d45d4de3d077f0bec4ef9a](https://user-images.githubusercontent.com/113209201/205527555-4c39911b-fb37-4d23-89e1-d4f304852c9b.jpg)
We will use PIO in pico4ml to rp2040. 

# demo1

https://youtu.be/9epRLCVayiY

The hole was randomly generated:
![0e44561f16b1917239642e189afe396](https://user-images.githubusercontent.com/113209201/205417980-ccd6b806-9c1c-4ca9-b883-0b86a4d445ff.jpg)

If you hit it in time, it will show no light, or you may hit wrong which shows red light, and the rat will escape after 0.5 second. 
![1fb9372dd3fc49cf10cbd6e4c82d438](https://user-images.githubusercontent.com/113209201/205418051-4dfb38aa-c2ff-424c-bb64-eb0b75730781.jpg)

hit right gain +2, hit wrong gain -1, hit none gain 0 credits. 

![1591f55f30e0efb9959507cbaad0104](https://user-images.githubusercontent.com/113209201/205418071-c22ed010-0436-4fa4-b551-a5c84b25396e.png)

after you got below 0 score, game over!
![b1dd96557909350e81a502d35c14e64](https://user-images.githubusercontent.com/113209201/205418063-43d84f5d-1f88-475b-adac-9487aaf1e8e9.jpg)

# the 4-steps Drumer 

# code

The code for the code for 4-step drumer mode is in second half of [code.py](https://github.com/MaxMa6150/finalproject.demo/blob/main/code.py).

# Design

![636b7ca723a340c71f5bbcdf99d054b](https://user-images.githubusercontent.com/114200453/205553680-971f081e-1312-4f0b-a658-c0102464a50a.jpg)


# System diagram:

![4952cf835d45d4de3d077f0bec4ef9a](https://user-images.githubusercontent.com/113209201/205527600-5bcd38d2-2480-4058-9eba-8b182687626f.jpg)

# trouble shooting:

1. the original code we used have the audioio module which didn't implement on qtpy2040, so we use audiopwmio instead and it has a lower resolution of audio out. In the next step, we will use a I2S drived audio AMP to drive the speaker. The new board MAX98357A has its own I2S module to play digital music file with higher resolution, then we can add more instrument file for lauchpad music playing mode. The new design is shown below:

![37ef09f08b88d881d7e9ab135455026](https://user-images.githubusercontent.com/114200453/205553995-0a5854b5-1a4b-4630-9eff-6a9f49ceb76e.jpg)


# demo2

https://youtu.be/yeAbvyMj_us

The 4 steps sequencer:

we use 4/4 time signature. 

![10fc630b4f2c8406bac2706b8bfcd4b](https://user-images.githubusercontent.com/113209201/205418094-1c88b3c4-5eb0-494a-baac-6569413cd4b1.jpg)

The drums are assigned with different color, and each button on y axis represents a quarter of a period. You can produce different combination of drums by pressing down those drum button and create drum beats.

![bd59270a8f012a40c5f49dafbe0900b](https://user-images.githubusercontent.com/113209201/205418163-4cc14d23-2ab0-4c8f-b9df-3c60070a3c02.jpg)

# In progress
## LCD on Pico4ML display:

we will show the credits on LCD screen which will read the data from RP2040 through PIO in/out. The "hello-world" code for LCD enable is shown [here](https://github.com/MaxMa6150/finalproject.demo/blob/main/hello_LCD.c). 

![gswto-8gi1d](https://user-images.githubusercontent.com/113209201/205536461-e9dffa7d-6352-4bbb-873e-25df8729c929.gif)

Later, we will use the LCD display to record the score of Whack a Mole and display the patterns in the 4 steps drumer. The connection between Pico4ML with LCD and QT PY 2040 is needed.

## Pico4ML and PY2040 connection:

Inspired by anothering group in demo day, we find out that Pico4ML with LCD display will be connected with QT PY 2040 with UART with Tx/RX port. The design diagram is shown below:

![a33de4dd40d9f26efe16ebe6f541f0e](https://user-images.githubusercontent.com/114200453/205554246-17c9fd91-0dd5-495f-bbae-505ebc2ae730.jpg)

We can use uart with/without pio. The code we will potentially edit is shown [here](https://github.com/MaxMa6150/finalproject.demo/tree/main/References%20(Uart%20connection)).

