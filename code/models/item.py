from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(12))
    price= db.Column(db.Float(precision = 2))
    count = db.Column(db.Integer,default=0)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store= db.relationship('StoreModel')

    def __init__(self,name, price, store_id,count):
        self.name = name
        self.price = price
        self.store_id = store_id
        self.count = count

    def json(self):
        return {'name': self.name, 'price': self.price, 'count': self.count}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_name_and_store(cls, name,store_id):
        return cls.query.filter_by(name=name).filter_by(store_id=store_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
