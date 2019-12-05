import warnings
warnings.filterwarnings("ignore")

import os
import csv

def getNewFilename(source, id, annotation, file_format):

	if annotation is None:

		return source+"_"+str(id)+"."+file_format

	elif type(annotation) is list:

		annotation = ".".join(annotation)
		return source+"_"+str(id)+"."+annotation+"."+file_format

	else:

		return source+"_"+str(id)+"_"+annotation+"."+file_format


def mapping(source, filename, new_filename):

	file = "../standardized-data/map.csv"

	if not os.path.exists(file):
		with open(file, "w") as f:
			wr = csv.DictWriter(f, fieldnames = ["source", "filename", "new_filename"])
			wr.writeheader()
			wr.writerow({"source":source, "filename":filename, "new_filename":new_filename})
	else:
		with open(file, "a") as f:
			wr = csv.DictWriter(f, fieldnames = ["source", "filename", "new_filename"])
			wr.writerow({"source":source, "filename":filename, "new_filename":new_filename})


if __name__ == '__main__':

	source = "KAGGLE"
	filename = "155_right.jpg"
	new_filename = getNewFilename(source, 10, "diabetic_retinopathy_1", "jpg")

	mapping(source, filename, new_filename)

