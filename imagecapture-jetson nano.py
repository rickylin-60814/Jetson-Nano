#coding=utf-8
import cv2
from threading import Timer
import datetime
import time

def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

# To flip the image, modify the flip_method parameter (0 and 2 are the most common)
print(gstreamer_pipeline(flip_method=0))
# 選擇攝影機
cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

datetime_dt = datetime.datetime.today()# 獲得當地時間
#datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")  # 格式化日期
this_seconds = int(datetime_dt.strftime("%S"))#格式化秒
imagecapture=5
second_seconds = this_seconds+imagecapture#每隔多少秒擷取
print(this_seconds)
print(second_seconds)
x=0
img = cv2.imread('5.jpg')

width = cap.get(3)  # float
height = cap.get(4) # float
print(cap.isOpened())
while(True):
    # 從攝影機擷取影像
    return_value, image = cap.read()

    datetime_dt = datetime.datetime.today()#再次取得當地時間
    this_seconds = int(datetime_dt.strftime("%S"))#再次格式化秒

    if second_seconds == this_seconds:
        second_seconds = this_seconds+imagecapture
        datetime_str = datetime_dt.strftime("%H-%M-%S_%d%m%Y")
        x=x+1
        cv2.imwrite(str(datetime_str) + ".png", image)
        print(this_seconds)
        print(second_seconds)

    if second_seconds >60 and this_seconds < 3:
        second_seconds = second_seconds-60

# 釋放資源
del(cap)