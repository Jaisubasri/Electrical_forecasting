import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED BRAND FOR C TYPE CHARGER </h1>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""<div style="background-color: #7D0552;"><h1 style='text-align: center; color : #FFFFFF; font-size:65px'>Ptron </h1></div>""", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

images = ["https://cdn.shopify.com/s/files/1/0040/4396/4531/products/61VRvdC7vXL._SL1100_22e98658-717f-4f0e-bb37-0563589190d7.jpg?v=1632969297","https://cdn.shopify.com/s/files/1/0040/4396/4531/products/61999E3htJL._SL1100.jpg?v=1632968711","https://ph-test-11.slatic.net/p/f0979de462f918848fbdc844962c8bf2.jpg","https://cf.shopee.com.my/file/7bb4cb5ae7e31470213ed5f30ac1187d"]
image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:2000px; height:550px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""<html>
  <head>
    <title>About PTron</title>
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
      <h1>About PTron</h1>
    </header>
    <div class="container">
      <section>
        <h2>Our Histroy</h2>
        <p>
          PTron is a popular brand that offers a wide range of mobile accessories and
          audio products. Founded in 2014, PTron has quickly become a household name
          in India and around the world, offering high-quality products at affordable
          prices.
        </p>
        <p>
        In addition to its mobile accessories, Ptron has also launched a range of 
        smartwatches and fitness trackers that are designed to help users keep track of 
        their fitness goals and monitor their health. These products are equipped with 
        features such as heart rate monitoring, step tracking, and sleep tracking.
        </p>
        <p>
        Overall, Ptron is a brand that is committed to delivering high-quality and 
        affordable mobile accessories to its customers. The brand's focus on 
        innovation, quality, and affordability has helped it to establish a strong 
        presence in the competitive mobile accessories market.
        </p>
      </section>
      <section>
        <h2>Our Products</h2>
        <p>PTron offers a variety of products, including:</p>
        <ul>
          <p>Earphones</p>
          <p>Bluetooth speakers</p>
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
        <img src="https://images-eu.ssl-images-amazon.com/images/G/31/img22/WLA/Launches23/PtronZen/Ingress2/D70984804_1.gif" 
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

st.markdown("""<table>
  <tr>
    <th>Brand</th>
    <td>pTron</td>
  </tr>
  <tr>
    <th>Connector Type</th>
    <td>USB Type C</td>
  </tr>
  <tr>
    <th>Cable Type</th>
    <td>USB</td>
  </tr>
  <tr>
    <th>Compatible Devices</th>
    <td>Charging Adapter</td>
  </tr>
  <tr>
    <th>Special Feature</th>
    <td>Fast Charging</td>
  </tr>
  <tr>
    <th>Compatible Phone Models</th>
    <td>All Type-C enabled models</td>
  </tr>
  <tr>
    <th>Colour</th>
    <td>Black</td>
  </tr>
  <tr>
    <th>Connector Gender</th>
    <td>Male-to-Male</td>
  </tr>
  <tr>
    <th>Data Transfer Rate</th>
    <td>0.48 Gigabits Per Second</td>
  </tr>
  <tr>
    <th>Net Quantity</th>
    <td>1 Count</td>
  </tr>
  <tr>
    <th>Item Weight</th>
    <td>38 Grams</td>
  </tr>
  <tr>
    <th>Connector Type</th>
    <td>USB</td>
  </tr>
  <tr>
    <th>Model Name</th>
    <td>Solero TB301</td>
  </tr>
  <tr>
    <th>Number of items</th>
    <td>1</td>
  </tr>
  <tr>
    <th>Manufacturer</th>
    <td>Palred Electronics Pvt. Ltd., Sy.No.1240, Kurnool Nandyal Road, Nannur Village, Kurnool, Andhra Pradesh, 518002</td>
  </tr>
  <tr>
    <th>Model</th>
    <td>Solero TB301</td>
  </tr>
  <tr>
    <th>Product Dimensions</th>
    <td>150 x 0.4 x 0.6 cm; 38 Grams</td>
  </tr>
  <tr>
    <th>Item model number</th>
    <td>Solero TB301</td>
  </tr>
  <tr>
    <th>Special Features</th>
    <td>Fast Charging</td>
  </tr>
  <tr>
    <th>Batteries Required</th>
    <td>No</td>
  </tr>
  <tr>
    <th>Manufacturer</th>
    <td>Palred Electronics Pvt. Ltd.</td>
  </tr>
  <tr>
    <th>Country of Origin</th>
    <td>India</td>
  </tr>
  <tr>
    <th>Item Weight</th>
    <td>38 g</td>
  </tr>
</table><style>
  table {
    margin: 0 auto; /* center the table horizontally */
  }
</style>
""",unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center;'>
        <img src="https://cdn.shopify.com/s/files/1/0078/4842/7635/files/Musicbot_01.gif?9465310955774872219" 
             alt="Animated GIF" 
             width="1250" 
             height="550">
    </div>
""", unsafe_allow_html=True)


data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')

product_data = data[data['Products'] == 'USB-C Charging Cable']

country_data = product_data.groupby('Country')['Quantities_Ordered'].mean().reset_index()

st.write("## Bar Chart\nThis shows the quantities ordered by the country :")

st.bar_chart(country_data, x='Country', y='Quantities_Ordered')

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED PRODUCTS </h1>", unsafe_allow_html=True)

st.markdown("""<div style="display: flex;">
<a href = "https://ptron.in/products/ptron-bassbuds-b21-tws-earbuds-with-bluetooth-5-2-immersive-sound-stereo-calls-24hrs-playtime-in-ear-wireless-headphones-lightweight-touch-control-voice-assistance-ipx4-black" target = "_self"><img src="https://d2d22nphq0yz8t.cloudfront.net/88e6cc4b-eaa1-4053-af65-563d88ba8b26/https://media.croma.com/image/upload/v1665479634/Croma%20Assets/Entertainment/Wireless%20Earbuds/Images/263443_rp2hhe.png/mxw_640,f_auto" style="width:400px; height:400px; object-fit: cover; display: block;margin-right: 20px;"></a>
<a href = "https://www.amazon.in/Pulsefit-Bluetooth-Smartwatch-Tracking-Waterproof/dp/B0B8ZLR1Z3/ref=sr_1_18?crid=2U8JZQEXE6BW4&keywords=ptron+smart+watch&qid=1678607241&sprefix=pTron+s%2Caps%2C1342&sr=8-18" target = "_self"><img src="https://cdn.shopify.com/s/files/1/0040/4396/4531/products/Black_1_04-04-2022.png?v=1656495159" style="width:500px; height:400px; object-fit: cover; display: block;margin-right: 20px;"></a>
<a href = "https://www.flipkart.com/ptron-avento-classic-bluetooth-headset/p/itm804a9beb6ed9a" target = "_self"><img src="https://media.croma.com/image/upload/v1674050152/Croma%20Assets/Communication/Headphones%20and%20Earphones/Images/243176_0_a4vbic.png" style="width:500px; height:400px; object-fit: cover; display: block;margin-right: 20px;"></a>
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
<a href="https://app.powerbi.com/reportEmbed?reportId=55622593-28cd-4182-840d-9a57160793fd&autoAuth=true&ctid=9d049b1f-0aea-4675-a840-732bbb1e6f9c" target ="_self" style="
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