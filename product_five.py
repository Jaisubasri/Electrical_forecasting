import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED BRAND FOR EARBUDS </h1>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""<div style="background-color: #000000;"><h1 style='text-align: center; color : #FFFFFF; font-size:65px'>Apple</h1></div>""", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

images = ["https://consomac.fr/images/news/airpods-pro-lc3.jpg","https://www.apple.com/newsroom/images/product/airpods/standard/Apple-AirPods-Pro-2nd-gen-hero-220907.jpg.news_app_ed.jpg","https://www.apple.com/v/airpods-pro/g/images/meta/og__eui2mpgzwyaa_specs.png?202212220347"]


image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:2000px; height:550px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

st.markdown("<br><hr><br>", unsafe_allow_html=True)

st.markdown("""<html>
  <head>
    <title>About Apple</title>
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
      <h1>About Apple</h1>
    </header>
    <div class="container">
      <section>
        <h2>Our Histroy</h2>
        <p>
          Apple is a multinational technology company based in Cupertino, California. 
          It was founded in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne. 
          Apple designs, develops, and sells consumer electronics, computer software, and online services.
        </p>
        <p>
        Apple is best known for its range of products, including the iPhone, iPad, Mac, iPod, Apple Watch, 
        and Apple TV. The company's software products include the macOS and iOS operating systems, 
        the iTunes media player, the Safari web browser, and the iLife and iWork creativity and productivity suites.
        </p>
        <p>
        Apple is also a leader in online services, with offerings such as the App Store, Apple Music, 
        iCloud, Apple Pay, and Apple Arcade.Apple has a reputation for creating innovative, high-quality 
        products that are well-designed and easy to use. The company has a strong focus on user 
        experience and has been recognized for its design and usability with numerous awards over the years.
        </p>
        <p>
        In addition to its product and service offerings, Apple is also known for its corporate 
        culture and management style. The company has a unique approach to innovation, with a focus on 
        secrecy and a highly centralized decision-making process.Overall, Apple has become one of 
        the world's most valuable companies, with a market capitalization of over $2 trillion. 
        The company continues to innovate and expand its offerings, with a strong focus on technology and design 
        </p>
      </section>
      <section>
        <h2>Our Products</h2>
        <p>Realme offers a variety of products, including:</p>
        <ul>
          <p>iPhone</p>
          <p>iPad</p>
          <p>MacBook<p/>
          <p>iMac<p/>
          <p>Air Pods</p>
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
        <img src="https://www.apple.com/newsroom/images/product/iphone/lifestyle/Apple_iPhone-11-and-iPhone-11-Pro-reviews_091719_inline.gif.large.gif" 
             alt="Animated GIF" 
             width="1300" 
             height="600">
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

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
    <th>Brand</th>
    <td>Apple</td>
  </tr>
  <tr>
    <th>Manufacturer</th>
    <td>Apple, Apple Inc, One Apple Park Way, Cupertino, CA 95014, USA. or Apple India Private Limited No.24, 19th floor, Concorde Tower C, UB City, Vittal Mallya Road, Bangalore - 560 001</td>
  </tr>
  <tr>
    <th>Model</th>
    <td>MPNY3HN/A</td>
  </tr>
  <tr>
    <th>Model Name</th>
    <td>AirPods 3rd Generation</td>
  </tr>
  <tr>
    <th>Batteries</th>
    <td>1 Lithium Ion batteries required. (included)</td>
  </tr>
  <tr>
    <th>Item model number</th>
    <td>MPNY3HN/A</td>
  </tr>
  <tr>
    <th>Special Features</th>
    <td>Force sensor lets you easily control your entertainment, answer or end calls, and more</td>
  </tr>
  <tr>
    <th>Mounting Hardware</th>
    <td>AirPods, Lightning Charging Case, Lightning to USB-C Cable, Documentation</td>
  </tr>
  <tr>
    <th>Number of items</th>
    <td>1</td>
  </tr>
  <tr>
    <th>Headphones form factor</th>
    <td>In Ear</td>
  </tr>
  <tr>
    <th>Batteries Included</th>
    <td>Yes</td>
  </tr>
  <tr>
    <th>Batteries Required</th>
    <td>Yes</td>
  </tr>
  <tr>
    <th>Battery cell composition</th>
    <td>Lithium Ion</td>
  </tr>
  <tr>
    <th>Cable feature</th>
    <td>Without Cable</td>
  </tr>
  <tr>
    <th>Connector Type</th>
    <td>Bluetooth 5.0</td>
  </tr>
  <tr>
    <th>Includes Rechargable Battery</th>
    <td>Yes</td>
  </tr>
  <tr>
    <th>Manufacturer</th>
    <td>Apple</td>
  </tr>
  <tr>
    <th>Country of Origin</th>
    <td>China</td>
  </tr>
  <tr>
    <th>Item Weight</th>
    <td>37.9 g</td>
  </tr>
</table><style>
  table {
    margin: 0 auto; /* center the table horizontally */
  }
</style>""",unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center;'>
        <img src="https://www.cultofmac.com/wp-content/uploads/2020/10/Apple_iPhone12Pro-back-camera-magsafe-charger_10132020.gif" 
             alt="Animated GIF" 
             width="1300" 
             height="600">
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)

data = pd.read_csv('D:/College/SEM-4/dav project/sales_forecasting.csv')

product_data = data[data['Products'] == 'Apple Airpods Headphones']

country_data = product_data.groupby('Country')['Quantities_Ordered'].mean().reset_index()

st.write("## Bar Chart\nThis shows the quantities ordered by the country :")

st.line_chart(country_data, x='Country', y='Quantities_Ordered')


st.markdown("<h1 style='text-align: center; color : #FFFFFF; font-size:65px'>RECOMMENDED PRODUCTS </h1>", unsafe_allow_html=True)

st.markdown("""<div style="display: flex;">
<a href = "https://www.amazon.in/Apple-iPhone-128GB-Deep-Purple/dp/B0BDJ7P6NG/ref=sr_1_5?crid=35ELJ5UOS40RL&keywords=apple%2Biphone%2B14&qid=1678620727&sprefix=apple%2Biphone%2B%2Caps%2C331&sr=8-5&th=1" target = "_self"><img src="https://images.unsplash.com/photo-1603791239531-1dda55e194a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8YXBwbGUlMjBpcGhvbmV8ZW58MHx8MHx8&w=1000&q=80" style="width:650px; height:500px; object-fit: cover; display: block;margin-right: 20px;"></a>
<a href = "https://www.amazon.in/2022-Apple-MacBook-Laptop-chip/dp/B0B3BQ11LP/ref=sr_1_4?crid=182PDG9H3RT3F&keywords=apple+laptops&qid=1678620887&sprefix=apple+lap%2Caps%2C337&sr=8-4" target = "_self"><img src="https://www.yankodesign.com/images/design_news/2021/08/this-concept-is-true-adaptation-of-how-we-want-apple-macbook-pro-to-be-in-2021/Apple_MacBook-Pro-2021_concept_-Gadget_-5.jpg" style="width:650px; height:500px; object-fit: cover; display: block;margin-right: 20px;"></a>
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
<a href="https://app.powerbi.com/reportEmbed?reportId=53068e80-8fe9-4bf5-80ce-69a4a6e60854&autoAuth=true&ctid=9d049b1f-0aea-4675-a840-732bbb1e6f9c" target ="_self" style="
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