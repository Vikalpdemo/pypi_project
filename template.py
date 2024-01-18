import os 
from pathlib import Path

package_name="mongodb_connect"

list_of_files=[
     "github/workflows/ci.yaml",
     "src/__init__.py",
     f"src/{package_name}/__init__.py",
     f"src/{package_name}/mongo_crud.py",
     "tests/__init__.py",
     "tests/unit/unit.py",
     "tests/integration/__init__.py",
     "tests/integration/init.py",
     "requirements.txt",
     "requirements_dev.txt",
     "setup.py",
     "setup.cfg",
     "pyproject.toml",
     "tox.ini",
     "experiment/experiment.ipynb",
     
]

for files in list_of_files:
     filepath=Path(files)
     filedir,filename=os.path.split(filepath)
     if filedir!="":
          os.makedirs(filedir,exist_ok=True)
          # logging.info(f"Creating directory:{filedir} for file :{filename}")
     if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
          with open(filepath,"w") as f:
               pass
     