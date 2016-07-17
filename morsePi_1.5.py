# Made by \- tatticadanito -/

#TO-DO:
# Make it comunicate with another device (socket)
# Add the possibility to insert special chars(?) (morsecode.scpillips.com/morse2.html)
# Make the user choose the LED's PIN (standard: 18)
#ALREADY DID:
# 1. Make it work with more than 1 word
# 2. Add ASCII and MORSE output on screen
# 3. Add sound
# 4. Add the possibility to use numbers
# 5. Optimizated conversion method (no more 30+ 'elif')

import RPi.GPIO as GPIO
import time
import sys
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

morseChar =    {'A': '.-',	'B': '-...',	'C': '-.-.',	#Valid chars dictionary
		'D': '-..',	'E': '.',	'F': '..-.',
		'G': '--.',	'H': '....',	'I': '..',
		'J': '.---',	'K': '-.-',	'L': '.-..',
		'M': '--',	'N': '-.',	'O': '---',
		'P': '.--.',	'Q': '--.-',	'R': '.-.',
		'S': '...',	'T': '-',	'U': '..-',
		'V': '...-',	'W': '.--',	'X': '-..-',
		'Y': '-.--',	'Z': '--..',	' ': ' ',
		'0': '-----', '1': '.----', '2': '..---',
		'3': '...--', '4': '....-', '5': '.....',
		'6': '-....', '7': '--...', '8': '---..',
		'9': '----.'} 		

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

inputString = input("String to convert: ")	#Input && check if its valid
#if not inputString.replace(" ","").isalnum():
inputString = inputString.upper()	
for c in inputString:
	if c not in morseChar:
		sys.exit("Invalid input !")


print("\t\tASCII   | MORSE")		#Start printing && making noise 
for c in inputString:
	currentChar(c)
	for x in range(len(morseChar[c])):	#Finally no more 30+ 'elif'
		if morseChar[c][x] == '.':
			dot()
		elif morseChar[c][x] == '-':
			dash()
		elif morseChar[c][x] == ' ':
			wordSpace()
	elementSpace()
