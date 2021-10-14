import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


print('''
Enter your Choice:-
1) Photo
2) Video / Webcam
''')
choice = int(input("Enter your Choice here:-"))

if choice == 1:
    img = cv2.imread('img_1.jpg') # put img here

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    cv2.waitKey()

else:
    print("Press ESC to EXIT")
    cap = cv2.VideoCapture(0) # put video here, default- webcam

    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k==27:
            break

    cap.release()
