import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from scipy import stats

options = ["Monitor","Headphone","TV","Phone","Dryer","Washing Machine","Charger","Laptop"]
selected_option = st.selectbox('Select an option', options)

if(selected_option == "Monitor"):
    
    value = st.slider("",6 , 12)
    
    if(value == 6):
        mon = '06'
    if(value == 7):
        mon = '07'
    if(value == 8):
        mon = '08'
    if(value == 9):
        mon = '09'
    if(value == 10):
        mon = '10'
    if(value == 11):
        mon = '11'
    if(value == 12):
        mon = '12'
    
    def moni(product):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        rows,col=data.shape
        for i in range(0,rows):
            data.loc[i,'Ordered_Date']=data.loc[i,'Ordered_Date'].split('-',1).pop(0)
        country_data = data[data['Ordered_Date'] == mon ]
        data['Ordered_Date'] = [int(x) for x in data['Ordered_Date']]
        WH  = {3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 }
        for i in range(len(data)) : 
            if(data.iloc[i]['Products'] == product):
                WH[int(str(data.iloc[i]['Ordered_Date']).split('_')[0])] += data.iloc[i]['Quantities_Ordered']
    
        k1 = list(WH.keys())
        k2 = list(WH.values())
        k1 = np.array(k1).reshape((-1, 1))
        k2 = np.array(k2).reshape((-1, 1))
        model = LinearRegression()
        model.fit(k1, k2)
    
        x = [value]
        x = np.array(x).reshape((-1, 1))
    
        ypred = model.predict(x)
        
        return ypred[0][0]
        
    sum = round(moni('20in Monitor') + moni('27in 4K Gaming Monitor') + moni('27in FHD Monitor') + moni('34in Ultrawide Monitor') , 0)
    
    st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Predicted Production</h1><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {sum}</h1><br><hr>", unsafe_allow_html=True)
 
if(selected_option == "Headphone"):
    
    value = st.slider("",6 , 12)
    
    if(value == 6):
        mon = '06'
    if(value == 7):
        mon = '07'
    if(value == 8):
        mon = '08'
    if(value == 9):
        mon = '09'
    if(value == 10):
        mon = '10'
    if(value == 11):
        mon = '11'
    if(value == 12):
        mon = '12'
    
    def moni(product):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        rows,col=data.shape
        for i in range(0,rows):
            data.loc[i,'Ordered_Date']=data.loc[i,'Ordered_Date'].split('-',1).pop(0)
        country_data = data[data['Ordered_Date'] == mon ]
        data['Ordered_Date'] = [int(x) for x in data['Ordered_Date']]
        WH  = {3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 }
        for i in range(len(data)) : 
            if(data.iloc[i]['Products'] == product):
                WH[int(str(data.iloc[i]['Ordered_Date']).split('_')[0])] += data.iloc[i]['Quantities_Ordered']
    
        k1 = list(WH.keys())
        k2 = list(WH.values())
        k1 = np.array(k1).reshape((-1, 1))
        k2 = np.array(k2).reshape((-1, 1))
        model = LinearRegression()
        model.fit(k1, k2)
    
        x = [value]
        x = np.array(x).reshape((-1, 1))
    
        ypred = model.predict(x)
        
        return ypred[0][0]
        
    sum = round(moni('Bose SoundSport Headphones') + moni('Apple Airpods Headphones') + moni('Wired Headphones') , 0)
    
    st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Predicted Production</h1><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {sum}</h1><br><hr>", unsafe_allow_html=True)          
    
if(selected_option == "TV"):
    
    value = st.slider("",6 , 12)
    
    if(value == 6):
        mon = '06'
    if(value == 7):
        mon = '07'
    if(value == 8):
        mon = '08'
    if(value == 9):
        mon = '09'
    if(value == 10):
        mon = '10'
    if(value == 11):
        mon = '11'
    if(value == 12):
        mon = '12'
    
    def moni(product):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        rows,col=data.shape
        for i in range(0,rows):
            data.loc[i,'Ordered_Date']=data.loc[i,'Ordered_Date'].split('-',1).pop(0)
        country_data = data[data['Ordered_Date'] == mon ]
        data['Ordered_Date'] = [int(x) for x in data['Ordered_Date']]
        WH  = {3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 }
        for i in range(len(data)) : 
            if(data.iloc[i]['Products'] == product):
                WH[int(str(data.iloc[i]['Ordered_Date']).split('_')[0])] += data.iloc[i]['Quantities_Ordered']
    
        k1 = list(WH.keys())
        k2 = list(WH.values())
        k1 = np.array(k1).reshape((-1, 1))
        k2 = np.array(k2).reshape((-1, 1))
        model = LinearRegression()
        model.fit(k1, k2)
    
        x = [value]
        x = np.array(x).reshape((-1, 1))
    
        ypred = model.predict(x)
        
        return ypred[0][0]
        
    sum = round(moni('Flatscreen TV') , 0)
    
    st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Predicted Production</h1><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {sum}</h1><br><hr>", unsafe_allow_html=True)

