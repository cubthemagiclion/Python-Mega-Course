import cv2
import numpy
im_g = cv2.imread("smallgray.png",0)
ims = numpy.vstack((im_g,im_g,im_g))
print("printing three im_g: ")
print(ims)
lst = numpy.vsplit(ims,3)
print("printing after the split now: ")
print(lst)