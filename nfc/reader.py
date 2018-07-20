
import signal
import time
import sys
import RPi.GPIO as GPIO


from pirc522 import RFID

run = True
rdr = RFID()
util = rdr.util()
util.debug = True


def card_reader():
    GPIO.setwarnings(False)
    def end_read(signal,frame):
        global run
        print("\nCtrl+C captured, ending read.")
        run = False
        rdr.cleanup()
        sys.exit()


    signal.signal(signal.SIGINT, end_read)

    print("NFC Ready . . . ")

    while run:
        rdr.wait_for_tag()

        (error, data) = rdr.request()
        (error, uid) = rdr.anticoll()
        if not error:

            tag_id=str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])+str(uid[4])
            return (tag_id)




