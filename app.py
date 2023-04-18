from flask import Flask
# WSGI Application
app = Flask(__name__)

@app.route('/') # Decorator
def welcome():
    return 'Welcome world'

@app.route('/member') # Decorator
def member():
    return 'Hello all members'

if __name__ == "__main__":
    app.run(debug=True)