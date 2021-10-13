from dotenv import load_dotenv
import os


load_dotenv('.env')

class Config(object):
    
    KEY = os.getenv('GMAIL_KEY')