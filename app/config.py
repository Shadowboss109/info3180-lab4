import os
import sys

from dotenv import load_dotenv
UPLOAD_FOLDER = './uploads'
path_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
load_dotenv()


class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'Password123')
    UPLOAD_FOLDER= os.path.join(path_dir, 'uploads')