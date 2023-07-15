import streamlit as st 
st.markdown("""<!DOCTYPE html>
<html>
<head>
	<title>Contact Us</title>
	<style>
		body {
			background-color: #f2f2f2;
		}
		h1 {
			color: #4CAF50;
			text-align: center;
		}
		p {
			color: #FFF;
			font-size: 18px;
			line-height: 1.5;
			margin: 20px;
			text-align: center;
		}
		form {
		  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* Add this line to center the form vertically */
  margin: 0 auto; /* Add this line to center the form horizontally */
  margin-top: 50px;
  padding: 20px;
  width: 100%;
  max-width: 1000px;
}
		label {
			color: #333;
			font-size: 16px;
			font-weight: bold;
			margin-top: 10px;
			text-align: left;
			width: 100%;
		}
		input[type="text"], input[type="email"], textarea {
			width: 100%;
			padding: 12px 20px;
			margin: 8px 0;
			box-sizing: border-box;
			border: 2px solid #ccc;
			border-radius: 4px;
			resize: vertical;
			font-size: 16px;
		}
		input[type="text"]:focus, input[type="email"]:focus, textarea:focus {
			border-color: #4CAF50;
			box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
		}
		input[type="submit"] {
			background-color: #4CAF50;
			color: white;
			padding: 14px 20px;
			margin-top: 20px;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			width: 100%;
			font-size: 18px;
			transition: background-color 0.3s ease;
		}
		input[type="submit"]:hover {
			background-color: #388E3C;
		}
		a {
			color: #4CAF50;
			text-decoration: none;
			transition: color 0.3s ease;
		}
		a:hover {
			color: #388E3C;
		}
	</style>
</head>
<body>
	<h1>Contact Us</h1>
	<p>Get in touch with us for any inquiries or feedback.</p>
	<form action="submit-form.php" method="post">
		<label for="name">Name:</label>
		<input type="text" id="name" name="name" required>
		<label for="email">Email:</label>
		<input type="email" id="email" name="email" required>
		<label for="message">Message:</label>
		<textarea id="message" name="message" rows="5" cols="30" required></textarea>
		<input type="submit" value="Submit">
	</form>
	<p>You can also reach us by email at <a href="mailto:jpk@electronics.com">jpk@electronics.com</a>.</p>
	<script>
		const form = document.querySelector('form');
		form.addEventListener('submit', (event) => {
			event.preventDefault();
			const formData = new FormData(event.target);
			fetch(event.target.action, {
				method: 'POST',
				body: formData,
				headers: {
					'Accept': 'application/json'
				}
			})
			.then(response => {
				if (response.ok) {
					alert('Thank you for contacting us!');
					form.reset();
				} else {
					alert('Something went wrong. Please try again later.');
				}
			})
			.catch(error => {
				alert('Something went wrong. Please try again later.');
			});
		});
	</script>
</body>
</html>
""",unsafe_allow_html=True)