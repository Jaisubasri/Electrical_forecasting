import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import time

st.set_page_config(layout="wide")

tab1,tab2,tab3=st.tabs(["Country Based" , "Product Based","Overall"])

with tab1:
    options = ['San Francisco','Los Angeles','New York City','Boston','Dallas','Seattle','Atlanta','Portland','Austin']
    
    def coun(country):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        country_data = data[data['Country'] == country]
        product_data = country_data.groupby('Products')['Quantities_Ordered'].mean().reset_index()
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Quantity of Products ordered in San Francisco</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        
        st.markdown("""<br><br>""",unsafe_allow_html=True)
        st.bar_chart(product_data, x='Products', y='Quantities_Ordered')
    
    def monthwise(country):
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Month-Wise Analysis</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
  
        st.markdown("<p style='text-align : none ; color : #FFFFFF; font-size:30px'>March &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; April", unsafe_allow_html=True)
        
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        data['Ordered_Date'] = pd.to_datetime(data['Ordered_Date']).dt.month.astype(str)
        
        months1 = ['3', '4']
        months2 = ['5', '6']
        
        product_data1 = data[(data['Country'] == country) & (data['Ordered_Date'].isin(months1))].groupby(['Products', 'Ordered_Date'])['Quantities_Ordered'].sum().reset_index()
        chart1 = alt.Chart(product_data1).mark_bar().encode(
            x=alt.X('Products:N', title='Product'),
            y=alt.Y('Quantities_Ordered:Q', title='Quantity Ordered'),
            column=alt.Column('Ordered_Date:N', title='Month'),
            color=alt.Color('Ordered_Date:N', legend=None)
            ).properties(
                width=200,
                height=300
                ).resolve_scale(
                    x='independent'
                    )
        
        product_data2 = data[(data['Country'] == country) & (data['Ordered_Date'].isin(months2))].groupby(['Products', 'Ordered_Date'])['Quantities_Ordered'].sum().reset_index()
        chart2 = alt.Chart(product_data2).mark_bar().encode(
            x=alt.X('Products:N', title='Product'),
            y=alt.Y('Quantities_Ordered:Q', title='Quantity Ordered'),
            column=alt.Column('Ordered_Date:N', title='Month'),
            color=alt.Color('Ordered_Date:N', legend=None)
            ).properties(
                width=200,
                height=300
                ).resolve_scale(
                    x='independent'
                    )
        col1,col2=st.columns(2)
        with col1:
            st.altair_chart(chart1, use_container_width=True)
        
        st.markdown("<p style='text-align : none ; color : #FFFFFF; font-size:30px'>May &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; June", unsafe_allow_html=True)
        
        col3,col4=st.columns(2)
        
        with col3:
            st.altair_chart(chart2, use_container_width=True)
    
    selected_option = st.selectbox('Select an option', options)
    
    if(selected_option == 'San Francisco'):
        
        coun(" San Francisco")
        
        st.write("## Product with Highest Quantity : AAA Batteries (4-pack)")
        
        monthwise(" San Francisco")
        
    if(selected_option == 'Los Angeles'):
        
        coun(" Los Angeles")
        
        st.write("## Product with Highest Quantity : AAA Batteries (4-pack)")

        monthwise(" Los Angeles")
    
    if(selected_option == 'New York City'):
        
        coun(" New York City")
        
        st.write("## Product with Highest Quantity : AA Batteries (4-pack)")

        monthwise(" New York City")      
        
    if(selected_option == 'Boston'):
        
        coun(" Boston") 
        
        st.write("## Product with Highest Quantity : AAA Batteries (4-pack)")

        monthwise(" Boston")   
        
    if(selected_option == 'Dallas'):
        
        coun(" Dallas")
        
        st.write("## Product with Highest Quantity : AAA Batteries (4-pack)")

        monthwise(" Dallas")      
       
    if(selected_option == 'Seattle'):
        
        coun(" Seattle")
        
        st.write("## Product with Highest Quantity : AAA Batteries (4-pack)")

        monthwise(" Seattle")
    
    if(selected_option == 'Atlanta'):
        
        coun(" Atlanta")
        
        st.write("## Product with Highest Quantity : AA Batteries (4-pack)")

        monthwise(" Atlanta")
   
    if(selected_option == 'Portland'):
        
        coun(" Portland")
        
        st.write("## Product with Highest Quantity : AA Batteries (4-pack)")

        monthwise(" Portland")
       
    if(selected_option == 'Austin'):
        
        coun(" Austin")
        
        st.write("## Product with Highest Quantity : AAA Batteries (4-pack)")

        monthwise(" Austin")
        
