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
		

def get_DIARETDB0_annotation(source, filename):
    """
    Gets the DIARETDBO annotations
    
    Input:
        source: string
            Source of the dataset
        filename: string
            Specific filename for the annotation
    Output:
        annotation: python list
            List of annotations available
    
    """
    with open("../../data/annotation/" + source + '/' + filename, "r") as f:
        txt_list = f.readline()
        ann_list = txt_list.split()
        annotation = [value for value in ann_list if value != 'n/a']
    return annotation
	
	
def get_eOPHTHA_annotation(source):
    """
    Gets the Annotation for EOPHTHA Data
    
    Input:
        source: string
            Source of the data: EOPHTHA
    Output:
        annotation: string
            Annotation of the data
    """
    
    for i in os.listdir("../../data/" + source):
        if i[:2] == 'MA':
            annotation = 'Microaneurysms'
        elif i[:2] == 'EX':
            annotation = 'Exudates'
        else:
            annotation = 'Healthy'
        print(annotation)
    return annotation