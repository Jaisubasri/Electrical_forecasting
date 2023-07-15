import streamlit as st
import requests

st.set_page_config(layout="wide")


#Tile
styles = """
    /* Center align text */
    .center {
        text-align: center;
    }

    /* Add a shadow to the box */
    .shadow {
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.25);
    }

    /* Add a gradient background */
    body {
        background: linear-gradient(to bottom, #ffffff, #f2f2f2);
    }

    /* Style the header */
    .header {
        background: linear-gradient(to bottom, #000000, #2C3539);
        color: white;
        padding: 20px;
    }

    /* Style the footer */
    .footer {
        background: linear-gradient(to bottom, #4B0082, #800080);
        color: white;
        padding: 20px;
    }
"""
st.markdown(f'<style>{styles}</style>', unsafe_allow_html=True)
header_html = """
    <div class="header shadow">
        <h1 class="center rainbow-text">Electronics Sale Analysis</h1>
    </div>
"""
st.markdown(header_html, unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

images = ["https://i.gadgets360cdn.com/large/oneplus_5_tv_ad_1497850410887.jpg",
          "https://i.ytimg.com/vi/nCi0EBl8MYY/maxresdefault.jpg",
          "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202103/boAt_TRebel_Collection_1200x768.jpeg?size=1200:675",
          "https://i.ytimg.com/vi/kFyku1QTGm4/maxresdefault.jpg",
          "https://i.ytimg.com/vi/2FVibB1tniI/maxresdefault.jpg",
          "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/G/31/img22/Laptops/Apple/MacBook_Pro_M2_Chip_Custom_Product_Page_Flex_Module_Amazon_Avail_L__en-IN_01._CB634583975_.jpg",
          "https://www.trustedreviews.com/wp-content/uploads/sites/54/2021/01/Sony-TV-2021-line-up.jpg"
  
            ]

image_html = ''
for url in images:
      image_html += f'<img src="{url}" style="width:2000px; height:550px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

st.markdown("<br><hr><br>", unsafe_allow_html=True)

#second title
st.markdown("""<div style='text-align: center;'>
                 <h2 style='display: inline-block; padding: 0 20px;
                            background-clip: text;
                            -webkit-background-clip: text;
                            color: white;'>
                     Spot Light
                 </h2>
             </div>""", unsafe_allow_html=True)


st.markdown("<br><hr><br>", unsafe_allow_html=True)


#scroll bar image for spot light
images = [
    {"src": "https://5.imimg.com/data5/SELLER/Default/2022/9/ZJ/EJ/TZ/130321820/duracell-aaaa-mx2500-alkaline-batteries-1-5v-pack-of-2-1000x1000.jpg", "href": "http://localhost:8502/","text" : "Battery"},
    {"src": "https://www.jiomart.com/images/product/420x420/492575299/boat-wcd-18-watts-qcpd-travel-charger-with-usb-type-c-cable-white-digital-o492575299-p591196614-5-202203212209.jpeg", "href": "http://localhost:8503/","text" : "Fast Charger"},
    {"src": "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/61m+5UD8+7L._SY355_.jpg", "href": "http://localhost:8504/","text":"C Type Cable"},
    {"src": "https://fonebook.cdn.betanet.in/fonebook/wp-content/uploads/2022/12/Realme-Buds-Q-RMA215-Black-Earbuds-02-phonewale-online-buy-at-lowest-price-ahmedabad-gujarat.jpg", "href": "http://localhost:8505/","text":"Wired HearPhone"},
    {"src": "https://images.unsplash.com/photo-1511300961358-669ca3ad05af?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZWFycG9kc3xlbnwwfHwwfHw%3D&w=1000&q=80", "href": "http://localhost:8506/","text":"Apple Air Pod"}
]

image_html = ''
for url in images:
    image_html += f"""
        <div style="text-align:center;">
            <a href="{url['href']}" target="_self" style="text-decoration: none;">
                <img src="{url['src']}" style="width:300px; height:550px; object-fit: cover; display: block;margin-right: 20px;">
                <div style= "color : #FFFFFF ; font-size : 25px ;margin-top: 20px;">{url['text']}</div>
            </a>
        </div>"""
st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)


