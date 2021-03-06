import keras
import numpy as np
import sklearn.model_selection
import shogicam.data
from shogicam.constant import *

def load_traindata(data_dir, test_size=0.05):
    x_raw, y_raw = shogicam.data.load_data(data_dir)
    x_all, y_all = format_traindata(x_raw, y_raw)
    return sklearn.model_selection.train_test_split(x_all, y_all, test_size=test_size)

def load_traindata_nosplit(data_dir):
    x_raw, y_raw = shogicam.data.load_data(data_dir)
    x_all, y_all = format_traindata(x_raw, y_raw)
    return x_all, y_all

def format_traindata(x, y):
    x = x.reshape(x.shape[0], IMG_ROWS, IMG_COLS, 1)
    x = x.astype(np.float32)
    x /= 255
    y = keras.utils.to_categorical(y[:, 0], NUM_CLASSES)
    return x, y

def load_traindata_with_validation_board(data_dir, test_size=0.05):
    x_train, y_train = load_traindata_nosplit(data_dir)
    x_valid, y_valid = shogicam.data.load_validation_cells(data_dir + '/board', include_empty_cells=True)
    x_all = np.r_[x_train, x_valid]
    y_all = np.r_[y_train, y_valid]
    return sklearn.model_selection.train_test_split(x_all, y_all, test_size=test_size)