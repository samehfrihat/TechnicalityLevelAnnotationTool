import os

# Local configurations
_CURRENT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
GERMAN_ABSTRACTS_PATH = os.path.join(_CURRENT_FILE_PATH, "static/data/germanAbstracts.csv")

# Database related configurations
#CONNECTION_STRING = os.environ.get("DB", 'localhost:27017')
#CONNECTION_STRING = os.environ.get("DB", 'mongodb://root:secret@sally.is.inf.uni-due.de:27017')
CONNECTION_STRING = os.environ.get("DB", 'mongodb://root:rootPasswordXXX@ariadne.is.inf.uni-due.de:27017')

# API related configurations
PORT = os.environ.get("PORT", 8787)

# Annotation configurations
NO_OF_ANNOTATION_PER_DOC = os.environ.get("APD", 3)  # annotation per document

LANGUAGES = {
    'en': 'English',
    'de': 'Deutsch'
}
