import cv2

## opening videocapture
cap = cv2.VideoCapture('rtsp://admin:Supervisor@172.18.191.177:554/live/0/MAIN/')

## some videowriter props
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fps = 20
#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#fourcc = cv2.VideoWriter_fourcc('m', 'p', 'e', 'g')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

## open and set props
vout = cv2.VideoWriter()
vout.open('output.mp4',fourcc,fps,sz,True)

cnt = 0
while cnt<200:
cnt += 1
print(cnt)
_, frame = cap.read()
cv2.putText(frame, str(cnt), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1, cv2.LINE_AA)
vout.write(frame)

vout.release()
cap.release()
