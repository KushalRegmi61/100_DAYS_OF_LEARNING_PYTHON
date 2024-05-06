import os
from dotenv import load_dotenv, dotenv_values

config = dotenv_values(".env")
print(config)
print(config["my_email"])