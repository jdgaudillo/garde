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


def getImageInformation(file_path):
    """
    Extracts the file name and file format of a specific file
    Input:
        file_path: str
            Absolute path of the file
            
    Output:
        example: random_file1.jpg
        file_name: str
            file_name of the file:: 
            "random_file"
        file_format: str
            file format of the file
            ".jpg"
    
    """
    if os.path.isdir(file_path) == False:
        file_dir = os.path.basename(file_path)
        file_name = os.path.splitext(file_dir)[0]
        file_format = os.path.splitext(file_path)[1]
    return file_name, file_format


def save(annotation, new_filename, original_path):
    """
    Saves the file to a new directory according to the annotation using the new filename
    Input:
        annotation:
            Annotation of the disease i.e. diabetic retinopathy
        new_filename:
            New File name of the file
        original_path:
            Original File Path of the file
    Output:
    """
    
    destination = "../../standardized-data/"
    if os.path.isdir(destination + "/" + annotation) == False:
        os.mkdir(destination + "/" + annotation)
        print(annotation, "FOLDER CREATED")
    if os.path.exists(destination + "/" + annotation + "/" + new_filename):
        print('FILE EXISTS: DOUBLE CHECK FOR DUPLICATION :', new_filename)
    else:
        shutil.copyfile(original_path, destination + "/" + annotation + "/" + new_filename)
    return
	

if __name__ == '__main__':

	source = "KAGGLE"
	filename = "155_right.jpg"
	new_filename = getNewFilename(source, 10, "diabetic_retinopathy_1", "jpg")

	mapping(source, filename, new_filename)

