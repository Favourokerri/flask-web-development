from flask import Flask, redirect, abort

app = Flask(__name__)

@app.route('/')
def index():
    """this is a redirect function
        this will take you to flask documentaion
    """
    return redirect('https://flask.palletsprojects.com/en/2.3.x/')

@app.route('/custom_abort')
def Custom_abort():
    """this is an abort response"""
    abort(404)

if __name__=="__main__":
    app.run('0.0.0.0', port=5000, debug=True)
