import warnings
warnings.filterwarnings("ignore")

import os
import pandas as pd

def get_STARE_annotation(filename):
	annotation_file = "../data/annotation/STARE.csv"

	annotation = pd.read_csv(annotation_file, sep=",", header=None)
	annotation.columns = ["imageid", "annotation"]

	annotations = annotation.loc[annotation.imageid==filename, "annotation"].values
	annotations = [annot.split(" ") for annot in annotations] 

	return annotations


def get_HRF_annotation(filename):
	annotation = filename.split(".")[0]
	annotation = annotation.split("_")[-1]

	if annotation == "dr":
		return "diabetic_retinopathy"
	elif annotation == "g":
		return "glaucoma"
	else:
		return "normal"


def get_MESSIDOR_annotation(filename):
	annotation_file = "../data/annotation/MESSIDOR.csv"
	annotation = pd.read_csv(annotation_file, sep=",")
	annotation.loc[:, "retinopathy_grade"] = "retinopathygrade" + "_" + annotation.retinopathy_grade.map(str)
	annotation.loc[:, "macular_edema"] = "macular_edema" + "_" + annotation.macular_edema.map(str)

	annot = annotation.loc[annotation.image_name==filename, ["retinopathy_grade", "macular_edema"]].values

	return annot[0]


def get_ROC_annotation(filename):

	return "microaneurysm"


def get_KAGGLE_annotation(filename):

	annot = pd.read_csv("../data/annotation/KAGGLE.CSV", sep = ",")

	filename = filename.split(".")[0]
	
	label = annot.loc[annot.image == filename]["level"].values

	if label == 0:
		
		return "normal"

	else:

		return "diabetic_retinopathy_"+str(int(label))


def get_DIARETDB0_annotation(source, filename):
	filename = filename.split(".")[0] + ".dot"
	annotation_dir = os.path.join("../data/annotation", source)
	annotation_dir = os.path.join(annotation_dir, filename)
	
	with open(annotation_dir, "r") as f:
		txt_list = f.readline()
		ann_list = txt_list.split()
		annotation = [value for value in ann_list if value != 'n/a']

	return annotation
	
	
def get_eOPHTHA_annotation(source):
	data_dir = "../data/eOPHTHA"

	for i in os.listdir(data_dir):
		if i[:2] == 'MA':
			annotation = 'Microaneurysms'
		elif i[:2] == 'EX':
			annotation = 'Exudates'
		else:
			annotation = 'Healthy'

	return annotation