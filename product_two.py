import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED BRAND FOR LIGHTNING FAST CHARGER </h1>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""<div style="background-color: #cf4040;"><h1 style='text-align: center; color : #FFFFFF; font-size:65px'>Boat </h1></div>""", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

images = ["https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/S/aplus-media/vc/aaa29ef7-5d2f-4225-84ac-8a4dfa39cb8a.__CR0,0,970,600_PT0_SX970_V1___.jpg","https://hungamadeal.co.in/wp-content/uploads/2021/04/boAt-Micro-USB-Fast-Charging-Cable.jpg","https://i0.wp.com/m.media-amazon.com/images/S/aplus-media/vc/6399677c-8f83-407d-9286-5848b38febe9.__CR0,0,970,600_PT0_SX970_V1___.jpg?ssl=1"]

image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:2000px; height:550px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""
<html>
  <head>
    <title>About Boat</title>
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
      <h1>About Boat</h1>
    </header>
    <div class="container">
      <section>
        <h2>Our Histroy</h2>
        <p>
          Boat is a leading brand in the audio equipment and accessories industry.
          Founded in 2016, Boat has quickly become a household name in India and
          around the world, offering a wide range of products that are designed to
          enhance the listening experience of its customers.
        </p>
        <p>
          Boat's products are known for their high-quality sound, innovative designs,
          and affordable prices. The company's mission is to make premium audio products
          accessible to everyone, regardless of their budget.
        </p>
        <p>
        Boat has a strong presence in India, and has expanded to other countries including 
        the United States, United Kingdom, and the United Arab Emirates. The company has 
        received several awards for its products and services, including the prestigious iF 
        Design Award in 2020 for its Airdopes 441 earbuds.
      </p>
      <p>
      Overall, Boat is a reputable and innovative company that continues to push the boundaries 
      of audio technology. With its focus on quality, affordability, and customer satisfaction, 
      Boat is a brand that is here to stay in the audio equipment and accessories industry.
      </p>
      </section>
      <section>
        <h2>Our Products</h2>
        <ul>
          <p>Earphones</p>
          <p>Bluetooth speakers</p>
          <p>Headphones</p>
          <p>Soundbars</p>
          <p>True wireless earbuds</p>
          <p>Gaming headphones</p>
          <p>Smartwatches</p>
        </ul>
      </section>
    </div>
  </body>
</html>

""",unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""<div style="text-align:center"><img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/dff3c854771989.5968b4c2b862a.gif" alt="Animated GIF" width="1000" height="500"></div>""", unsafe_allow_html=True)

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
    <td>boAt</td>
  </tr>
  <tr>
    <th>Model</th>
    <td>Micro USB 55</td>
  </tr>
  <tr>
    <th>Connector Type</th>
    <td>USB 2.0</td>
  </tr>
  <tr>
    <th>Cable Type</th>
    <td>USB</td>
  </tr>
  <tr>
    <th>Compatible Devices</th>
    <td>Personal Computer, Smartphone, Speaker</td>
  </tr>
  <tr>
    <th>Special Feature</th>
    <td>Tangle Free</td>
  </tr>
  <tr>
    <th>Recommended Uses For Product</th>
    <td>Game</td>
  </tr>
  <tr>
    <th>Color</th>
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
    <td>1 Piece</td>
  </tr>
  <tr>
    <th>Number of items</th>
    <td>2</td>
  </tr>
  <tr>
    <th>Product Dimensions</th>
    <td>150 x 1 x 2 cm; 30 Grams</td>
  </tr>
  <tr>
    <th>Item Weight</th>
    <td>30 Grams</td>
  </tr>
  <tr>
    <th>Batteries Required</th>
    <td>No</td>
  </tr>
  <tr>
    <th>Country of Origin</th>
    <td>China</td>
  </tr>
  <tr>
    <th>Manufacturer</th>
    <td>Imagine Marketing Ltd</td>
  </tr>
  <tr>
    <th>Manufacturer Contact</th>
    <td>info@imaginemarketingindia.com</td>
  </tr>
</table>
<style>
  table {
    margin: 0 auto; /* center the table horizontally */
  }
</style>
""",unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center;'>
        <img src="https://cdn.shopify.com/s/files/1/0057/8938/4802/files/2_3d583989-3aab-4622-91cd-f256b3007d7b.gif?v=1658570608" 
             alt="Animated GIF" 
             width="1000" 
             height="500">
    </div>
""", unsafe_allow_html=True)


st.markdown("<br><hr><br>",unsafe_allow_html=True)

data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')

product_data = data[data['Products'] == 'Lightning Charging Cable']

country_data = product_data.groupby('Country')['Quantities_Ordered'].mean().reset_index()

st.write("## Bar Chart\nThis shows the quantities ordered by the country :")

st.bar_chart(country_data, x='Country', y='Quantities_Ordered')


st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED PRODUCTS </h1>", unsafe_allow_html=True)

st.markdown("""<div style="display: flex;">
<a href = "https://www.amazon.in/Rockerz-450-Wireless-Bluetooth-Headphone/dp/B07PR1CL3S/ref=sr_1_17_sspa?crid=10X7P4T25FIFK&keywords=boat%2Bheadphones&qid=1678605465&sprefix=boat%2B%2Caps%2C386&sr=8-17-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfbmV4dA&th=1" target = "_self"><img src="https://cdn.shopify.com/s/files/1/0057/8938/4802/products/rockerz-410-black_600x.png" style="width:450px; height:500px; object-fit: cover; display: block;margin-right: 20px;"></a>
<a href = "https://www.amazon.in/boAt-Bluetooth-Playback-Wireless-Ergonomical/dp/B0BR3WB2S2/ref=sr_1_20?crid=1ZHXLIHPY9R91&keywords=boat+bluetooth+speaker&qid=1678605557&sprefix=boat+bluetooth+%2Caps%2C575&sr=8-20" target = "_self"><img src="https://cdn.shopify.com/s/files/1/0057/8938/4802/products/playback_b877b7fc-430a-46f2-9005-aecfb756db3b_1500x.jpg?v=1655372348" style="width:450px; height:500px; object-fit: cover; display: block;margin-right: 20px;"></a>
<a href = "https://www.amazon.in/boAt-Wave-Lite-Smartwatch-Activity/dp/B09V12K8NT/ref=sr_1_7?crid=3II0OVJS6U5H1&keywords=boat+smart+watch&qid=1678605636&sprefix=boat+smart%2Caps%2C568&sr=8-7"target = "_self"><img src="https://5.imimg.com/data5/SELLER/Default/2021/4/LR/BL/DK/10876653/boat-storm-smartwatch-1000x1000.jpeg" style="width:450px; height:500px; object-fit: cover; display: block;margin-right: 20px;"></a>
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
<a href="https://app.powerbi.com/reportEmbed?reportId=cf4ae071-d3f7-4c62-93af-8c24e2fec3f8&autoAuth=true&ctid=9d049b1f-0aea-4675-a840-732bbb1e6f9c" target ="_self" style="
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