if(selected_option == "Phone"):
    
    value = st.slider("",6 , 12)
    
    if(value == 6):
        mon = '06'
    if(value == 7):
        mon = '07'
    if(value == 8):
        mon = '08'
    if(value == 9):
        mon = '09'
    if(value == 10):
        mon = '10'
    if(value == 11):
        mon = '11'
    if(value == 12):
        mon = '12'
    
    def moni(product):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        rows,col=data.shape
        for i in range(0,rows):
            data.loc[i,'Ordered_Date']=data.loc[i,'Ordered_Date'].split('-',1).pop(0)
        country_data = data[data['Ordered_Date'] == mon ]
        data['Ordered_Date'] = [int(x) for x in data['Ordered_Date']]
        WH  = {3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 }
        for i in range(len(data)) : 
            if(data.iloc[i]['Products'] == product):
                WH[int(str(data.iloc[i]['Ordered_Date']).split('_')[0])] += data.iloc[i]['Quantities_Ordered']
    
        k1 = list(WH.keys())
        k2 = list(WH.values())
        k1 = np.array(k1).reshape((-1, 1))
        k2 = np.array(k2).reshape((-1, 1))
        model = LinearRegression()
        model.fit(k1, k2)
    
        x = [value]
        x = np.array(x).reshape((-1, 1))
    
        ypred = model.predict(x)
        
        return ypred[0][0]
        
    sum = round(moni('Google Phone') + moni('iPhone') , 0)
    
    st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Predicted Production</h1><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {sum}</h1><br><hr>", unsafe_allow_html=True)
    
if(selected_option == "Dryer"):
    
    value = st.slider("",6 , 12)
    
    if(value == 6):
        mon = '06'
    if(value == 7):
        mon = '07'
    if(value == 8):
        mon = '08'
    if(value == 9):
        mon = '09'
    if(value == 10):
        mon = '10'
    if(value == 11):
        mon = '11'
    if(value == 12):
        mon = '12'
    
    def moni(product):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        rows,col=data.shape
        for i in range(0,rows):
            data.loc[i,'Ordered_Date']=data.loc[i,'Ordered_Date'].split('-',1).pop(0)
        country_data = data[data['Ordered_Date'] == mon ]
        data['Ordered_Date'] = [int(x) for x in data['Ordered_Date']]
        WH  = {3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 }
        for i in range(len(data)) : 
            if(data.iloc[i]['Products'] == product):
                WH[int(str(data.iloc[i]['Ordered_Date']).split('_')[0])] += data.iloc[i]['Quantities_Ordered']
    
        k1 = list(WH.keys())
        k2 = list(WH.values())
        k1 = np.array(k1).reshape((-1, 1))
        k2 = np.array(k2).reshape((-1, 1))
        model = LinearRegression()
        model.fit(k1, k2)
    
        x = [value]
        x = np.array(x).reshape((-1, 1))
    
        ypred = model.predict(x)
        
        return ypred[0][0]
        
    sum = round(moni('LG Dryer') , 0)
    
    st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Predicted Production</h1><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {sum}</h1><br><hr>", unsafe_allow_html=True)

if(selected_option == "Washing Machine"):
    
    value = st.slider("",6 , 12)
    
    if(value == 6):
        mon = '06'
    if(value == 7):
        mon = '07'
    if(value == 8):
        mon = '08'
    if(value == 9):
        mon = '09'
    if(value == 10):
        mon = '10'
    if(value == 11):
        mon = '11'
    if(value == 12):
        mon = '12'
    
    def moni(product):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        rows,col=data.shape
        for i in range(0,rows):
            data.loc[i,'Ordered_Date']=data.loc[i,'Ordered_Date'].split('-',1).pop(0)
        country_data = data[data['Ordered_Date'] == mon ]
        data['Ordered_Date'] = [int(x) for x in data['Ordered_Date']]
        WH  = {3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 }
        for i in range(len(data)) : 
            if(data.iloc[i]['Products'] == product):
                WH[int(str(data.iloc[i]['Ordered_Date']).split('_')[0])] += data.iloc[i]['Quantities_Ordered']
    
        k1 = list(WH.keys())
        k2 = list(WH.values())
        k1 = np.array(k1).reshape((-1, 1))
        k2 = np.array(k2).reshape((-1, 1))
        model = LinearRegression()
        model.fit(k1, k2)
    
        x = [value]
        x = np.array(x).reshape((-1, 1))
    
        ypred = model.predict(x)
        
        return ypred[0][0]
        
    sum = round(moni('LG Washing Machine') , 0)
    
    st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Predicted Production</h1><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {sum}</h1><br><hr>", unsafe_allow_html=True)
    
