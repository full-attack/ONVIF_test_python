import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://admin:Supervisor@172.18.191.177:554/live/0/MAIN/')

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))


fps = 20
#fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v') # note the lower case
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

vout = cv2.VideoWriter()
success = vout.open('output.mp4',fourcc,fps,size,True)
while True:
ret, frame = cap.read()
if not ret:
break

frame = cv2.flip(frame, -1)

vout.write(frame)

cv2.imshow('frame', frame)

if cv2.waitKey(1) & 0xFF == ord('q'):
break

cap.release()
vout.release()
cv2.destroyAllWindows()
