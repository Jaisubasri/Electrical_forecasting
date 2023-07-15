import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED BRAND FOR BATTERY </h1>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""<div style="background-color: #cf4d02;"><h1 style='text-align: center; color : #FFFFFF; font-size:65px'>Duracell </h1></div>""", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

images = ["https://i.shgcdn.com/79e6cfa8-42ab-4197-b898-7872b750d346/-/format/auto/-/preview/3000x3000/-/quality/lighter/","https://www.technicolor.com/sites/default/files/2021-07/duracell_1170x660.jpg","https://m.media-amazon.com/images/S/stores-image-uploads-na-prod/a/AmazonStores/ATVPDKIKX0DER/d83ff3231100507a8069443b101ef497.w3000.h1500.jpg"]
image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:2000px; height:550px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""
<html>
  <head>
    <title>Duracell - About Us</title>
    <style>
      /* Style the header */
      header {
        background-color: #000000;
        padding: 20px;
        text-align: center;
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
      <h1>About Duracell</h1>
    </header>
    <div class="container">
      <section>
        <h2>Our History</h2>
        <p>
          Duracell is a brand of batteries and smart power systems owned by the American 
          multinational corporation Procter & Gamble. The company was originally founded 
          in the early 1920s as the P.R. Mallory Company, which produced batteries for military 
          and commercial use. The brand name "Duracell" was first used in the 1960s and has 
          since become synonymous with reliable, long-lasting batteries.
        </p>
        <p>
          Duracell produces a wide range of batteries for consumer and industrial use, 
          including alkaline, lithium, and rechargeable batteries. The company's batteries 
          are used in a variety of devices, including toys, flashlights, remote controls, 
          and portable electronics.In addition to its batteries, Duracell also produces smart 
          power systems and portable chargers designed to provide power for smartphones, tablets, and other mobile devices.
        </p>
        <p>
        Duracell is known for its "copper top" design, which features a copper-colored top on its batteries. 
        The company's logo is a silhouette of a copper-colored drum with the brand name written in 
        white letters.Overall, Duracell has a reputation for producing high-quality batteries and power 
        solutions that are reliable and long-lasting. The brand is widely recognized and trusted by consumers around the world.
        </p>
      </section>
      <section>
        <h2>Our Products</h2>
        <p>
          Duracell offers a wide range of batteries and power products for a variety of devices, including:
        </p>
        <ul>
          <p>Alkaline batteries (AA, AAA, C, D, 9V)</p>
          <p>Lithium coin batteries</p>
          <p>Rechargeable batteries</p>
          <p>Battery chargers</p>
          <p>Portable power banks</p>
        </ul>
      </section>
    </div>
  </body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""<div style="text-align:center"><img src="https://thumbs.gfycat.com/BrownMindlessGoral-max-1mb.gif" alt="Animated GIF" width="1000" height="500"></div>
""",unsafe_allow_html=True)


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
    <td><strong>Brand</strong></td>
    <td>Duracell</td>
  </tr>
  <tr>
    <td><strong>Manufacturer</strong></td>
    <td>HongTu High & New Technology Development Zone,Nan Cheng District,DongGuan,GuangDong Province,China, HongTu High & New Technology Development Zone, Nan Cheng District, DongGuan City, GuangDong Province, China 523080, Tollfree Number-18001207897</td>
  </tr>
  <tr>
    <td><strong>Model Name</strong></td>
    <td>Alkaline</td>
  </tr>
  <tr>
    <td><strong>Product Dimensions</strong></td>
    <td>31 x 30 x 18.5 cm; 110 Grams</td>
  </tr>
  <tr>
    <td><strong>Compatible Devices</strong></td>
    <td>Camera</td>
  </tr>
  <tr>
    <td><strong>Mounting Hardware</strong></td>
    <td>Battery</td>
  </tr>
  <tr>
    <td><strong>Number of items</strong></td>
    <td>20</td>
  </tr>
  <tr>
    <td><strong>Voltage</strong></td>
    <td>1.5 Volts</td>
  </tr>
  <tr>
    <td><strong>Batteries Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Battery cell composition</strong></td>
    <td>Alkaline</td>
  </tr>
  <tr>
    <td><strong>Manufacturer</strong></td>
    <td>HongTu High & New Technology Development Zone,Nan Cheng District,DongGuan,GuangDong Province,China</td>
  </tr>
  <tr>
    <td><strong>Country of Origin</strong></td>
    <td>China</td>
  </tr>
  <tr>
    <td><strong>Item Weight</strong></td>
    <td>110 g</td>
  </tr>
