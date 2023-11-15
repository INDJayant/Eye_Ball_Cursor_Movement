import cv2

cam = cv2.VideoCapture(0)
_, frame = cam.read()
frame = cv2.flip(frame, 2)
# rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# window_name = 'Image'
# cv2.imshow(window_name, rgb_frame)
cv2.imshow('Eye Controlled Mouse', frame)
cv2.waitKey(0)
# while True:
#     window_name = 'Image'
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
