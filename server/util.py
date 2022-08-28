import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(Location, Beds, Sq_feet, Baths):
    try:
        loc_index = __data_columns.index(Location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Beds
    x[1] = Sq_feet
    x[2] = Baths
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...Start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("./artifacts/Florida_Home_Prices_model.pickle","rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_estimated_price('Miami',3,1500,2))
    print(get_location_names())