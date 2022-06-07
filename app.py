import sys
import numpy as np
from time import sleep
import traceback
import cv2
from imutils.video import VideoStream
from VideoStreamSubscriber import VideoStreamSubscriber

import configparser
config = configparser.ConfigParser()
config.read('config/app.ini')
HOSTNAME = config['PUBLISHER']['HOSTNAME']
PORT = int(config['PUBLISHER']['PORT'])

if __name__ == "__main__":
    receiver = VideoStreamSubscriber(HOSTNAME, PORT)

    try:
        while True:
            msg, frame = receiver.receive()
            image = cv2.imdecode(np.frombuffer(frame, dtype='uint8'), -1)

            cv2.imshow("Pub Sub Receive", image)
            cv2.waitKey(1)
    except (KeyboardInterrupt, SystemExit):
        print('Exit due to keyboard interrupt')
    except Exception as ex:
        print('Python error with no Exception handler:')
        print('Traceback error:', ex)
        traceback.print_exc()
    finally:
        receiver.close()
        sys.exit()
