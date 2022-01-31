import time
import board
from rainbowio import colorwheel
import neopixel
import adafruit_hcsr04
import digitalio
import simpleio
import random
from analogio import AnalogIn
import colorsys

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP3, echo_pin=board.GP2)
PIEZO_PIN = board.GP15
num_pixels = 36
pin1 = digitalio.DigitalInOut(board.GP16)
pin2 = digitalio.DigitalInOut(board.GP17)
pin3 = AnalogIn(board.GP26)
pixels = neopixel.NeoPixel(board.GP0, num_pixels, auto_write=False)

pixels.brightness = 1
setmode = 0
curtime1 = 0
endtime1 = 0
curtime2 = 0
endtime2 = 0
led1hue = random.random()
on = False
onvalue = 13000
sonar_dis = 100
tones = {
    "B0": 31,
    "C1": 33,
    "CS1": 35,
    "D1": 3 + 7,
    "DS1": 39,
    "E1": 41,
    "F1": 44,
    "FS1": 46,
    "G1": 49,
    "GS1": 52,
    "A1": 55,
    "AS1": 58,
    "B1": 62,
    "C2": 65,
    "CS2": 69,
    "D2": 73,
    "DS2": 78,
    "E2": 82,
    "F2": 87,
    "FS2": 93,
    "G2": 98,
    "GS2": 104,
    "A2": 110,
    "AS2": 117,
    "B2": 123,
    "C3": 131,
    "CS3": 139,
    "D3": 147,
    "DS3": 156,
    "E3": 165,
    "F3": 175,
    "FS3": 185,
    "G3": 196,
    "GS3": 208,
    "A3": 220,
    "AS3": 233,
    "B3": 247,
    "C4": 262,
    "CS4": 277,
    "D4": 294,
    "DS4": 311,
    "E4": 330,
    "F4": 349,
    "FS4": 370,
    "G4": 392,
    "GS4": 415,
    "A4": 440,
    "AS4": 466,
    "B4": 494,
    "C5": 523,
    "CS5": 554,
    "D5": 587,
    "DS5": 622,
    "E5": 659,
    "F5": 698,
    "FS5": 740,
    "G5": 784,
    "GS5": 831,
    "A5": 880,
    "AS5": 932,
    "B5": 988,
    "C6": 1047,
    "CS6": 1109,
    "D6": 1175,
    "DS6": 1245,
    "E6": 1319,
    "F6": 1397,
    "FS6": 1480,
    "G6": 1568,
    "GS6": 1661,
    "A6": 1760,
    "AS6": 1865,
    "B6": 1976,
    "C7": 2093,
    "CS7": 2217,
    "D7": 2349,
    "DS7": 2489,
    "E7": 2637,
    "F7": 2794,
    "FS7": 2960,
    "G7": 3136,
    "GS7": 3322,
    "A7": 3520,
    "AS7": 3729,
    "B7": 3951,
    "C8": 4186,
    "CS8": 4435,
    "D8": 4699,
    "DS8": 4978,
    "E8": 5274,
    "F8": 5588,
    "FS8": 5920,
    "G8": 6272,
    "GS8": 6645,
    "A8": 7040,
    "AS8": 7459,
    "B8": 7902,
    0: 0,
    '0': 0,
    "SILENT": 0,
    "R": 0
}
songs = []
tempos = []

song2 = ['E7', 'E7', 0, 'E7', 0, 'C7', 'E7', 0, 'G7', 0, 0, 0, 'G6', 0, 0, 0,
         'C7', 0, 0, 'G6', 0, 0, 'E6', 0, 0, 'A6', 0, 'B6', 0, 'AS6', 'A6', 0,
         'G6', 'E7', 'G7', 'A7', 0, 'F7', 'G7', 0, 'E7', 0, 'C7', 'D7', 'B6', 0, 0,
         'C7', 0, 0, 'G6', 0, 0, 'E6', 0, 0, 'A6', 0, 'B6', 0, 'AS6', 'A6', 0,
         'G6', 'E7', 'G7', 'A7', 0, 'F7', 'G7', 0, 'E7', 0, 'C7', 'D7', 'B6', 0, 0]
