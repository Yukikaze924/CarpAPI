from models.model import Logo


# Basic configurations
BASE_URL = '0.0.0.0'
BASE_PORT = 8000

# Database configuration
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'carp'

# Miscellaneous settings/preferences
"""
You have multiple choices for logo,
- Logo.Default
- Logo.Ukraine
- Logo.Russia
- Logo.Rainbow
"""
LOGO = Logo.Rainbow
LAUNCH_AUDIO = 'assets/audios/launched.mp3'