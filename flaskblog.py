from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


@app.route("/blog")
def blog():
	return render_template('blog.html')


@app.route("/contact")
def contact():
	return render_template('contact.html')


@app.route("/portfolio")
def portfolio():
	return render_template('portfolio.html')




if __name__ == '__main__':
	app.run(debug=True) 