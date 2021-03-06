import imagecodecs
import tifffile as tiff
import cv2
import random
import json
import shutil, os
from random import randint
import fnmatch
import hashlib
from PIL import Image
import numpy as np


#crops a defined image
def imcrop(path,size):
	img = tiff.imread(path, 0)
	#helper and counter variables
	a=img.shape
	i=0
	d=0
	j=0

	#crops and exports chunks of the images
	while i <= a[0]-size-1:
		j=0
		while j <= a[1]-size-1:
			crop = img[j:(j+size), i:(i+size),:]
			filename = "./TNBC/gitrepo/tnbc/Image_Processing/imgsplit/editedimages/file_%d.jpg"%d
			crop = cv2.resize(crop,(224,224))
			cv2.imwrite(filename, crop)
			d=d+1
			j+=size
		i=i+size




#crops n random regions of the image 
def randcrop(path, filename, size):
	filekey = dict()
	img = tiff.imread(path,0) #brings the image into memory
	x=0
	for i in range(0,img.shape[0]-size,+img.shape[0]//10):
		for j in range(0, img.shape[1]-size, +img.shape[1]//10):
			random.seed(x)
			w = i+ randint(0,img.shape[0]//10-size)
			print(f"w={w}")
			l = j+ randint(0,img.shape[1]//10-size)
			crop = img[w:(w+size) ,l:(l+size)] #crops size squared area around the defined random coordinate
			newfilename = "patch_"+str(x)+".tif"
			filepath = "/storage/tnbc/segments/newseg/224/"+newfilename
			filekey[newfilename] = {"name":filename, "path":filepath, "x":w, "y":l, "seed":x, "size":size, "im_shape":img.shape}
			cv2.imwrite(filepath, crop) #saves the image with the filepath mentioned above
			x+=1
	with open("/storage/tnbc/segments/newseg/224/metadata_224.json", "w+") as outfile:
		json.dump(filekey, outfile)

def new_randcrop():
	size=224
	filekey = dict()
	x=0
	dir = "/storage/tnbc"
	key="hne"
	exclude = ['benchmark','segments']
	exclude_im=["20200220-515-191_17-1049_17A-HER2-Biopsy-HnE-40X.tif","20200220-161-112_15-619_15_A-HER2-Biopsy-HnE-40X.tif", "20200220-142-246_15-3385_15_A-HER2-Biopsy-HnE-40X.tif", "20210821_752_307_19_W3_19_H7_ER_Surgery_HnE_40X.tif", "20210821_897_497_19_1816_19_A_ER_biopsy_HnE_40X.tif"]
	for subdir, dirs, files in os.walk(dir):
		dirs[:] = [d for d in dirs if d not in exclude]
		files[:] = [f for f in files if f not in exclude_im]
		print(f"files: {files}\n")
		for file in files:
			if fnmatch.fnmatch(file, '*.tif'):
				if key in file.lower():
					path=str(os.path.join(subdir, file))
					img = tiff.imread(path,0) #brings the image into memory
					print(str(file))
					for i in range(0,img.shape[0]-size,+img.shape[0]//10):
						for j in range(0, img.shape[1]-size, +img.shape[1]//10):
							random.seed(x)
							w = i+ randint(0,img.shape[0]//10-size)
							random.seed(x)
							l = j+ randint(0,img.shape[1]//10-size)
							crop = img[w:(w+size) ,l:(l+size)] #crops size squared area around the defined random coordinate
							newfilename = "patch_"+str(x)+".tif"
							filepath = "/storage/tnbc/segments/newseg/224/"+newfilename
							filekey[newfilename] = {"name":file, "path":filepath, "x":w, "y":l, "seed":x, "size":size, "im_shape":img.shape}
							cv2.imwrite(filepath, crop) #saves the image with the filepath mentioned above
							x+=1
	with open("/storage/tnbc/segments/newseg/224/metadata_224.json", "w+") as outfile:
		json.dump(filekey, outfile)
			




#defines a random image by path
def randpath():

	# PLEASE CHANGE	THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY
	dir = "/storage/tnbc/segments/224:224/Raw"
	filename = random.choice(os.listdir(dir))
	path = os.path.join(dir, filename)
	return (path,filename)



#Calls the crop function 
def visit(n):
	for i in range(n):
		tpath = randpath() #generates a random path
		shutil.copy(tpath[0], '/storage/tnbc/segments/224:224/Send')
		#randcrop(tpath[0], tpath[1], 580,10) #Calls the function randcrop


#returns all .tif files from the entire storage by mapping 
#from the root inside all subdirectories. This returns a path
#to every single .tif file in the entire directory defined
#by the user
def tiffimgs():
	# PLEASE CHANGE THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY
	dir = "/storage/tnbc/segments/newseg/224"
	for subdir, dirs, files in os.walk(dir):
		for file in files:
			if fnmatch.fnmatch(file, '*.tif'):
				prpath=str(os.path.join(subdir, file))
				#call your preferred function here
				print(file)
				#can be randcrop or imgcrop or any
				#custom function


#does the same function as tiffimgs() while ensuring that
#the paths accepted are only thos of images with 'key' in
#their name. This can be used to run certian functions on
#specifically HnE/Vimentin/CD31 files.
def keyimgs(key):
	# PLEASE CHANGE THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY
	dir = "/storage/tnbc"
	exclude = ['benchmark','segments']
	exclude_im=["20200220-515-191_17-1049_17A-HER2-Biopsy-HnE-40X.tif","20200220-161-112_15-619_15_A-HER2-Biopsy-HnE-40X.tif", "20200220-142-246_15-3385_15_A-HER2-Biopsy-HnE-40X.tif"]
	for subdir, dirs, files in os.walk(dir):
		dirs[:] = [d for d in dirs if d not in exclude]
		files[:] = [f for f in files if f not in exclude_im]
		for file in files:
			if fnmatch.fnmatch(file, '*.tif'):
				if key in file.lower():
					prpath=str(os.path.join(subdir, file))
					print(file)
					#call yout preferred function here
					#can be	randcrop or imgcrop or any
					#custom function

new_randcrop()

