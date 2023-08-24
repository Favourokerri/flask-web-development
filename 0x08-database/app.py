from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
app = Flask(__name__)

# Replace with your MySQL database credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:helvericawhite@localhost/learn_flask'
app.config['SECRET_KEY'] = '%64you-can-try%%-to-$$getme'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

#Models definition one to many relationship
class Roles(db.Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    
    users = db.relationship('User', backref='role')

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(128), nullable=False)
    role_id = Column(Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %s>' % self.username

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run('0.0.0.0', port=5000, debug=True)