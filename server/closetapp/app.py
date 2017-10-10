from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'App is running on port 5000!'


if __name__ == '__main__':
	app.run()