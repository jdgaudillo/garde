import warnings
warnings.filterwarnings("ignore")

import os
import csv
import shutil
from zipfile import ZipFile
import glob


def clean_MESSIDOR_dataset():
	data_dir = "../data/MESSIDOR"

	for base in os.listdir(data_dir):
		if base.endswith(".zip"):
			print(">>>>>>>> ", base)
			base_dir = os.path.join(data_dir, base)

			with ZipFile(base_dir, "r") as zip:
				zip.extractall(data_dir)

			base_dir = base_dir.replace(".zip", "/")
			image_files = os.listdir(base_dir)
			renamed_files = [base + "_" + image_file for image_file in image_files]

			for i, file in enumerate(image_files):
				if file.endswith(".tif"):
					os.rename(os.path.join(base_dir, file), os.path.join(data_dir, renamed_files[i]))

				if file.endswith(".xls"):
					shutil.move(os.path.join(base_dir, file), "../data/annotation/MESSIDOR/")

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

def main():
	clean_MESSIDOR_dataset()
	#clean_MESSIDOR_annotation()


if __name__ == "__main__":
	main()