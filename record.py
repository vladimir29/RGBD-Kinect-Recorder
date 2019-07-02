import freenect
import cv2
import numpy as np
import png
import imageio
from PIL import Image
import os

def get_video():
	array,_ = freenect.sync_get_video()
	array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
	return array

def get_depth():
	array,_ = freenect.sync_get_depth()
	array = array.astype(np.uint8)
	return array

def delete_folder_contents(folder):
	for the_file in os.listdir(folder):
	    file_path = os.path.join(folder, the_file)
	    try:
	        if os.path.isfile(file_path):
	            os.unlink(file_path)
	        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
	    except Exception as e:
	        print(e)

image_out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (640, 480))
depth_out = cv2.VideoWriter('depth.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (640, 480))

# file = open('video.txt', 'w')

w = png.Writer(640, 480, greyscale=True)
# dept = open('depth.png', 'w+')
i = 0

while 1:
	print(1)
	frame = get_video()
	print('got video')
	cv2.imshow('RGB image',frame)
	image_out.write(frame)

	depth = get_depth()
	print 'got depth'

	# open depth data file
	depth_filename = 'depths/depth' + str(i) + '.png'
	depth_filename = 'depth.png'
	depth_filename = 'depth.jpg'
	dept = open(depth_filename, 'w+')

	# write depth data to opened file
	# w = png.Writer(640, 480, greyscale=True)
	# w.write(dept, depth)
	cv2.imwrite(depth_filename, depth)

	# read depth data from file
	depth_img = cv2.imread(depth_filename)

	# write depth data to video
	depth_out.write(depth_img)

	# remove depth file for rewriting
	# os.remove('depth.png')

	# dept.close()
	i += 1

	k = cv2.waitKey(5)
	if k == 27:
		delete_folder_contents('depths/')
		break

cv2.destroyAllWindows()

# file.close()

image_out.release()
depth_out.release()
