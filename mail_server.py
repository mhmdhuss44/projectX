import yaml

import paths


class MailServer:

    def __init__(self):
        self.CONFIGS = None

    def load_mail_server(self):
        conf_yaml=paths.yaml_path
        if conf_yaml.exists():
            with open(file=conf_yaml, mode="r") as yaml_file:
                try:
                    self.CONFIGS = yaml.safe_load(stream=yaml_file.read())
                    print("Configuration yaml file loaded successfully.")
                except yaml.YAMLError as ex:
                    print(f"Failed to load Mail Server configuration file")
