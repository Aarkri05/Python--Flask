import math
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/good')
def main():
    return render_template('j1.html')

@app.route('/process', methods=['POST'])
def process():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    a=float(request.form.get('first'))# get(attr) returns None if attr is not present
    b=float(request.form.get('second'))
    #c=float(request.form.get('third'))
    #d=float(request.form.get('fourth'))
    
    #if 'blue' in request.form:
    additi=add(a, b)
    return render_template('j2.html', **locals())
  
def additi(a, b):
    addition=a+b
    return addition



if __name__=='__main__':
    app.run(debug=True)
