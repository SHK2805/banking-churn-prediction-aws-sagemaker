import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')


def create_directory(path: Path):
    if not path.exists():
        os.makedirs(path, exist_ok=True)
        logging.info(f"Creating directory: {path}")
    else:
        logging.info(f"Directory {path} already exists")


def create_file(filepath: Path):
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath.name} already exists")


def create_project_structure(project_name: str) -> bool:
    try:
        data_folder_name: str = "data"
        list_of_files = [
            # general files
            "template.py",
            "setup.py",
            ".env",
            ".gitignore",
            "requirements.txt",
            "README.md",
            # data
            f"{data_folder_name}/raw",
            # logs
            f"logs",
            # notebooks
            f"notebooks/churn.ipynb",
            # clean
            "clean.py",
        ]

        for filepath in list_of_files:
            filepath = Path(filepath)
            filedir = filepath.parent

            # Ensure Dockerfile, docker-compose.yml and .dockerignore are treated as files
            if filepath.name in ['Dockerfile',
                                 '.dockerignore',
                                 'docker-compose.yml',
                                 '.env']:
                create_file(filepath)
                continue

            # Create directories
            create_directory(filedir)

            # Create files if they do not exist or are empty
            if filepath.suffix:  # Check if it's a file (has a suffix)
                create_file(filepath)
            else:
                create_directory(filepath)
    except Exception as e:
        logging.error(f"Error in creating project structure: {e}")
        return False
    return True


if __name__ == "__main__":
    ml_project_name = "bank-churn-prediction"
    create_project_structure(ml_project_name)
    logging.info(f"Project structure created for {ml_project_name}")