import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="ml_project"

list_of_file=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py"
    f"src/{project_name}/logger.py"
    f"src/{project_name}/utils.py"
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "main.py"
]

for filepath in list_of_file:
    filepath=Path(filepath)
    filedr,filename=os.path.split(filepath)

    if filedr != "":
        os.makedirs(filedr,exist_ok=True)
        logging.info(f"creating directory :{filedr} for the file name {filename}")

    if(not os.path.exists(filepath) or os.path.getsize(filepath)==0):
            with open(filepath,"w") as f:
                pass
                logging.info(f"creating empty file:{filepath}")

    else:
        logging.info(f"{filename} already exist")