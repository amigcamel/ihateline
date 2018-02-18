"""Settings."""
from os.path import join, dirname, abspath
from configparser import ConfigParser

ROOT_DIR = dirname(dirname(abspath(__file__)))
UID = 'ophjlpahpchlmihnnnihgmmeilfjmjjc'
COMMAND_EXECUTOR = 'http://chrome:4444/wd/hub'
EXTENSTION_PATH = join(ROOT_DIR, f'src/Extensions/{UID}/2.1.0_0.crx')

# session info cache
SESSION_CACHE_PATH = join(ROOT_DIR, '.session')

# credentials
config = ConfigParser()
config.read(join(ROOT_DIR, 'credentials.conf'))
EMAIL = config['main']['email']
PASSWORD = config['main']['password']
