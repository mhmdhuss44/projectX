import os
from pathlib import Path

ABSOLUTE_PATH = Path(os.path.abspath(__file__)).parent
yaml_path= ABSOLUTE_PATH / "mail_server.yaml"
