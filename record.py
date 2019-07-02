import freenect
import cv2
import numpy as np

def get_video():
	array,_ = freenect.sync_get_video()
	array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
	return array

def get_depth():
	array,_ = freenect.sync_get_depth()
	array = array.astype(np.uint8)
	return array

image_out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (640, 480))
depth_out = cv2.VideoWriter('depth.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (640, 480))

depth_filename = 'depth.jpg'

while 1:
	print(1)
	frame = get_video()
	print('got video')
	cv2.imshow('RGB image',frame)
	image_out.write(frame)

	depth = get_depth()
	print 'got depth'

	# open depth data file
	dept = open(depth_filename, 'w+')

	# write depth data to opened file
	cv2.imwrite(depth_filename, depth)

	# read depth data from file
	depth_img = cv2.imread(depth_filename)

	# write depth data to video
	depth_out.write(depth_img)

	dept.close()

	k = cv2.waitKey(5)
	if k == 27:
		break

cv2.destroyAllWindows()

image_out.release()
depth_out.release()