</table>
<style>
  table {
    margin: 0 auto; /* center the table horizontally */
  }
</style>""",unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""<div style="text-align:center"><img src="https://thumbs.gfycat.com/SkinnyFavoriteImpala-size_restricted.gif" alt="Animated GIF" width="1000" height="500"></div>
""",unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)

data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')

product_data = data[data['Products'] == 'AAA Batteries (4-pack)']

country_data = product_data.groupby('Country')['Quantities_Ordered'].mean().reset_index()

st.write("## Bar Chart\nThis shows the quantities ordered by the country :")

st.bar_chart(country_data, x='Country', y='Quantities_Ordered')

st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED PRODUCTS </h1>", unsafe_allow_html=True)

st.markdown("""<div style="display: flex;">
<a href="https://www.amazon.in/Duracell-Alkaline-Battery-Duralock-Technology/dp/B014SZOORC/ref=sr_1_2?crid=1OWO9UF4CZGPW&keywords=aa+4+duracell+ultra&qid=1678603242&sprefix=aa+4+duracell+ultra%2Caps%2C364&sr=8-2" target = "_self"><img src="https://www.duracell.in/upload/sites/10/2016/05/Alkaline_packshot_IN_Ultra_AA_4_BL_5000394121201_5009747_FOP-crop.png" style="width:500px; height:450px; object-fit: cover; display: block;margin-right: 20px;"></a>
<a href="https://www.amazon.in/Duracell-Alkaline-Battery-Duralock-Technology/dp/B014SZORQA/ref=pd_rhf_d_se_s_pd_crcd_sccl_2_3/261-2821198-7462932?pd_rd_w=35Kqs&content-id=amzn1.sym.dcf9b861-ea71-4cd9-870f-f1d20747f687&pf_rd_p=dcf9b861-ea71-4cd9-870f-f1d20747f687&pf_rd_r=05EYCNFF20057YMVE2MV&pd_rd_wg=wprm5&pd_rd_r=91f5c884-a256-4ba8-96dd-1f7a67c288ea&pd_rd_i=B014SZORQA&psc=1" target = "_self"><img src="https://www.duracell.co.uk/upload/2021/06/unnamed-file3.png" style="width:300px; height:450px; object-fit: cover; display: block;margin-right: 20px;"></a>
<a href = "https://www.amazon.in/Duracell-DURDL2032B2PK-Lithium-3-Volt-Battery/dp/B07G7KRQQ5/ref=sr_1_6_mod_primary_new?crid=3M7NDEPNU2MXZ&keywords=duracell+coin+battery+cr2032&qid=1678603872&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=duracell+coin+battery+cr+2032%2Caps%2C1346&sr=8-6" target = "_self"><img src="https://www.duracell.co.uk/upload/2016/07/Web-PI-Specialty_packshot_WE_LC_2032_1_BL_5000394033917_5014796_FOP.png" style="width:500px; height:450px; object-fit: cover; display: block;margin-right: 20px;"></a>
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
<a href="https://app.powerbi.com/reportEmbed?reportId=fa69100e-e132-4a84-a780-b283076ffdd0&autoAuth=true&ctid=9d049b1f-0aea-4675-a840-732bbb1e6f9c" target ="_self" style="
    display: inline-block;
    padding: 0.5em 1em;
    background-color: #000000;
    border:none;
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