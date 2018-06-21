#!/usr/bin/env python
# USAGE
# python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

# import the necessary packages
#from imutils.video import VideoStream
#from imutils.video.pivideostream import PiVideoStream
#import argparse
#import imutils
import time
#import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
#import numpy as np
import roslib
import sys
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import rospkg
import os
#ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--picamera", type=int, default=-1,
#	help="whether or not the Raspberry Pi camera should be used")
#args = vars(ap.parse_args())
#vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
#time.sleep(5.0)
#vs = PiVideoStream().start()
camera = PiCamera()
resolution=(320,240)
camera.resolution = resolution
camera.framerate = 20
rawCapture = PiRGBArray(camera, size=resolution)
#stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
#rawCapture = np.empty((240*320*3,), dtype=np.uint8)

time.sleep(2.0)
def CVControl():




	# initialize the list of class labels MobileNet SSD was trained to
	# detect, then generate a set of bounding box colors for each class


	rospy.init_node("rear_view", anonymous = True)
	image_pub = rospy.Publisher("rear_cv",Image, queue_size = 10)

	rate = rospy.Rate(20)
	bridge = CvBridge()

	# loop over the frames from the video stream
	while not rospy.is_shutdown():
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
		#frame = vs.read()
		#frame = imutils.resize(frame,width=400)
		# grab the frame dimensions and convert it to a blob
		#rawCapture = np.empty((240*320*3,), dtype=np.uint8)
		frame = camera.capture(rawCapture, 'bgr', use_video_port=True)
		image = rawCapture.array		
#rawCapture = rawCapture.reshape((240, 320, 3))
		image_pub.publish(bridge.cv2_to_imgmsg(image, "bgr8"))		# update the FPS counter
#		rawCapture.seek(0)
		rawCapture.truncate(0)
#	        rospy.spin()


if __name__ == '__main__':
	CVControl()
# stop the timer and display FPS information
# fps.stop()
# print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
# print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
#cv2.destroyAllWindows()
#vs.stop()
