"""Settings."""
from os.path import join, dirname, abspath
from configparser import ConfigParser

ROOT_DIR = dirname(dirname(abspath(__file__)))
UID = 'ophjlpahpchlmihnnnihgmmeilfjmjjc'
EXECUTABLE_PATH = join(ROOT_DIR, 'src/chromedriver')
EXTENSTION_PATH = join(ROOT_DIR, f'src/Extensions/{UID}/2.1.0_0.crx')

# credentials
config = ConfigParser()
config.read(join(ROOT_DIR, 'credentials.conf'))
EMAIL = config['main']['email']
PASSWORD = config['main']['password']


