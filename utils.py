#!/usr/bin/env python
# coding: utf-8

# In[20]:


import json
import pickle
import numpy as np


# In[27]:


__datacolumn=None
__location=None
__model=None

def estimate_price(location,sqft,bhk,bath):
    try:
        loc_ind=__datacolumn.index(location.lower())
    except:
        loc_ind=-1
    x=np.zeros(len(__datacolumn))
    x[0]=sqft
    x[1]=bhk
    x[2]=bath
    
    if loc_ind>=0:
        x[loc_ind]=1
    return round(__model.predict([x])[0],2)
def get_location_name():
    return __location
def load_data():
    global __datacolumn
    global __location
    global __model
    
    with open("columns.json","r") as f:
        __datacolumn=json.load(f)["data_columns"]
        __location=__datacolumn[3:]
    with open("bangalore_home_prediction_model.pickle","rb") as f:
        __model=pickle.load(f)


# In[29]:


if __name__=="__main__":
    load_data()
    print(get_location_name())
    print(estimate_price('1st phase jp nagar',1000,3,2))
    print(estimate_price('1st phase jp nagar',1000,2,2))
    

