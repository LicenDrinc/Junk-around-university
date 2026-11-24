import cv2
# my_photo = cv2.imread('./../фото и видео/SonicLilac.png')
my_photo = cv2.imread('./../фото и видео/Баг/Снимок экрана (163).png', cv2.IMREAD_REDUCED_COLOR_2)
print(my_photo.shape)
gray = my_photo
for i in range(1):
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2HSV)
for i in range(2):
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2Lab)
for i in range(4):
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2HLS)
# cv2.imshow('--', gray)

# cv2.circle(my_photo, (300, 200), 150, (0,0,255), 2)
cv2.ellipse(my_photo, (300,200), (100, 150), 45, 0, 360, (0,0,255), 2)
cv2.ellipse(my_photo, (300,200), (150, 100), 45, 0, 360, (0,0,255), 2)
cv2.ellipse(my_photo, (300,200), (50, 150), 0, 0, 360, (0,0,255), 2)
cv2.arrowedLine(my_photo, (600,500), (420, 320), (0,0,255), 4, cv2.LINE_AA, tipLength=0.3)

cv2.imshow('-', my_photo)
cv2.waitKey(0)
cv2.destroyAllWindows()