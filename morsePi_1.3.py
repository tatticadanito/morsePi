# Made by \- tatticadanito -/

#TO-DO:
# Make it comunicate with another device (socket)
# Add the possibility to insert special chars (morsecode.scpillips.com/morse2.html)
# Make the user choose the LED's PIN (standard: 18)
#ALREADY DID:
# Make it work with more than 1 word
# Add ASCII and MORSE output on screen
# Add sound

import RPi.GPIO as GPIO
import time
import sys
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

morseChar =    {'A': '.-',	'B': '-...',	'C': '-.-.',
		'D': '-..',	'E': '.',	'F': '..-.',
		'G': '--.',	'H': '....',	'I': '..',
		'J': '.---',	'K': '-.-',	'L': '.-..',
		'M': '--',	'N': '-.',	'O': '---',
		'P': '.--.',	'Q': '--.-',	'R': '.-.',
		'S': '...',	'T': '-',	'U': '..-',
		'V': '...-',	'W': '.--',	'X': '-..-',
		'Y': '-.--',	'Z': '--..',	' ': ' '} 		

def currentChar(char):
	print("Current char:\t", char, "\t|", morseChar[char])

def elementSpace():			#Timing between dots and dashes
	GPIO.output(18,GPIO.LOW)
	time.sleep(0.2)

def dot():				#Dot timing
	GPIO.output(18,GPIO.HIGH)
	subprocess.call(['play', '-n', 'synth', '0.2', 'sin', '1000'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
	elementSpace()

def dash():				#Dash timing
	GPIO.output(18,GPIO.HIGH)
	subprocess.call(['play', '-n', 'synth', '0.5', 'sin', '1000'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
	elementSpace()

def charSpace():			#Timing between each character
	GPIO.output(18,GPIO.LOW)
	time.sleep(0.4)
	elementSpace()

def wordSpace():			#Timing between each word
	GPIO.output(18,GPIO.LOW)
	time.sleep(1.2)
	elementSpace()

inputString = input("String to convert: ")
if not inputString.replace(' ','').isalpha():
	sys.exit("Invalid input !")
inputString = inputString.upper()

print("\t\tASCII   | MORSE") 
for c in inputString:
	currentChar(c)
	if c == 'A':
		dot()
		dash()

	elif c == 'B':
		dash()
		for _ in range(3):
			dot()

	elif c == 'C':
		dash()
		dot()
		dash()
		dot()

	elif c == 'D':
		dash()
		for _ in range(2):
			dot()
	elif c == 'E':
		dot()

	elif c == 'F':
		for _ in range(2):
			dot()
		dash()
		dot()

	elif c == 'G':
		for _ in range(2):
			dash()
		dot()

	elif c == 'H':
		for _ in range(4):
			dot()

	elif c == 'I':
		for _ in range(2):
			dot()

	elif c == 'J':
		dot()
		for _ in range(3):
			dash()

	elif c == 'K':
		dash()
		dot()
		dash()

	elif c == 'L':
		dot()
		dash()
		for _ in range(2):
			dot()

	elif c == 'M':
		for _ in range(2):
			dash()

	elif c == 'N':
		dash()
		dot()

	elif c == 'O':
		for _ in range(3):
			dash()

	elif c == 'P':
		dot()
		for _ in range(2):
			dash()
		dot()

	elif c == 'Q':
		for _ in range(2):
			dash()
		dot()
		dash()

	elif c == 'R':
		dot()
		dash()
		dot()

	elif c == 'S':
		for _ in range(3):
			dot()

	elif c == 'T':
		dot()

	elif c == 'U':
		for _ in range(2):
			dot()
		dash()

	elif c == 'V':
		for _ in range(3):
			dot()
		dash()

	elif c == 'W':
		dot()
		for _ in range(2):
			dash()

	elif c == 'X':
		dash()
		for _ in range(2):
			dot()
		dash()

	elif c == 'Y':
		dash()
		dot()
		for _ in range(2):
			dash()
	
	elif c == 'Z':
		for _ in range(2):
			dash()
		for _ in range(2):
			dot()
	elif c == ' ':
		wordSpace()


	elementSpace()