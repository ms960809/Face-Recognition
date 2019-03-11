import cv2
import os
import numpy as np
from PIL import Image

#初始化识别器和人脸检测器
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')


def getImageand_labels(path):
    image_paths = [os.path.join(path,f) for f in os.listdir(path)]
    face_samples = []
    ids = []
    for image_path in image_paths:
        # 模式“L”
        # 为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度
        # 。在PIL中，从模式“RGB”转换为“L”模式是按照下面的公式转换的
        # L = R * 299 / 1000 + G * 587 / 1000 + B * 114 / 1000
        #转换成灰度图
        image = Image.open(image_path).convert('L')
        #转换为numpy数组
        image_np = np.array(image,'uint8')
        if os.path.split(image_path)[-1].split('.')[-1] != 'jpg':
            continue
        # 获取图片路径的相关信息
        image_id = int(os.path.split(image_path)[-1].split('.')[1])
        faces = detector.detectMultiScale(image_np)
        # 将图片和id都添加到list中
        for (x,y,w,h) in faces:
            face_samples.append(image_np[y:y+h,x:x+w])
            ids.append(image_id)
    return face_samples,ids

if __name__ == "__main__":
    print('正在训练人脸模型...')
    face,Ids = getImageand_labels('dataSet')
    recognizer.train(face,np.array(Ids))
    # 保存到数据到指定文件
    recognizer.save('./trainner/trainner.yml')
    print('已完成')