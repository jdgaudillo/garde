import warnings
warnings.filterwarnings("ignore")

import pandas as pd

def get_ROC_annotation(source, filename):

	return "microaneurysm"


def get_KAGGLE_annotation(source, filename):

	annot = pd.read_csv("../data/annotation/KAGGLE.CSV", sep = ",")

	filename = filename.split(".")[0]
	
	label = annot.loc[annot.image == filename]["level"].values

	if label == 0:
		
		return "normal"

	else:

		return "diabetic_retinopathy_"+str(int(label))