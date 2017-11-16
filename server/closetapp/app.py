import os
from flask import Flask
from models.item import Item
from models.database import db
from responses import api_response, ResponseCodes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://closetapp:123@localhost/closet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Bind the db instance to the app.
db.app = app
db.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/ping')
def ping():
    return api_response(code=ResponseCodes.SUCCESS, data='you won')


@app.route('/item/bottom_top/<bottom_top_param>')
def get_tops(bottom_top_param):
    items = Item.query.filter(Item.bottom_top == bottom_top_param).all()
    item_serialized = [item.serialize for item in items]

    return api_response(code=ResponseCodes.SUCCESS, data=item_serialized)

if __name__ == '__main__':
    app.run(debug=True)