#Best Product
st.markdown("""<!DOCTYPE html>
<html>
<head>
	<title>Best Product</title>
	<style>
		.container1 {
			display: flex;
			flex-wrap: nowrap;
			justify-content: center;
			align-items: center;
			margin-top: 50px;
            text-align : center;
            overflow-x: scroll;
		}
		.card1 {
			width: 500px;
			margin: 20px;
			padding: 20px;
			border: 1px solid #ccc;
			border-radius: 4px;
			box-shadow: 0 0 10px rgba(0,0,0,0.1);
			text-align: center;
		}
		.card1 img {
			width: 203px;
			height: 249px;
			object-fit: cover;
			margin-bottom: 10px;
			border-radius: 4px;
		}
		.card1 h2 {
			font-size: 24px;
			margin: 10px 0;
		}
		.card1 p {
			font-size: 16px;
			margin: 10px 0;
		}
  .rating {
  display: flex;
  align-items: center;
  font-size: 1.2rem;
  color: #f5b41c;
}
.rating svg {
  fill: #f5b41c;
  height: 1.2rem;
  width: 1.2rem;
  margin-right: 0.3rem;
}
.rating svg.unfilled {
  fill: none; /* or transparent */
}
.rating svg.half {
  position: relative;
  overflow: hidden;
  height: 1.0rem;
  width: 1.2rem;
  margin-right: 0.3rem;
}
.rating svg.half:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  height: 50%;
  width: 30%;
  z-index: 1;
}
.rating svg.half path {
  fill: #f5b41c;
  height: 0.5rem;
  width: 0.5rem;
  margin-right: 0.3rem;
}
}
.rating svg.half:before path {
  fill: #f5b41c;
  height: 0.8rem;
  width: 1.2rem;
  margin-right: 0.3rem;
}
}
.rating span {
  margin-left: 0.5rem;
}
	</style>
</head>
<body>
	<h1>Best Product</h1>
    <br><hr>
	<div class="container1">
		<div class="card1">
			<img src="https://m.media-amazon.com/images/I/610pghkO81L._AC_UY327_FMwebp_QL65_.jpg">
			<h2>Apple iPhone 14 Pro Max - Space Black </h2>
            <a href = 'https://www.amazon.in/Apple-iPhone-128GB-Space-Black/dp/B0BDJ22G36/ref=sr_1_1?keywords=Apple+iPhone+14+Pro+Max+%28128+GB%29+-+Space+Black&qid=1678902422&sr=8-1'; target = "_self" style = "background-color: #4CAF50;
			color: white;
			padding: 10px 20px;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			font-size: 16px;">Buy Now</a>
             <div class="rating">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="half"><path d="M11.26,17.68l-4.1,3.38a1,1,0,0,1-1.45-1.06l.89-4.9L3.14,9.81a1,1,0,0,1,.54-1.7L8.23,7.5,11.5,2.38a1,1,0,0,1,1,0l3.27,5.12,5.55.81a1,1,0,0,1,.54,1.7L16.32,14.72l.89,4.9a1,1,0,0,1-1.45,1.06l-4.1-3.38Z"/></svg>       
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
       <span>4.2</span>
    </div>
		</div>
  <div class="card1">
			<img src="https://m.media-amazon.com/images/I/81I2VpromoL._AC_UY327_FMwebp_QL65_.jpg">
			<h2>Samsung 108 cm (43 inches) - Black </h2>
			<a href = 'https://www.amazon.in/Samsung-inches-Smart-UA43T5770AUXXL-Black-Hair/dp/B086WPVCP7/ref=sr_1_6?keywords=Samsung+108+cm+%2843+inches%29+-+Black&qid=1678902469&sr=8-6'; target = "_self" style = "background-color: #4CAF50;
			color: white;
			padding: 10px 20px;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			font-size: 16px;">Buy Now</a>
    <div class="rating">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <span>4.8</span>
    </div>
		</div>
  <div class="card1">
			<img src="https://m.media-amazon.com/images/I/71f5Eu5lJSL._AC_UL480_FMwebp_QL65_.jpg">
			<h2>Apple Air Laptop 8GB RAM, Space Grey</h2>
			<a href = 'https://www.amazon.in/2022-Apple-MacBook-Laptop-chip/dp/B0B3BQ11LP/ref=sr_1_2?keywords=Apple+Air+Laptop+8GB+RAM%2C+Space+Grey&qid=1678902567&sr=8-2'; target = "_self" style = "background-color: #4CAF50;
			color: white;
			padding: 10px 20px;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			font-size: 16px;">Buy Now</a>
    <div class="rating">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <span>4.7</span>
    </div>
		</div>
  <div class="card1">
			<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcWimWMcawQqTUkmI4GIRzi3JTW2Gvl2TewYxVJfL8JR4k7MPbAzi8Gal0q6l0r8FsLhs&usqp=CAU">
			<h2>Google Pixel 4 Pro 4G clearly White , 64GB</h2>
			<a href = 'https://www.amazon.in/Google-Pixel-64GB-Clearly-White/dp/B0972PWTK3/ref=sr_1_9?keywords=Google+Pixel+6+Pro+5G+Cloudy+White+%2C+128GB&qid=1678902645&sr=8-9'; target = "_self" style = "background-color: #4CAF50;
			color: white;
			padding: 10px 20px;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			font-size: 16px;">Buy Now</a>
    <div class="rating">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 .5l3.09 7.72 8.41.58-6.42 5.45 1.87 7.76L12 18.52 4.03 22.01l1.87-7.76L.5 8.8l8.41-.58L12 .5z"/></svg>
        <span>4.9</span>
    </div>
		</div>
	</div>
</body>
</html>
""",unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

st.markdown("""<div class="upcoming-products">
  <h2>Upcoming Products</h2>
  <ul>
    <li>
    <div class = "product-item">
      <img src="https://cdn1.smartprix.com/rx-ijurVye4l-w420-h420/realme-buds-air-4-tr.webp" alt="Product 1">
      <h3>Realeme Buds Air 4 Earbuds</h3>
      <div class="top-seller">Coming Soon..</div>
      </div>
    </li>
    <li>
    <div class = "product-item">
      <img src="https://cdn.shopify.com/s/files/1/0057/8938/4802/products/black_320d7c10-5bdf-435b-a0e5-5f19aaeb8de2_600x.png?v=1673616471" alt="Product 2">
      <h3>boAt Wave Style Call</h3>
      <div class="top-seller">Coming Soon..</div>
      </div>
    </li>
    <li>
    <div class = "product-item">
      <img src="https://images.macrumors.com/t/5QQKabw_7gEYdFHUJHw7Fb_Xhac=/800x0/article-new/2022/06/MacBook-Air-Multiple-Sizes-Feature.jpg?lossy" alt="Product 3">
      <h3>Apple's 15-Inch MacBook Air</h3>
      <div class="top-seller">Coming Soon..</div>
      </div>
    </li>
    <li>
    <div class = "product-item">
      <img src="https://images.macrumors.com/t/zhGDOPq20ZA9WC3MSqteDUFFEak=/400x400/smart/article-new/2021/09/airpods-pro-black-background.jpg" alt="Product 3">
      <h3>Second-Generation AirPods Pro</h3>
      <div class="top-seller">Coming Soon..</div>
      </div>
    </li>
    <li>
    <div class = "product-item">
      <img src="https://cdn.shopify.com/s/files/1/0057/8938/4802/products/Packaging_v2.5130_800x.png?v=1678378826" alt="Product 3">
      <h3>boAt Airdopes 458</h3>
      <div class="top-seller">Coming Soon..</div>
      </div>
    </li>
  </ul>
</div>

<style>
  .upcoming-products h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  .upcoming-products ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-wrap: nowrap;
    overflow-x:auto;
  }
  .upcoming-products li {
    margin: 1rem;
    width: calc(33.33% - 2rem);
    text-align: center;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    transition: transform 0.2s ease-in-out;
  }
 .product-item .top-seller {
        background-color: #00D100;
        color: #fff;
        font-size: 16px;
        font-weight: bold;
        padding: 5px 10px;
        border-radius: 5px;
        position: absolute;
        top: 10px;
        right: 10px;
    }
  .upcoming-products li:hover {
    transform: scale(1.05);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  }
  .upcoming-products li img {
    width: 100%;
    height: 250px;
    object-fit: contain;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
  }
  .upcoming-products li h3 {
    margin: 1rem 0 0;
    font-size: 1.2rem;
  }
  .upcoming-products li p {
    margin: 0.5rem 0;
  }
  .upcoming-products li p:last-of-type {
    font-style: italic;
  }
   .product-item {
    height: 350px;
    overflow: hidden;
  }
  .product-item img {
    width: 100%;
    height: auto;
    object-fit: cover;
  }
  .product-item h3 {
    margin: 1rem 0 0;
    font-size: 1.2rem;
  }
</style>""",unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

#Latest News
st.markdown("""<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="container">
  <h2>News</h2>
  <ul class="cards">
    <li class="card">
    <img src="https://img.etimg.com/thumb/msid-98649465,width-210,height-158,imgsize-15430,,resizemode-75/bharat-electronics.jpg">
      <div><br>
        <h4 class="card-title">Buy Bharat Electronics, target price Rs 130: ICICI Direct</h4>
        <div class="card-content">
          <p>Bharat Electronics, incorporated in the year 1954, is a Large Cap company operating in Defence sector.</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://economictimes.indiatimes.com/markets/stocks/recos/buy-bharat-electronics-target-price-rs-130-icici-direct/articleshow/98649435.cms" target = "_self" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
    <img src="https://img.etimg.com/thumb/msid-98595930,width-210,height-158,imgsize-32364,,resizemode-75/bel.jpg" alt="news2" style="width:100%">
      <div><br>
        <h4 class="card-title">Buy Bharat Electronics, target price Rs 105</h4>
        <div class="card-content">
          <p>Promoters held 51.14 per cent stake in the company as of 31-Dec-2022, while FIIs owned 17.34 per cent, DIIs 24.96 per cent</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://economictimes.indiatimes.com/markets/stocks/recos/buy-bharat-electronics-target-price-rs-105-prabhudas-lilladher/articleshow/98595916.cms" target = "_self" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
      <img src="https://img.etimg.com/thumb/msid-98218728,width-300,height-225,imgsize-1239954,,resizemode-75/xiaomis-india-biz-turns-around-revenue-grows-over-9-in-fy22.jpg" alt="news3" style="width:100%">
      <div><br>
        <h4 class="card-title">Xiaomi's India biz turns around, revenue grows</h4>
        <div class="card-content">
          <p>Xiaomi turned around its India business in FY22 with the company's turnover growing more than 9% to Rs 39,099 crore</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://economictimes.indiatimes.com/industry/cons-products/electronics/xiaomis-india-biz-turns-around-revenue-grows-over-9-in-fy22/articleshow/98218720.cms" target = "_self" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
      <img src="https://img.etimg.com/thumb/msid-94251757,width-300,height-225,imgsize-30808,,resizemode-75/samsung-india-to-start-selling-televisions-from-mobile-phone-stores.jpg" alt="news4" style="width:100%">
      <div><br>
        <h4 class="card-title">Samsung aims for 45% jump in electronic product </h4>
        <div class="card-content">
          <p>Senior vice president Mohandeep Singh said the sales projections are made after the company posted a similar pace...</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://economictimes.indiatimes.com/news/india/dri-issues-show-cause-notice-to-samsung-india/articleshow/96925150.cms" target = "_self" class="card-link">Learn More</a>
      </div>
    </li>
    <li class="card">
      <img src="https://img.etimg.com/thumb/msid-96738431,width-300,height-225,imgsize-297100,,resizemode-75/hong-ju-jeon-md-lg-india-.jpg" alt="news5" style="width:100%">
      <div><br>
        <h4 class="card-title">Hong Ju Jeon appointed as LG Electronics MD for India business</h4>
        <div class="card-content">
          <p>LG Electronics India on Wednesday appointed Hong Ju Jeon as the Managing Director...</p>
        </div>
      </div>
      <div class="card-link-wrapper">
        <a href="https://economictimes.indiatimes.com/industry/cons-products/electronics/hong-ju-jeon-appointed-as-lg-electronics-md-for-india-business/articleshow/96738408.cms" target = "_self" class="card-link">Learn More</a>
      </div>
    </li>
  </ul>
</div>
</body>
</html>
<style>
:root {
  --red: #ef233c;
  --darkred: #c00424;
  --platinum: #e5e5e5;
  --black: #2b2d42;
  --white: #fff;
  --thumb: #edf2f4;
}
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
body {
  font: 16px / 24px "Rubik", sans-serif;
  color: var(--white);
  background: var(--black);
  margin: 50px 0;
}
.container {
  width: 1200px;
  height:600px;
  padding: 0 15px;
  margin: 0 auto;
}
h2 {
  font-size: 50px;
  margin-bottom: 1em;
  text-align : center;
}
.cards {
    width: 1200px;
  height:500px;
  display: flex;
  padding: 25px 0px;
  list-style: none;
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
}
.card img {
			width: 250px;
			height: 150px;
			object-fit: cover;
			margin-bottom: 10px;
			border-radius: 4px;
}
.card {
    width: 1200px;
  height:400px;
  display: flex;
  flex-direction: column;
  flex: 0 0 100%;
  padding: 20px;
  background: var(--black);
  border-radius: 12px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 15%);
  scroll-snap-align: start;
  transition: all 0.2s;
}
.card:not(:last-child) {
  margin-right: 10px;
}
.card:hover {
  color: var(--white);
  background:#fe8267;
}
.card .card-title {
  font-size: 20px;
}
.card .card-content {
  margin: 20px 0;
  max-width: 85%;
}
.card .card-link-wrapper {
  margin-top: auto;
}
.card .card-link {
  display: inline-block;
  text-decoration: none;
  color: white;
  background: var(--red);
  padding: 6px 12px;
  border-radius: 8px;
  transition: background 0.2s;
}
.card:hover .card-link {
  background: var(--darkred);
}
.cards::-webkit-scrollbar {
  height: 12px;
}
.cards::-webkit-scrollbar-thumb,
.cards::-webkit-scrollbar-track {
  border-radius: 92px;
}
.cards::-webkit-scrollbar-thumb {
  background: var(--darkred);
}
.cards::-webkit-scrollbar-track {
  background: var(--thumb);
}
@media (width: 200%) {
  .card {
    flex-basis: calc(50% - 10px);
  }
  .card:not(:last-child) {
    margin-right: 20px;
  }
}
@media (min-width: 700px) {
  .card {
    flex-basis: calc(calc(100% / 3) - 20px);
  }
  .card:not(:last-child) {
    margin-right: 30px;
  }
}
@media (min-width: 1100px) {
  .card {
    flex-basis: calc(25% - 30px);
  }
  .card:not(:last-child) {
    margin-right: 40px;
  }
}
/* FOOTER STYLES
–––––––––––––––––––––––––––––––––––––––––––––––––– */
.page-footer {
  position: fixed;
  right: 0;
  bottom: 50px;
  display: flex;
  align-items: center;
  padding: 5px;
  z-index: 1;
}
.page-footer a {
  display: flex;
  margin-left: 4px;
}
</style>
""",unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

#Rating webpage
st.markdown("""<html>
<head>
	<title>Rating Page</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			background-color: #f7f7f7;
		}
		h1 {
			text-align: center;
			margin-top: 40px;
		}
		.rating {
			display: flex;
			flex-direction: row-reverse;
			justify-content: center;
			align-items: center;
			font-size: 60px;
			color: #ffd700;
			margin-top: 60px;
		}
		.rating > label {
			margin: 0 15px;
			cursor: pointer;
		}
		.rating > label:hover,
		.rating > label:hover ~ label {
			color: #f5bc42;
		}
		.rating > input:checked ~ label {
			color: #f5bc42;
		}
		.rating > input:checked ~ label:hover,
		.rating > input:checked ~ label:hover ~ label {
			color: #ffd700;
		}
		.submit-button {
			display: block;
			margin-top: 60px;
			padding: 10px 20px;
			background-color: #007bff;
			color: #fff;
			font-size: 24px;
			font-weight: bold;
			border: none;
			border-radius: 5px;
			cursor: pointer;
		}
	</style>
</head>
<body>
	<h1>Rate our WebPage</h1>
	<div class="rating">
		<input type="radio" id="star5" name="rating" value="5" /><label for="star5">&#9733;</label>
		<input type="radio" id="star4" name="rating" value="4" /><label for="star4">&#9733;</label>
		<input type="radio" id="star3" name="rating" value="3" /><label for="star3">&#9733;</label>
		<input type="radio" id="star2" name="rating" value="2" /><label for="star2">&#9733;</label>
		<input type="radio" id="star1" name="rating" value="1" /><label for="star1">&#9733;</label>
	</div>
	<button class="submit-button">Submit</button>
</body>
</html>""",unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)  

images = ["https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/HeroHomepage_2880x1200.jpg"]

image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:20%; height:20%; object-fit: cover; display: block;margin-right: auto; margin-left: auto;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
st.markdown("<br><hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------------------------------------------------------------------
# Removing 'made with streamlit'
# ------------------------------
hide_st_style = """ <style>footer{visibility:hidden;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)

#insta whatsapp twitter email
st.markdown(
    """
    <style>
    .icon-container {
        bottom: 20px;
        right: 20px;
    }
    .icon-container a {
        margin-left: 10px;
    }
    </style>
    """,unsafe_allow_html=True
)

st.markdown(
    """
    <div class="icon-container">
      <a href="#" onclick="showAccount('instagram')"><img src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/instagram_circle-512.png" width="30" height="30"></a>
      <a href="#" onclick="showAccount('whatsapp')"><img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-whatsapp-circle-512.png" width="30" height="30"></a>
      <a href="#" onclick="showAccount('twitter')"><img src="https://cdn3.iconfinder.com/data/icons/social-icons-5/607/Twitterbird.png" width="30" height="30"></a>
      <a href="#" onclick="showAccount('mail')"><img src="https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/gmail-512.png" width="30" height="30"></a>
    </div>
    """,
    unsafe_allow_html=True
)

