#!/usr/bin/env python
import sys
from mpd import MPDClient
import RPi.GPIO as GPIO
import chime


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

bouncetime = 1000
button_pin_play = 16
button_pin_prev = 22
button_pin_next = 15


def sound_success():
  #chime.theme('mario')
  #chime.info()
  #Sssssttt
  pass

def connectMPD():
    try:
        client = MPDClient()               # create client object
        client.timeout = 200               # network timeout in seconds (floats allowed), default: None
        client.idletimeout = None  
        #print("Connecting...")
        client.connect("localhost", 6600) 
        #print("Connected!")
        return client
    except:
        print('Could not connect to MPD server')

def handle_play_pause(channel):
    #print("Play/Pause was pushed!")
    client = connectMPD()
    status = client.status()
    #print(status)
    if (status['state'] == 'play'):
      client.pause()
    else:
      client.play()
    sound_success()

def handle_prev(channel):
    #print("Prev was pushed!")
    client = connectMPD()
    client.previous()
    sound_success()

def handle_next(channel):
    #print("Next was pushed!")
    client = connectMPD()
    client.next()
    sound_success()


def register_pins():
  GPIO.setup(button_pin_play, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
  GPIO.add_event_detect(button_pin_play, GPIO.FALLING, callback=handle_play_pause, bouncetime=bouncetime)
  GPIO.setup(button_pin_prev, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
  GPIO.add_event_detect(button_pin_prev, GPIO.FALLING, callback=handle_prev, bouncetime=bouncetime)
  GPIO.setup(button_pin_next, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
  GPIO.add_event_detect(button_pin_next, GPIO.FALLING, callback=handle_next, bouncetime=bouncetime)

def startup():
  register_pins()
  #message = input("Press enter to quit\n\n") # Run until someone presses enter
  #while: pass
  try:
    while True:
      pass
  except KeyboardInterrupt:
    sys.exit(0)
  except:
    pass

def handle_cleanup():
  GPIO.cleanup()


def main():
    try:
      startup()
    finally:
        handle_cleanup() # Stuff that happens when program exits

if __name__=='__main__':
    main()