tempo2 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
          12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
          9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
          12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
          9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

song3 = ['G4', 'E5', 'D5', 'C5', 'G4', '0', 'G4', 'E5', 'D5', 'C5', 'A4', '0', 'A4', 'F5', 'E5', 'D5', 'B4', '0', 'G5',
         'G5', 'F5', 'D5', 'E5', 'C5'
         ]
tempo3 = [
    25, 25, 25, 25, 75, 25,
    25, 25, 25, 25, 75, 25,
    25, 25, 25, 25, 75, 25,
    25, 25, 25, 25, 50, 25, 25
]

song4 = ['A4', 'A4', 'R', 'R', 'A4', 'R', 'F4', 'R', 'C5', 'R', 'A4', 'R', 'F4', 'R', 'C5', 'R', 'A4', 'R', 'E5', 'R',
         'E5', 'R', 'E5', 'R', 'F5', 'R', 'C5', 'R', 'G5', 'R', 'F5', 'R', 'C5', 'R', 'A4', 'R', 'F4', 'F4', 'F4',
         'AS4', 'F5', 'DS5', 'D5', 'C5', 'AS5', 'F5', 'DS5', 'D5', 'C5', 'AS5', 'F5', 'DS5', 'D5', 'DS5', 'C5'
         ]
tempo4 = [
    50, 20, 50, 20, 50, 20, 40, 5, 20, 5, 60, 10, 40, 5, 20, 5, 60, 80, 50, 20, 50, 20, 50, 20, 40, 5, 20, 5, 60, 10,
    40, 5, 20, 5, 60, 40
    , 21, 21, 21, 128, 128, 21, 21, 21, 128, 64, 21, 21, 21, 128, 64, 21, 21, 21, 128
]
songs.append(song2)
songs.append(song3)
songs.append(song4)
tempos.append(tempo2)
tempos.append(tempo3)
tempos.append(tempo4)


class Cdata:
    def __init__(self):
        self.number = random.randint(0, 35)
        self.colorhue = random.random()
        self.timeing = 0
        self.bright = random.randint(1, 255)
        self.increase = 1

    def update(self):
        self.bright += self.increase
        if self.bright == 256:
            self.increase = -1
        if self.bright == 0:
            self.increase = 1
            self.number = random.randint(0, 35)
            while self.check():
                self.number = random.randint(0, 35)
            self.colorhue = random.random()

    def check(self):
        ret = True
        for i in cleds:
            if i.number == self.number:
                if i == self:
                    continue
                return True
        return False


def rainbow(speed):
    for k in range(10):
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = colorwheel(pixel_index & 255)
            pixels.show()
            time.sleep(speed)


def led1(speed, speed2, hue):
    for i in range(30):
        pixels.fill(colorsys.hsv_to_rgb(hue, 1, 255 / 29 * i))
        pixels.show()
        time.sleep(speed2)
    time.sleep(speed)
    for i in range(30):
        pixels.fill(colorsys.hsv_to_rgb(hue, 1, 255 / 29 * (29 - i)))
        pixels.show()
        time.sleep(speed2)


def led11(speed, speed2, hue, sa):
    for i in range(30):
        pixels.fill(colorsys.hsv_to_rgb(hue, sa, 255 / 29 * i))
        pixels.show()
        time.sleep(speed2)
    time.sleep(speed)
    for i in range(30):
        pixels.fill(colorsys.hsv_to_rgb(hue, sa, 255 / 29 * (29 - i)))
        pixels.show()
        time.sleep(speed2)


def led2(speed1, color):
    for j in range(5):
        for i in range(6):
            if i == 4:
                setstripcolor(i, (255,0,0))
            else:
                setstripcolor(i, color)
            pixels.show()
            time.sleep(speed1)
        alloff(0)


def led3(speed):
    for i in range(5000):
        pixels[random.randint(0, 35)] = colorsys.hsv_to_rgb(random.random(), 1, 255)
        pixels.show()
        time.sleep(speed)
        alloff(0)