with tab2:
    
    def pro(product):
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        product_data = data[data['Products'] == product]
        country_data = product_data.groupby('Country')['Quantities_Ordered'].mean().reset_index()
        st.bar_chart(country_data, x='Country', y='Quantities_Ordered')
    
    def monthwise(product):
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Month-Wise Analysis</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
  
        st.markdown("<p style='text-align : none ; color : #FFFFFF; font-size:30px'>March &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; April", unsafe_allow_html=True)
        
        data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')
        data['Ordered_Date'] = pd.to_datetime(data['Ordered_Date']).dt.month.astype(str)
        
        months1 = ['3', '4']
        months2 = ['5', '6']
        
        product_data1 = data[(data['Products'] == product) & (data['Ordered_Date'].isin(months1))].groupby(['Country', 'Ordered_Date'])['Quantities_Ordered'].sum().reset_index()
        chart1 = alt.Chart(product_data1).mark_bar().encode(
            x=alt.X('Country:N', title='Country'),
            y=alt.Y('Quantities_Ordered:Q', title='Quantity Ordered'),
            column=alt.Column('Ordered_Date:N', title='Month'),
            color=alt.Color('Ordered_Date:N', legend=None)
            ).properties(
                width=200,
                height=300
                ).resolve_scale(
                    x='independent'
                    )
        
        product_data2 = data[(data['Products'] == product) & (data['Ordered_Date'].isin(months2))].groupby(['Country', 'Ordered_Date'])['Quantities_Ordered'].sum().reset_index()
        chart2 = alt.Chart(product_data2).mark_bar().encode(
            x=alt.X('Country:N', title='Country'),
            y=alt.Y('Quantities_Ordered:Q', title='Quantity Ordered'),
            column=alt.Column('Ordered_Date:N', title='Month'),
            color=alt.Color('Ordered_Date:N', legend=None)
            ).properties(
                width=200,
                height=300
                ).resolve_scale(
                    x='independent'
                    )
        col1,col2=st.columns(2)
        with col1:
            st.altair_chart(chart1, use_container_width=True)
        
        st.markdown("<p style='text-align : none ; color : #FFFFFF; font-size:30px'>May &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; June", unsafe_allow_html=True)
        
        col3,col4=st.columns(2)
        
        with col3:
            st.altair_chart(chart2, use_container_width=True)
    options = ["Monitor","Headphone","TV","Phone","Dryer","Washing Machine","Charger","Laptop"]
    selected_option = st.selectbox('Select an option', options)
    
    if(selected_option == "Monitor"):
        with st.spinner('Processing'):
            time.sleep(7)
            
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>20in Monitor</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("20in Monitor")
        monthwise("20in Monitor")
            
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>27in 4K Gaming Monitor</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("27in 4K Gaming Monitor")
        monthwise("27in 4K Gaming Monitor")
            
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>27in FHD Monitor</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("27in FHD Monitor")
        monthwise("27in FHD Monitor")
            
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>34in Ultrawide Monitor</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        pro("34in Ultrawide Monitor")
        monthwise("34in Ultrawide Monitor")
    
    if(selected_option == "Headphone"):        
        with st.spinner('Processing'):
            time.sleep(7)
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Bose SoundSport Headphones</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("Bose SoundSport Headphones")
        monthwise("Bose SoundSport Headphones")
            
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Apple Airpods Headphones</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("Apple Airpods Headphones")
        monthwise("Apple Airpods Headphones")
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Wired Headphones</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("Wired Headphones")
        monthwise("Wired Headphones")
        
    if(selected_option == "TV"):
        with st.spinner('Processing'):
            time.sleep(7)
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Flatscreen TV</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("Flatscreen TV")
        monthwise("Flatscreen TV")
   
    if(selected_option == "Phone"):
        with st.spinner('Processing'):
            time.sleep(7)
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Google Phone</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("Google Phone")
        monthwise("Google Phone")
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>iPhone</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("iPhone")
        monthwise("iPhone")


    if(selected_option == "Dryer"):
        with st.spinner('Processing'):
            time.sleep(7)
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>LG Dryer</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("LG Dryer")
        monthwise("LG Dryer")

    if(selected_option == "Washing Machine"):
        with st.spinner('Processing'):
            time.sleep(7)
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>LG Washing Machine</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("LG Washing Machine")
        monthwise("LG Washing Machine")
        
    if(selected_option == "Charger"):
        with st.spinner('Processing'):
            time.sleep(7)
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Lightning Charging Cable</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("Lightning Charging Cable")
        monthwise("Lightning Charging Cable")
   
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>USB-C Charging Cable</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("USB-C Charging Cable")
        monthwise("USB-C Charging Cable")
   
    if(selected_option == "Laptop"):
        with st.spinner('Processing'):
            time.sleep(7)
        
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>Macbook Pro Laptop</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("Macbook Pro Laptop")
        monthwise("Macbook Pro Laptop")

        st.markdown("<br><hr><br>", unsafe_allow_html=True)
        st.markdown("""<html>
						<head>
							<title>My Title</title>
							<style>
								body {
									display: flex;
									flex-direction: column;
									align-items: center;
									justify-content: center;
									height: 100vh;
									margin: 0;
									text-align:center;
								}
							</style>
						</head>
						<body>
							<h1>ThinkPad Laptop</h1>
						</body>
						</html>
					""",unsafe_allow_html=True)
        st.markdown("<br><hr><br>", unsafe_allow_html=True)
            
        pro("ThinkPad Laptop")
        monthwise("ThinkPad Laptop")
   
