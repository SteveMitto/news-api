import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    API_KEY=os.environ.get('API_KEY')

class ProdConfig:
    pass

class DevConfig:
    DEBUG = True

config_options={
'production':ProdConfig,
'development':DevConfig
}
