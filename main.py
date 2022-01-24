import time
import board
from rainbowio import colorwheel
import neopixel
import adafruit_hcsr04
import digitalio
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP3, echo_pin=board.GP2)

PIEZO_PIN = board.GP15

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 24
pin = digitalio.DigitalInOut(board.GP16)
pixels = neopixel.NeoPixel(board.GP0, num_pixels, auto_write=False)
pixels.brightness = 0.5

tones = {
    "B0": 31,
    "C1": 33,
    "CS1": 35,
    "D1": 37,
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
    "SILENT": 0,
    "R":0
}

song = ["E5", "G5", "A5", "P", "E5", "G5", "B5", "A5", "P", "E5", "G5", "A5", "P", "G5", "E5"]

song2 = ['E7', 'E7', 0, 'E7', 0, 'C7', 'E7', 0, 'G7', 0, 0, 0, 'G6', 0, 0, 0,
         'C7', 0, 0, 'G6', 0, 0, 'E6', 0, 0, 'A6', 0, 'B6', 0, 'AS6', 'A6', 0,
         'G6', 'E7', 'G7', 'A7', 0, 'F7', 'G7', 0, 'E7', 0, 'C7', 'D7', 'B6', 0, 0,
         'C7', 0, 0, 'G6', 0, 0, 'E6', 0, 0, 'A6', 0, 'B6', 0, 'AS6', 'A6', 0,
         'G6', 'E7', 'G7', 'A7', 0, 'F7', 'G7', 0, 'E7', 0, 'C7', 'D7', 'B6', 0, 0]

song3 = ['SILENT', 'AS7', 'SILENT', 'GS7', 'SILENT', 'GS6', 'SILENT', 'E7', 'SILENT', 'GS6', 'SILENT', 'DS7', 'E8',
         'SILENT', 'F5', 'E8', 'A7', 'SILENT', 'AS5', 'SILENT', 'F4', 'SILENT', 'FS8', 'SILENT', 'C5', 'SILENT', 'F5',
         'SILENT', 'FS8', 'SILENT', 'E8', 'SILENT', 'AS4', 'SILENT', 'A7', 'SILENT', 'F6', 'SILENT', 'CS8', 'SILENT',
         'G8', 'SILENT', 'AS4', 'F4', 'SILENT', 'F8', 'SILENT', 'FS8', 'B7', 'SILENT', 'FS7', 'F5', 'SILENT', 'A6',
         'SILENT', 'E7', 'SILENT', 'FS7', 'SILENT', 'D7', 'SILENT', 'DS8', 'SILENT', 'C6', 'SILENT', 'CS6', 'A7',
         'SILENT', 'B7', 'SILENT', 'A7', 'SILENT', 'F7', 'SILENT', 'D5', 'SILENT', 'AS7', 'SILENT', 'B7', 'SILENT',
         'D5', 'GS7', 'SILENT', 'A5', 'SILENT', 'G5', 'SILENT', 'F5', 'SILENT', 'AS7', 'SILENT', 'E7', 'SILENT', 'FS7',
         'G8', 'SILENT', 'F4', 'SILENT', 'D7', 'SILENT']

song4 = [ 'A4'	,
'R'	,
'A4'	,
'R'	,
'A4'	,
'R'	,
'F4'	,
'R'	,
'C5'	,
'R'	,
'A4'	,
'R'	,
'F4'	,
'R'	,
'C5'	,
'R'	,
'A4'	,
'R'	,
'E5'	,
'R'	,
'E5'	,
'R'	,
'E5'	,
'R'	,
'F5'	,
'R'	,
'C5'	,
'R'	,
'G5'	,
'R'	,
'F5'	,
'R'	,
'C5'	,
'R'	,
'A4'	,
'R'	,
'F4'	,
'F4'	,
'F4'	,
'AS4'	,
'F5'	,
'DS5'	,
'D5'	,
'C5'	,
'AS5'	,
'F5'	,
'DS5'	,
'D5'	,
'C5'	,
'AS5'	,
'F5'	,
'DS5'	,
'D5'	,
'DS5'	,
'C5'	,

]
tempo4=[
 50, 20, 50, 20, 50, 20, 40, 5, 20, 5,  60, 10, 40, 5, 20, 5, 60, 80, 50, 20, 50, 20, 50, 20, 40, 5, 20, 5,  60, 10, 40, 5,  20, 5, 60, 40
    ,21, 21, 21, 128, 128, 21, 21, 21, 128, 64, 21, 21, 21, 128, 64, 21, 21, 21, 128
]
tempo3 = [
    4, 2, 15, 2, 3, 3, 8, 2, 4, 2, 2, 2, 2, 4, 4, 3, 2, 13, 2, 47, 4, 9, 3, 10, 2, 9, 2, 8, 2, 51, 2, 5, 2, 20, 2, 15,
    2, 22, 3, 8, 2, 18, 4, 2, 2, 2, 18, 2, 2, 8, 2, 2, 3, 2, 3, 2, 20, 2, 13, 2, 10, 2, 11, 2, 5, 2, 2, 2, 2, 39, 3, 8,
    2, 4, 3, 10, 3, 13, 3, 12, 2, 2, 9, 2, 36, 3, 3, 2, 4, 2, 5, 2, 25, 2, 2, 21, 2, 14, 2, 6]

tempo2 = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
          12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
          9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
          12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
          9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]


def rainbow(speed):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(pixel_index & 255)
        pixels.show()
        print('rainbow')
        time.sleep(speed)


def alloff():
    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
        print('red')
    pixels.show()


def playtone(ton, tempo):
    simpleio.tone(PIEZO_PIN, ton, duration=tempo / 100)


def playsong(mysong, tempo):
    for i in range(len(mysong)):
        playtone(tones[mysong[i]], tempo[i])


while True:
    playsong(song4, tempo4)

#
# while True:
#     if pin.value == 1:
#         rainbow(0.01)
#     alloff()
#     try:
#         print((sonar.distance,))
#     except RuntimeError:
#         print("Retrying!")
#     time.sleep(0.1)
