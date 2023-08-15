import cv2 

img = cv2.imread("solar-system.jpg")


cv2.putText(img, "Sun", (20,300), cv2.FONT_HERSHEY_DUPLEX , 0.5, (255,255,255))
cv2.putText(img, "Mercury", (120,250), cv2.FONT_HERSHEY_DUPLEX , 0.5, (255,255,255))
cv2.putText(img, "Venus", (190,270), cv2.FONT_HERSHEY_DUPLEX , 0.5, (255,255,255))
cv2.putText(img, "Earth", (290,270), cv2.FONT_HERSHEY_DUPLEX , 0.5, (255,255,255))
cv2.putText(img, "Mars", (380,260), cv2.FONT_HERSHEY_DUPLEX , 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (580,400), cv2.FONT_HERSHEY_DUPLEX , 0.5, (255,255,255))
cv2.putText(img, "Saturn", (770,320), cv2.FONT_HERSHEY_DUPLEX , 0.5, (255,255,255))
cv2.putText(img, "Uranus", (950,300), cv2.FONT_HERSHEY_DUPLEX , 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1090,300), cv2.FONT_HERSHEY_DUPLEX , 0.5, (255,255,255))




cv2.imshow("OUTPUT", img)
cv2.waitKey(0)