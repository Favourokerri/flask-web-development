from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
app = Flask(__name__)

# Replace with your MySQL database credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:helvericawhite@localhost/learn_flask'
app.config['SECRET_KEY'] = '%64you-can-try%%-to-$$getme'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

#Models definition
class Roles(db.Model):
    __tablename__ = 'Roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

class User(db.Model):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)

    def __repr__(self):
        return '<User %s>' % self.username

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run('0.0.0.0', port=5000, debug=True)