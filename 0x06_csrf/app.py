from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hola-you will never guess me ^&%$ldk890923'

#the above is how to set a secret key to protect
#to protect against cross site request forgery