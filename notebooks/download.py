import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
kaggle.api.authenticate()

kaggle.api.dataset_download_files("robikscube/hourly-energy-consumption", path='./input', unzip=True)
