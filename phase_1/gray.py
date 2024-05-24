import cv2 as c
img = c.imread(r"C:\Users\KITS\Pictures\virat.jpg")
print(img)
gry = c.cvtColor(img,c.COLOR_BGR2GRAY)
c.imwrite("gray.jpg",gry)