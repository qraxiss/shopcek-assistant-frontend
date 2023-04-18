# env files
from dotenv import load_dotenv
load_dotenv()


from os import environ as config, getcwd

PORT = int(config['PORT'])
PATH = getcwd()
IMG_PATH = f'{PATH}/views/img'
API_URI = config['API_URI']