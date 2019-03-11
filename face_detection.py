# -*- coding: utf-8 -*-
import cv2

def faceDetection(id):
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
    cap = cv2.VideoCapture(0)
    sampleNum = 0
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = img[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                sampleNum = sampleNum + 1
                cv2.imwrite("dataSet/User." + str(id) + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])  #
                cv2.imshow('jiaopb', img)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif sampleNum > 500:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    faceDetection()