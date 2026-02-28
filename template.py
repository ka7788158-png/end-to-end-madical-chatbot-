# by using this we are going to manage our project folder structure no need to do it one by one 

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

list_of_files = [
    "src/__init__.py", # src will create a folder 
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath) # path will take care wether its for window or mac
    filedir , filename = os.path.split(filepath) # split file and folder name

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")

