import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED BRAND FOR WIRED HEARPHONE </h1>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""<div style="background-color: #F8FF1F;"><h1 style='text-align: center; color : #000000; font-size:65px'>Realme </h1></div>""", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

images = ["https://cdn3.mydukaan.io/app/image/700x700/?url=https://projecteagle.s3.ap-south-1.amazonaws.com/images/35073b0e-e519-4d5a-b125-d7a38f729ab7.jpg","https://i0.wp.com/m.media-amazon.com/images/S/aplus-media/vc/f818212f-acf8-4775-b63b-a8a7f5f9e26b.__CR0,0,300,300_PT0_SX300_V1___.jpg?ssl=1","https://static.c.realme.com/IN/thread/1164154289317216256.jpg"]
image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:2000px; height:550px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""<html>
  <head>
    <title>About Realme</title>
    <style>
      /* Style the header */
      header {
        background-color: #222;
        padding: 20px;
        text-align: center;
        color: white;
      }
      /* Style the container */
      .container {
        margin: 50px;
      }
      /* Style the section */
      section {
        margin: 20px;
        padding: 20px;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>About Realme</h1>
    </header>
    <div class="container">
      <section>
        <h2>Our Histroy</h2>
        <p>
          Realme is a smartphone brand that was established in May 2018 as a subsidiary of 
          Oppo, another Chinese smartphone manufacturer. Realme primarily focuses on producing 
          budget and mid-range smartphones that offer competitive features and specifications.
        </p>
        <p>
        The company has rapidly expanded since its inception and is now available in many 
        countries around the world, including India, China, Southeast Asia, Europe, and more 
        recently, the United States. Realme has also diversified its product portfolio to include 
        other consumer electronics such as smart TVs, smartwatches, earphones, and more.
        </p>
        <p>
        In addition to their product offerings, Realme has also been active in promoting and 
        sponsoring esports events and tournaments, which has helped to increase their brand 
        recognition among younger consumers.
        </p>
        <p>
        Overall, Realme has quickly become a significant player in the smartphone market and 
        has gained a reputation for producing high-quality devices at affordable prices. 
        </p>
      </section>
      <section>
        <h2>Our Products</h2>
        <p>Realme offers a variety of products, including:</p>
        <ul>
          <p>Earphones</p>
          <p>Phone</p>
          <p>Power banks<p/>
          <p>Chargers<p/>
          <p>Selfie sticks</p>
          <p>Smartwatches</p>
          <p>and more</p>
        </ul>
      </section>
    </div>
  </body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center;'>
        <img src="https://static.c.realme.com/IN/thread/1303184915067568128.gif" 
             alt="Animated GIF" 
             width="1300" 
             height="600">
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""<html>
<head>
	<title>Product Details</title>
	<style>
		.container {
			text-align: center;
		}
	</style>
</head>
<body>
	<div class="container">
		<h1>Product Detail</h1>
	</div>
</body>
</html>""",unsafe_allow_html=True)


st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""<table>
  <tr>
    <td><strong>Brand</strong></td>
    <td>realme</td>
  </tr>
  <tr>
    <td><strong>Manufacturer</strong></td>
    <td>realme, Jiangxi Risound Electronics Co.,Ltd. No.271, Innovation Avenue, China</td>
  </tr>
  <tr>
    <td><strong>Model</strong></td>
    <td>RMA2016</td>
  </tr>
  <tr>
    <td><strong>Model Name</strong></td>
    <td>realme Buds 2 Neo</td>
  </tr>
  <tr>
    <td><strong>Model Year</strong></td>
    <td>2021</td>
  </tr>
  <tr>
    <td><strong>Product Dimensions</strong></td>
    <td>132 x 2.8 x 1.5 cm; 14 Grams</td>
  </tr>
  <tr>
    <td><strong>Item model number</strong></td>
    <td>RMA2016</td>
  </tr>
  <tr>
    <td><strong>Special Features</strong></td>
    <td>in-ear</td>
  </tr>
  <tr>
    <td><strong>Mounting Hardware</strong></td>
    <td>Earphone, Ear Tips, User Manual</td>
  </tr>
  <tr>
    <td><strong>Number of items</strong></td>
    <td>1</td>
  </tr>
  <tr>
    <td><strong>Microphone format</strong></td>
    <td>In-Line, Built-In</td>
  </tr>
  <tr>
    <td><strong>Microphone technology</strong></td>
    <td>Omnidirectional</td>
  </tr>
  <tr>
    <td><strong>Headphones form factor</strong></td>
    <td>In Ear</td>
  </tr>
  <tr>
    <td><strong>Batteries Included</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Batteries Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Cable feature</strong></td>
    <td>Tangle Free</td>
  </tr>
  <tr>
    <td><strong>Connector Type</strong></td>
    <td>Wired</td>
  </tr>
  <tr>
    <td><strong>Material</strong></td>
    <td>Tpu</td>
  </tr>
  <tr>
    <td><strong>Manufacturer</strong></td>
    <td>realme</td>
  </tr>
  <tr>
    <td><strong>Country of Origin</strong></td>
    <td>China</td>
  </tr>
  <tr>
    <td><strong>Item Weight</strong></td>
    <td>14 g</td>
  </tr>