def led4(time1, color):
    for j in range(5):
        for i in range(6):
            alloff(0)
            if i ==4:
                setstripcolor(i, (255,0,0))
            else:
                setstripcolor(i, color)
            pixels.show()
            time.sleep(time1)


def alloff(time1):
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(time1)


def setstripcolor(setnumber, color):
    for i in range(6):
        pixels[i + setnumber * 6] = color


def playtone(ton, tempo):
    simpleio.tone(PIEZO_PIN, ton, duration=tempo / 100)


def playsong(mysong, tempo):
    for i in range(len(mysong)):
        playtone(tones[mysong[i]], tempo[i])


cleds = []
for i in range(12):
    cleds.append(Cdata())

while True:
    if pin1.value == 1:
        curtime1 = time.monotonic_ns() / 1000000000
        temp = 0
        while pin1.value == 1:
            setstripcolor(temp, (255, 0, 0))
            pixels.show()
            simpleio.tone(PIEZO_PIN, 2000, duration=0.3)
            temp += 1
        endtime1 = time.monotonic_ns() / 1000000000

    if pin2.value == 1:
        curtime2 = time.monotonic_ns() / 1000000000
        temp = 0
        while pin2.value == 1:
            setstripcolor(temp, (0, 255, 0))
            pixels.show()
            simpleio.tone(PIEZO_PIN, 1000, duration=0.3)
            temp += 1
        endtime2 = time.monotonic_ns() / 1000000000

    if endtime1 - curtime1 < 0.2:
        pass
    elif endtime1 - curtime1 < 0.4:
        setmode = 0
    elif endtime1 - curtime1 < 0.7:
        setmode = 1
    elif endtime1 - curtime1 < 1.0:
        setmode = 2
    elif endtime1 - curtime1 < 1.3:
        setmode = 3
    elif endtime1 - curtime1 < 1.6:
        setmode = 4
    elif endtime1 - curtime1 < 1.9:
        setmode = 5
        led1hue = random.random()
        led1(0.5, 0.01, led1hue)
        rainbow(0.01)
    else:
        pass

    if endtime2 - curtime2 < 0.2:
        pass
    elif endtime2 - curtime2 < 0.4:
        onvalue = 100
    elif endtime2 - curtime2 < 0.7:
        onvalue = 4000
    elif endtime2 - curtime2 < 1.0:
        onvalue = 7000
    elif endtime2 - curtime2 < 1.3:
        onvalue = 13000
    elif endtime2 - curtime2 < 1.6:
        onvalue = 20000
    elif endtime2 - curtime2 < 1.9:
        onvalue = 30000
    alloff(0)

    curtime1 = time.monotonic_ns() / 1000000000
    endtime1 = time.monotonic_ns() / 1000000000
    curtime2 = time.monotonic_ns() / 1000000000
    endtime2 = time.monotonic_ns() / 1000000000
    time.sleep(0.1)
    try:
        print(sonar.distance)
    except:
        pass
    if pin3.value < onvalue:
        on = True
    else:
        on = False
    if on:
        if setmode == 0:
            try:
                if sonar_dis > sonar.distance:
                    led11(20, 0.1, 1, led1hue)
            except:
                pass
        elif setmode == 1:
            try:
                if sonar_dis > sonar.distance:
                    led4(3, colorsys.hsv_to_rgb(led1hue, 1, 255))
            except:
                pass
        elif setmode == 2:
            try:
                if sonar_dis > sonar.distance:
                    led3(0.01)
            except:
                pass
        elif setmode == 3:
            try:
                if sonar_dis > sonar.distance:
                    for i in range(10000):
                        for j in cleds:
                            pixels[j.number] = colorsys.hsv_to_rgb(j.colorhue, 1, j.bright)
                            j.update()
                        pixels.show()
            except:
                pass
        elif setmode == 4:
            try:
                if sonar_dis > sonar.distance:
                    led2(3, colorsys.hsv_to_rgb(led1hue, 1, 255))
            except:
                pass





