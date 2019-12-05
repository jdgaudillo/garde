import warnings
warnings.filterwarnings("ignore")

from data_cleaning.main import main


if __name__ == "__main__":
	source = "HRF"

	main(source)
