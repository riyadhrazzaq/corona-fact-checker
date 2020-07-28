import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
IMAGE_UPLOADS = PROJECT_ROOT + "/files/"
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
DB_HOST = <CONNECTION URL OF MONGODB ATLAS>

DB_PORT = 27017
MISINFO_COLLECTION = 'misinfo_collection'
CACHE_COLLECTION = 'cache_collection'
BLACKLIST_COLLECTION = 'blacklist_collection'
USER_STUDY_COLLECTION = 'user_study'
DB_NAME = 'covid'

SIMILARITY_THRESHOLD = 0.1
NUMBER_OF_RESULT = 2

DICTIONARY = PROJECT_ROOT + "/current_dictionary.dict"
# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "covid19server"

# Secret key for signing cookies
SECRET_KEY = "covid19secret"
