import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user_registration import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

#test
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'wow'
api = Api(app)
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)
db.init_app(app)
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

if __name__ == '__main__':

    app.run(debug=True)
