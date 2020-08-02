import cv2
import time

path_name = 'mypic/tw'
# time_start = time.time()
cap = cv2.VideoCapture(0)   # 使用摄像头
# fps = 0
num = 0

# 设置人脸分类器
classfier = cv2.CascadeClassifier('D:\\SoftWareInstall\\anaconda3\\pkgs\\libopencv-3.4.2-h20b85fd_0\\Library\\etc\\haarcascades\\haarcascade_frontalface_alt2.xml')

while cap.isOpened():
    # print("摄像头开启成功")
    ret, frame = cap.read()     # 摄像头读取一帧数据
    if not ret:     # 失败，程序退出
        exit(-1)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 图像灰度处理
    # 人脸检测
    faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32,32))
    # fps = 1/time.time() - time_start
    if len(faceRects) > 0:
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.putText(frame, 'Cherish99', (100, 100), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 2)      # 文本显示
            cv2.rectangle(frame, (x-10, y-10), (x+w+10, y+h+10), (255, 0, 0), 2)    # 在图片上画框
            image = frame[y-10:y+h+10, x-10:x+w+10]
            img_name = '%s/%d.jpg'%(path_name, num)
            cv2.imwrite(img_name, image)
            num += 1

            if num == 200:
                exit(0)


    cv2.imshow('FaceRecognizing', frame)    # 图像在窗口显示
    key = cv2.waitKey(30) & 0xff    # 等待事件
    if key == 27:   # Esc键，循环结束
        exit(0)
    # time_start = time.time()
    # time.sleep(0.001)

cap.release()
cv2.destroyAllWindows()