with tab3:
    power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=7b84957d-a596-46d1-9697-65971e88ca5b&autoAuth=true&ctid=9d049b1f-0aea-4675-a840-732bbb1e6f9c"
    embedded_url = power_bi_url + "&toolbarHidden=true&navContentPaneEnabled=false&filterPaneEnabled=false"
    st.markdown(f'<div style="display: flex; justify-content: center;"><iframe width="1000" height="541.25" src="{embedded_url}" frameborder="0" allowFullScreen="true"></iframe></div>', unsafe_allow_html=True)
    
    st.markdown("<br><hr><br>", unsafe_allow_html=True)
    
    power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=68095cad-6169-47ad-a895-35839a304c94&autoAuth=true&ctid=9d049b1f-0aea-4675-a840-732bbb1e6f9c"
    embedded_url = power_bi_url + "&toolbarHidden=true&navContentPaneEnabled=false&filterPaneEnabled=false"
    st.markdown(f'<div style="display: flex; justify-content: center;"><iframe width="1000" height="541.25" src="{embedded_url}" frameborder="0" allowFullScreen="true"></iframe></div>', unsafe_allow_html=True)
    
    st.markdown("<br><hr><br>", unsafe_allow_html=True)
    
    power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=d1a7a2af-e694-457f-93a5-86657111b993&autoAuth=true&ctid=9d049b1f-0aea-4675-a840-732bbb1e6f9c"
    embedded_url = power_bi_url + "&toolbarHidden=true&navContentPaneEnabled=false&filterPaneEnabled=false"
    st.markdown(f'<div style="display: flex; justify-content: center;"><iframe width="1000" height="541.25" src="{embedded_url}" frameborder="0" allowFullScreen="true"></iframe></div>', unsafe_allow_html=True)


