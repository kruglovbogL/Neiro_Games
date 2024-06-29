from pathlib import Path

from ultralytics.data.utils import compress_one_image
from ultralytics.utils.downloads import zip_directory

# Define dataset directory
path = Path("Im_Trening")

# Optimize images in dataset (optional)
for f in path.rglob("*.jpg"):
    compress_one_image(f)

# Zip dataset into 'path/to/dataset.zip'
zip_directory(path)