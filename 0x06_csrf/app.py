from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hola-you will never guess me ^&%$ldk890923'

#the above is how to set a secret key to protect
#against cross site request forgery
# in the future we will store this secret key in an 
# environmental variable instaed of just passing it this way