import time
import sys
from threading import Thread
from cam_stream import run_server
from ultrasonic import Ultrasonic

if __name__ == '__main__':
    try:
        Thread(target=run_server, args=()).start()
        ultrasonic = Ultrasonic()
        while True:
            sys.stdout.write("\rEntfernung: " + str(ultrasonic.getDistance()) + "cm")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Programm vom User gestoppt")