</table>
</table><style>
  table {
    margin: 0 auto; /* center the table horizontally */
  }
</style>
""",unsafe_allow_html=True)


st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center;'>
        <img src="https://cdn.dribbble.com/users/673429/screenshots/12590629/media/013d852be84f6587110cc59f75d75eec.gif" 
             alt="Animated GIF" 
             width="1300" 
             height="600">
    </div>
""", unsafe_allow_html=True)


st.markdown("<br><hr><br>",unsafe_allow_html=True)

data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')

product_data = data[data['Products'] == 'Wired Headphones']

country_data = product_data.groupby('Country')['Quantities_Ordered'].mean().reset_index()

st.write("## Bar Chart\nThis shows the quantities ordered by the country :")

st.bar_chart(country_data, x='Country', y='Quantities_Ordered')



st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED PRODUCTS </h1>", unsafe_allow_html=True)

st.markdown("""<div style="display: flex;">
<a href = "https://www.amazon.in/realme-Shade-Qualcomm-Snapdragon-Camera/dp/B0BN3LHR75/ref=sr_1_3?crid=6VI2M747QLWT&keywords=realme+gt+neo+3t&qid=1678608910&sprefix=realme+gt%2Caps%2C664&sr=8-3" target = "_self"><img src="https://image01.realme.net/general/20220914/1663157307583.png" style="width:400px; height:400px; object-fit: cover; display: block;margin-right: 20px;"></a>
<a href = "https://buy.realme.com/in/goods/196" target = "_self"><img src="https://fdn.gsmarena.com/imgroot/news/20/05/realme-watch-official/-727/gsmarena_001.jpg" style="width:500px; height:400px; object-fit: cover; display: block;margin-right: 20px;"></a>
<a href = "https://onecart.co.in/product/realme-buds-air-pro-bluetooth-truly-wireless-in-ear-earbuds-with-mic/" target = "_self"><img src="https://shreepng.com/img/Inside/Electronic/Earphone/realme%20Buds%20Air%20Pro%20Black%20Earphones.png" style="width:400px; height:400px; object-fit: cover; display: block;margin-right: 20px;"></a>
</div>""",unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""<div>
            <a href="http://localhost:8501/" target ="_self" style="
    display: inline-block;
    padding: 0.5em 1em;
    background-color: #000000;
    border: none;
    border-radius: 3px;
    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2);
    text-decoration: none;
    color: #FFFFFF;
    transition: all 0.2s ease-in-out;
">
&#9754; Back
</a>
<a href="https://app.powerbi.com/reportEmbed?reportId=d54cfa2c-3392-4bb5-8b7b-cac038b09f31&autoAuth=true&ctid=9d049b1f-0aea-4675-a840-732bbb1e6f9c" target ="_self" style="
    display: inline-block;
    padding: 0.5em 1em;
    background-color: #000000;
    border: none;
    border-radius: 3px;
    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2);
    text-decoration: none;
    color: #FFFFFF;
    transition: all 0.2s ease-in-out;
    float : right
">
 Visualize &#9755;
</a>
</div>""", unsafe_allow_html=True)