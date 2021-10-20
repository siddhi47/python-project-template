import yaml
import os
from utils.utils import ROOT_DIR


class Variables:
    def __init__(self) -> None:
        with open(os.path.join(ROOT_DIR,"config","config.yaml"), "r") as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        database_credentials = config['database']
        self.user = database_credentials['user']
        self.password = database_credentials['password']
        self.host = database_credentials['host']

        logging_config = config['logging']
        self.log_level = logging_config['log_level']

vars = Variables()