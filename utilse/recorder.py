import pyscreenshot as ImageGrab
import numpy as np
import cv2
import time



def getStat_file():
    f = open("../rec_stat.txt", "r")
    txt = f.read()
    f.close()
    
    return (txt == "1" or txt == "1\n")


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 2.0, (1920,1080))

start_time = time.time()
while getStat_file():
    img = ImageGrab.grab()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    #cv2.imshow("Screenshot", frame)
    if cv2.waitKey(1) == 27:
        break

out.release()
cv2.destroyAllWindows()
