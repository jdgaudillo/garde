import warnings
warnings.filterwarnings("ignore")

import os
import csv
import shutil


from data_cleaning.annotation import *


def clean_MESSIDOR_dataset():
	data_dir = "../data/MESSIDOR"

	for base in os.listdir(data_dir):
		print(">>>>>>>> ", base)
		if not base.endswith(".DS_Store"):
			base_dir = os.path.join(data_dir, base)
			image_files = os.listdir(base_dir)
			renamed_files = [base + "_" + image_file for image_file in image_files]

			for i, file in enumerate(image_files):
				print(">>>>>>>> ", file)
				os.rename(os.path.join(base_dir, file), os.path.join(data_dir, renamed_files[i]))
		print(">>>>>>> Successfully renamed files")


def clean_MESSIDOR_annotation():
	data_dir = "../data/annotation/MESSIDOR/"

	for file in glob.glob(data_dir + "*.xls"):
		print(file)
		df = pd.read_excel(file)
		df.columns = ["image_name", "dept", "retinopathy_grade", "macular_edema"]
		df = df.drop("dept", axis=1)

		base = file.split("/")[-1]
		base = base.split(".")[0]
		base = base.split("_")[-1]
		df.loc[:, "image_name"] = base + "_" + df.image_name.map(str)

		outfile = "../data/annotation/MESSIDOR.csv"
		if os.path.isfile(outfile):
			df.to_csv(outfile, mode="a", index=False, header=False)
		else:
			df.to_csv(outfile, index=False)


def getImageInformation(file_path):
    if os.path.isdir(file_path) == False:
        file_dir = os.path.basename(file_path)
        file_name = os.path.splitext(file_dir)[0]
        file_format = os.path.splitext(file_path)[1]

    return file_name, file_format


def getAnnotation(source, filename):
	no_annotations = ["DRIONSDB", "CHASEDB", "FIRE", "DRIVE", "DIARETDB1"]

	if source in no_annotations:
		return None

	elif source == "MESSIDOR":
		annotation = get_MESSIDOR_annotation(filename)
		print(">>>>>>>>>", filename, annotation)

	elif source == "HRF":
		annotation = get_HRF_annotation(filename)
		print(">>>>>>>>>", filename, annotation)

	elif source == "STARE":
		annotation = get_STARE_annotation(filename)
		print(">>>>>>>>>", filename, annotation)

	elif source == "ROC":
		annotation = get_ROC_annotation(filename)
		print(">>>>>>>>>", filename, annotation)

	elif source == "DIARETDB0":
		annotation = get_DIARETDB0_annotation(source, filename)
		print(">>>>>>>>>", filename, annotation)

	elif source == "eOPHTHA":
		annotation = get_eOPHTHA_annotation(filename)
		print(">>>>>>>>>", filename, annotation)

	elif source == "KAGGLE":
		annotation = get_KAGGLE_annotation(filename)
		print(">>>>>>>>>", filename, annotation)

	return annotation


def getNewFilename(source, id, annotation, file_format):
	file_format = file_format.replace(".", "")

	if annotation is None:

		return source+"_"+str(id)+"."+file_format

	elif type(annotation) is str:

		return source+"_"+str(id)+"."+annotation+"."+file_format

	else:

		annotation = ".".join(annotation)
		return source+"_"+str(id)+"."+annotation+"."+file_format


def mapping(source, filename, new_filename):

	""" LOCAL
	file = "../standardized-data/map.csv" """

	# SERVER
	file = "/mnt/sdb/A-EYE/standardized-data/map.csv"

	if not os.path.exists(file):
		with open(file, "w") as f:
			wr = csv.DictWriter(f, fieldnames = ["source", "filename", "new_filename"])
			wr.writeheader()
			wr.writerow({"source":source, "filename":filename, "new_filename":new_filename})
	else:
		with open(file, "a") as f:
			wr = csv.DictWriter(f, fieldnames = ["source", "filename", "new_filename"])
			wr.writerow({"source":source, "filename":filename, "new_filename":new_filename})


def saveImage(annotation, new_filename, original_path):
	#LOCAL
	#destination_dir = "../standardized-data/"

	# SERVER
	destination_dir = "/mnt/sdb/A-EYE/standardized-data/"

	if not os.path.isdir(destination_dir):
		os.mkdir(destination_dir)

	if annotation is None:
		annotation_dir = os.path.join(destination_dir, "no-label")

	elif type(annotation) is str:
		annotation_dir = os.path.join(destination_dir, annotation)

	else:
		annotation_dir = os.path.join(destination_dir, "multilabel")

	if not os.path.isdir(annotation_dir):
		os.mkdir(annotation_dir)

	shutil.copyfile(original_path, os.path.join(annotation_dir, new_filename))



