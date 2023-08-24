from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from datetime import datetime

app = Flask(__name__)

# Replace with your MySQL database credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:helvericawhite@localhost/learn_sqlalchemy'
app.config['SECRET_KEY'] = '%64you-can-try%%-to-$$geoiu6tme'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
# db.init_app(app)

class Customer(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address = Column(String(500), nullable=False)
    city = Column(String(50), nullable=False)
    postcode = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    orders = db.relationship('Orders', backref='customer')

order_product = db.Table('order_product',
    Column('order_id', Integer, ForeignKey('orders.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True)
)

class Order(db.Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    shipped_date = Column(DateTime)
    delivery_date = Column(DateTime)
    coupon_code = Column(String(50))
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)

    products = db.relationship('Product', secondary=order_product)

class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Integer)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run('0.0.0.0', port=5000, debug=True)
