# Saving model to current directory
# Pickle serializes objects so they can be saved to a file, and loaded in a program again later on.


import pickle

#name the file in which model will be saved

name="solar_pickle_model.pkl"

#save your model in that file

pickle.dump(model, open(name, 'wb'))

#load back the model
loaded_model = pickle.load(open(filename, 'rb'))
