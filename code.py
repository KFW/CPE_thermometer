# Office Thermometer
# for Adafruit Circuit Python Express (CPE)
# Uses color to indicate temp range, and then NeoPixels for exact temp
# light sensor turns off NeoPixels if it's dark
# assumes orientation with USB port down


from adafruit_circuitplayground.express import cpx
import time

# low values on NeoPixels 
BLANK = (0,0,0)
BLUE = (0,0,4)     # 50's
BG = (0,2,2)      # 60's 
GREEN = (0,4,0)    # 70's
ORANGE = (3,1,0)   # 80's
RED = (14,0,0)      # 90's
TEMP_COLOR = {5:BLUE, 6:BG, 7:GREEN, 8:ORANGE, 9:RED}

while True:
    cpx.pixels.fill(BLANK) # make sure pixels refresh
    if cpx.light > 10: # don't display temp if room is dark
        temp = int(cpx.temperature * 1.8 + 32.5)    # extra 0.5 to make sure temp 
                                                    # rounds correctly
        temp -= 6   # CPE seems to consistently read 6 degrees F too high
                    # consistent on 2 different CPEs
        if temp < 50: temp = 50 # in the unlikely event temp is lower than 50's
        if temp > 99: temp = 99 # in unlikely event temp in the 100's
        tens = temp//10
        digit = temp%10
        # for temp ending in '0' light up only pixel 0 (tenth pixel as mounted)
        if digit == 0:
            cpx.pixels[0] = TEMP_COLOR[tens]
        # otherwise fill in digits clockwise from 7 o'clock position
        else:
            for i in range(digit):
                cpx.pixels[9 - i] = TEMP_COLOR[tens]   # use '9 -' since pixels
                                                        # in reverse order

    time.sleep(60) # cycle every 60 seconds
