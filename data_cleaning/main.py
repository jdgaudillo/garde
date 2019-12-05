import warnings
warnings.filterwarnings("ignore")

import os
import glob
import time

from data_cleaning.clean import getImageInformation, getNewFilename, getAnnotation, mapping, saveImage


def main(source):
	start_time = time.time()

	""" LOCAL
	data_dir = "../data/" """

	# SERVER         					
	data_dir = "/mnt/sdb/A-EYE" 

	source_dir = os.path.join(data_dir, source)

	file_formats = (".JPG", ".jpg", ".tif", ".png", ".jpeg", ".ppm")

	for i, image_file in enumerate(os.listdir(source_dir)):
		if image_file.endswith(file_formats):

			filename, file_format = getImageInformation(os.path.join(source_dir, image_file))
			annotation = getAnnotation(source, image_file)

			new_filename = getNewFilename(source, str(i), annotation.lower(), file_format)

			saveImage(annotation, new_filename, os.path.join(source_dir, image_file))
			mapping(source, filename, new_filename)

			print(">>>>>>>>>> Successfully cleaned ", i, image_file, new_filename, "\n")
	
	print(">>>>> TOTAL RUNTIME: ", time.time() - start_time)