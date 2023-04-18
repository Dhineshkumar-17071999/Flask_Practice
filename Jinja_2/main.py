# Integrate HTML with flask -> Ginja 2 technique (You will be having a seperate data source you can integrate with the html however you want)
# HTTP verb GET and POST

# Jinja2 template engine

'''
{%...%} conditions, for loops
{{   }} expressions to print output
{#...#} this is for comments
'''
from flask import Flask, redirect,url_for,render_template,request # redirect & url_for -> building url dynamically, request -> read posted values 
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    exp = {'score':score,'res':res}
    return render_template('result.html', result = exp)

@app.route('/fail/<int:score>')
def fail(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', result = res)

@app.route('/results/<int:mark>')
def results(mark):
    result = ""
    if mark < 50:
        result = 'fail'
    else:
        result = 'success'
        
    return redirect(url_for(result, score = mark))
# Result checker submit HTML page
@app.route('/submit', methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    res = ""
    if total_score >= 50:
        res = "success"
    else:
        res = "fail"
    
    return redirect(url_for("success", score = total_score))
    

if __name__ == "__main__":
    app.run(debug = True)