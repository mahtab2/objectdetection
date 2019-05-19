import cv2

font = cv2.FONT_ITALIC

img = cv2.imread("Untitled.jpg", cv2.IMREAD_GRAYSCALE)

a, mask= cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

contours, a = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)

    cv2.drawContours(img, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    print(len(approx))
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
    elif len(approx) == 6:
        cv2.putText(img, "hexagon", (x, y), font, 1, (0))
    else:
        cv2.putText(img, "Circle", (x, y), font, 1, (0))

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
