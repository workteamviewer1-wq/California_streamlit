#import joblib,sklearn,numpy, pandas,streamlit


import streamlit as st

import numpy as np
import joblib as jb


obj = jb.load('california.joblib')
model= obj['model']
cols = obj['columns']


st.title('California app')
In = []


for i in cols:
    v= st.number_input(f'enter {i} value')
    In.append(v)


if st.button('click'):
    out = model.predict([In])
    st.success(out)


