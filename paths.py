import os
from pathlib import Path

ABSOLUTE_PATH = Path(os.path.abspath(__file__)).parent
YAML_PATH= ABSOLUTE_PATH / "mail_server.yaml"
JSON_PATH= ABSOLUTE_PATH / "jobs.json"


# This class imports the os and Path modules from the pathlib library. It then defines a constant
# named ABSOLUTE_PATH which is set to the parent directory of the file where this code is located,
# using the os.path.abspath(__file__) method.
#
# It then creates a variable yaml_path which is set to the file named mail_server.yaml
# located in the parent directory of the file where this code is located, using the / operator
# to join the two paths.
#
# This file path is used in the MailServer class to load the configurations of the mail server.
# This is done by using the paths.yaml_path in the load_mail_server method, if the file exists it
# will load the configuration yaml file

