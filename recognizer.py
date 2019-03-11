# conding:utf-8
import os
import cv2
import numpy as np


def recognizerFn():
    # 初始化识别器
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    for f in os.listdir('trainner'):
        recognizer.read(os.path.join('trainner',f))
        # 创建分类器
        face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
        cam = cv2.VideoCapture(0)
        # 设置显示字体
        font = cv2.FONT_HERSHEY_SIMPLEX
        while 1:
            ret,img = cam.read()
            # 图像灰度化
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.2,5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
                #预测函数
                img_id,conf = recognizer.predict(gray[y:y+h,x:x+w])
                if conf > 50:
                    if img_id == 1:
                        img_id = 'JPB'
                    elif img_id == 2:
                        img_id = 'ZMS'
                else:
                    img_id = "Unknown"
                cv2.putText(img,str(img_id),(x-10,y+h+30),font,1,(0,255,0),2)
            cv2.imshow("Jiao Pengbo's Face Recognition",img)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    recognizerFn()


