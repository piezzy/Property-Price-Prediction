import pickle
import json
import numpy as np
import warnings
warnings.filterwarnings("ignore")


__locations = None
__data_columns = None
__model = None

def estimate_price(location, sqft, bhk, bath):
    try:
        locIndex = __data_columns.index(location.lower())
    except:
        locIndex = -1 
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if locIndex >= 0:
        x[locIndex] = 1
    
    return round(__model.predict([x])[0], 2)
    
def home():
    return __locations

def loadArti():
    print('loading artifacts...start')
    global __data_columns
    global __locations
    
    with open('server/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        
    global __model    
    with open('server/banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading artifacts...done')
        
if __name__ == '__main__':
    loadArti()
    print(home())
    print(estimate_price('1st Phase JP Nagar', 1000, 3, 3))