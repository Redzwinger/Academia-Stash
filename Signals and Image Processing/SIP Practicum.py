
import cv2

img = cv2.imread("subaru.jpg")

down_width = 1280
down_height = 720
down_points = (down_width, down_height)
img = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)

hh, ww = img.shape[:2]

# resize down, then back up
w, h = (8, 8)
result1 = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
result1 = cv2.resize(result1, (ww, hh), interpolation=cv2.INTER_AREA)

w, h = (16, 16)
result2 = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
result2 = cv2.resize(result2, (ww, hh), interpolation=cv2.INTER_AREA)

w, h = (32, 32)
result3 = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
result3 = cv2.resize(result3, (ww, hh), interpolation=cv2.INTER_AREA)

w, h = (64, 64)
result4 = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
result4 = cv2.resize(result4, (ww, hh), interpolation=cv2.INTER_AREA)

# show result
cv2.imshow("Original Image", img)
cv2.imshow("8 Bit", result1)
cv2.imshow("16 Bit", result2)
cv2.imshow("32 Bit", result3)
cv2.imshow("64 Bit", result4)
cv2.waitKey(0)
cv2.destroyAllWindows()
