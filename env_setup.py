import os
from dotenv import load_dotenv
load_dotenv()

HOMEPAGE_URL = os.getenv('HOMEPAGE_URL')
QUALITY_ASSURANCE_URL = os.getenv('QUALITY_ASSURANCE_URL')
FULL_PATH = os.path.dirname(os.path.realpath(__file__))
