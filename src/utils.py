import os
import configparser


def load_openai():
    config_parser = configparser.ConfigParser()
    config_parser.read_file(open(r"../config.txt"))
    OPENAI_API_KEY = config_parser.get("openai", "OPENAI_API_KEY")
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    return OPENAI_API_KEY