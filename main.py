from threading import Thread
from cam_stream import CamServer
from ultrasonic import Ultrasonic
from servo import Servo

if __name__ == '__main__':
    try:
        Thread(target=CamServer().run_server, args=()).start()
        Thread(target=Ultrasonic().print_distance_to_console, args=()).start()
        Thread(target=Servo().runServo(), args=()).start()
    except KeyboardInterrupt:
        print("Programm vom User gestoppt")
