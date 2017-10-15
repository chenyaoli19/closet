import os
from flask import Flask, render_template
from models.items import Items
from models.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://closetapp:123@localhost/closet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Bind the db instance to the app.
db.app = app
db.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/shuffle')
def shuffle():
	items = Items.query.all()
	for item in items:
		print(item.category)

	return render_template('shuffle.html')


@app.route('/collage')
def collage():
	return render_template('collage.html')


if __name__ == '__main__':
	app.run(debug=True)