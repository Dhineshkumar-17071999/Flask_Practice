# Building URL Dynamically
# Variable rule and URL Building

from flask import Flask, redirect,url_for # redirect & url_for -> building url dynamically 
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello All'

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The person has passed</h2></body></html>" # not good approach

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has fail and the mark is '+str(score)

@app.route('/results/<int:mark>')
def results(mark):
    result = ""
    if mark < 50:
        result = 'fail'
    else:
        result = 'success'
        
    return redirect(url_for(result, score = mark))

if __name__ == "__main__":
    app.run(debug = True)