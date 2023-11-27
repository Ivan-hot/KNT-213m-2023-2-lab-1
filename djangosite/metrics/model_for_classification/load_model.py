from .constants import *
from joblib import load
from os.path import isfile
from .make_model import make_model


def load_model():
    if not isfile(file_model):
        make_model()
    model = load(file_model)
    return model
