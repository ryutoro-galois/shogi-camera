from ._util import save_model
from ._purple import learn as purple
from ._purple2 import learn as purple2
from ._blue import learn as blue

models = { "purple": purple, "purple2": purple2, "blue": blue }

def learn_model(name, data_dir, verbose=True):
   return models[name](data_dir, verbose)