if(selected_option == "Charger"):
    
    value = st.slider("",6 , 12)
    
    if(value == 6):
        mon = '06'
    if(value == 7):
        mon = '07'
    if(value == 8):
        mon = '08'
    if(value == 9):
        mon = '09'
    if(value == 10):
        mon = '10'
    if(value == 11):
        mon = '11'
    if(value == 12):
        mon = '12'
    
    def moni(product):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        rows,col=data.shape
        for i in range(0,rows):
            data.loc[i,'Ordered_Date']=data.loc[i,'Ordered_Date'].split('-',1).pop(0)
        country_data = data[data['Ordered_Date'] == mon ]
        data['Ordered_Date'] = [int(x) for x in data['Ordered_Date']]
        WH  = {3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 }
        for i in range(len(data)) : 
            if(data.iloc[i]['Products'] == product):
                WH[int(str(data.iloc[i]['Ordered_Date']).split('_')[0])] += data.iloc[i]['Quantities_Ordered']
    
        k1 = list(WH.keys())
        k2 = list(WH.values())
        k1 = np.array(k1).reshape((-1, 1))
        k2 = np.array(k2).reshape((-1, 1))
        model = LinearRegression()
        model.fit(k1, k2)
    
        x = [value]
        x = np.array(x).reshape((-1, 1))
    
        ypred = model.predict(x)
        
        return ypred[0][0]
        
    sum = round(moni('Lightning Charging Cable') + moni('USB-C Charging Cable') , 0)
    
    st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Predicted Production</h1><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {sum}</h1><br><hr>", unsafe_allow_html=True)
    
if(selected_option == "Laptop"):
    
    value = st.slider("",6 , 12)
    
    if(value == 6):
        mon = '06'
    if(value == 7):
        mon = '07'
    if(value == 8):
        mon = '08'
    if(value == 9):
        mon = '09'
    if(value == 10):
        mon = '10'
    if(value == 11):
        mon = '11'
    if(value == 12):
        mon = '12'
    
    def moni(product):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        rows,col=data.shape
        for i in range(0,rows):
            data.loc[i,'Ordered_Date']=data.loc[i,'Ordered_Date'].split('-',1).pop(0)
        country_data = data[data['Ordered_Date'] == mon ]
        data['Ordered_Date'] = [int(x) for x in data['Ordered_Date']]
        WH  = {3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 }
        for i in range(len(data)) : 
            if(data.iloc[i]['Products'] == product):
                WH[int(str(data.iloc[i]['Ordered_Date']).split('_')[0])] += data.iloc[i]['Quantities_Ordered']
    
        k1 = list(WH.keys())
        k2 = list(WH.values())
        k1 = np.array(k1).reshape((-1, 1))
        k2 = np.array(k2).reshape((-1, 1))
        model = LinearRegression()
        model.fit(k1, k2)
    
        x = [value]
        x = np.array(x).reshape((-1, 1))
    
        ypred = model.predict(x)
        
        return ypred[0][0]
        
    sum = round(moni('Macbook Pro Laptop') + moni('ThinkPad Laptop') , 0)
    
    st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Predicted Production</h1><br>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {sum}</h1><br><hr>", unsafe_allow_html=True)
    

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')

max_product = data.loc[data['Quantities_Ordered'].idxmax(), 'Products']
min_product = data.loc[data['Quantities_Ordered'].idxmin(), 'Products']


st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Top Sold Product</h1><br>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {max_product}</h1><br><hr>", unsafe_allow_html=True) 

st.markdown("<h1 style='text-align: center; color : white; font-size:45px'>Least Sold Product</h1><br>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:40px'> {min_product}</h1><br><hr>", unsafe_allow_html=True) 
