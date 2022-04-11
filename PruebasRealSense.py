import cv2
import pyrealsense2 as rs
from realsense_depth import *

#Initialize Camera Intel Realsense

dc = DepthCamera()

ret, depth_frame, color_frame = dc.get_frame()

cv2.imshow("depth frame", depth_frame)
cv2.imshow("Color frame", color_frame)
cv2.waitKey(0)
