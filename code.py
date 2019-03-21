import cv2
import numpy as np
import math
import random

for l in range(0,2):
        if(l==1):
            length=15
        else:
            length=7
        for w in range(0,2):
            if(w==1):
                width=3
            else:
                width=1
            for a in range(0,12):
                angle=a*15*(math.pi)/180
                for c in range(0,2):
                    if(c==1):
                        color=(0,0,255)
                    else:
                        color=(255,0,0)
                    x_l = abs(math.ceil((length/2.0)*(math.cos(angle))))
                    x_u = 27 - x_l
                    y_l = abs(math.ceil((length/2.0)*(math.sin(angle))))
                    y_u = 27 - y_l
                    for num in range(0,1000):
                        centre_x = random.randint(x_l+2,x_u-1)
                        centre_y = random.randint(y_l+2,y_u-1)
                        pt1 = (centre_x-math.ceil((length/2.0)*(math.cos(angle))),centre_y+math.ceil((length/2.0)*(math.sin(angle))))
                        pt2 = (centre_x+math.ceil((length/2.0)*(math.cos(angle))),centre_y-math.ceil((length/2.0)*(math.sin(angle))))
                        img = np.zeros((28,28,3), np.uint8)
                        cv2.line(img,pt1,pt2,color,width)
                        path = str(l)+"_"+str(w)+"_"+str(a)+"_"+str(c)+"_"+str(num)+".jpg"
                        cv2.imwrite("data_set/"+path,img)