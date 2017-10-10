from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/shuffle')
def shuffle():
	return render_template('shuffle.html')


@app.route('/collage')
def collage():
	return render_template('collage.html')


if __name__ == '__main__':
	app.run(debug=True)