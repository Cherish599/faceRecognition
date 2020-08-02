import os
import cv2
import numpy as np

images = []
labels = []
IMAGE_SIZE = 64

def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)
    # 获取图像的尺寸
    h, w, _ = image.shape

    # 获取图片宽高的最大值(最长边)
    longest_edge = max(h, w)

    # 计算短边需要增加多少像素，和长边保持一致；
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass

    # 给图像增加边界，
    BALCK = [0, 0, 0]
    constant = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BALCK)

    return cv2.resize(image, (height, width))

def read_path(path_name):
    for dir_item in os.listdir(path_name):
        # 从初始路径开始叠加，合并成为可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        # 判断路径是否为目录
        if os.path.isdir(full_path): #目录
            print(dir_item, 'is dir')
            read_path(full_path)
        else:   # 文件
            if dir_item.endswith('.jpg'):
                image = cv2.imread(full_path)
                print(image.shape)
                image = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)

                images.append(image)
                labels.append(path_name)

                print(labels)
    return images, labels

def load_dataset(path_name):
    images, labels = read_path(path_name)
    images = np.array(images)
    print(images)
    for i, label in enumerate(labels):
        if label.endswith('me'):
            labels[i] = 0
        elif label.endswith('tw'):
            labels[i] = 1
        else:
            labels[i] = 2
    return images, labels

if __name__ == '__main__':
    images, labels = load_dataset('./mypic')
    print(labels)