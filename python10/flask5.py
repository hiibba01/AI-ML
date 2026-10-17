#Building URL Dynamically, variables rule and jinja 2 template engine

from flask import Flask, render_template,request, redirect, url_for


app = Flask(__name__)  

@app.route("/")
def welcome():
    return "<html><H2>Welcome to this application....</H2></html>"

@app.route("/about", methods = ['GET'])
def about():
    return render_template("index.html ")


# @app.route('/submit', methods = ['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         return f"Form submitted! Name: {name}, Email: {email}"
#     return render_template("form.html")  

#Variable rule
@app.route('/success/<int:score>')
def success(score):
    # return "The marks you obtained is "+ str(score)  
    #by default the score val is string
    res = ""
    if score < 50:
        res = "failed"
    else:
        res = "passed"
    return render_template("result.html", results = res)    

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score < 50:
        res = "failed"
    else:
        res = "passed"
    exp={'score':score,'result':res}   #key:value pair , so for condition

    return render_template("result1.html", results = exp)  


@app.route('/successif/<int:score>')
def successif(score):
     

    return render_template("result.html", results = score)   #using if statement here

#building url dynamically by using url_for
@app.route('/fail/<int:score>')
def fail(score):
    
    
    return render_template("result.html", results = score) 

@app.route('/submit', methods = ['GET', 'POST'])
def get_result():
    total_score = 0
    if request.method == 'POST':
        Science = float(request.form['Science'])
        Maths = float(request.form['Maths'])
        English = float(request.form['English'])
        History = float(request.form['History'])

        total_score = (Science + Maths + English + History)/4
        return redirect(url_for('successres', score=total_score)) #redirecting to successres page with score    
    return render_template('getresult.html')


if __name__ == "__main__":  
    app.run(debug=True) 


#ways to read from jinja2 template engine
'''
1- {{ }} - for expressions to print to the template output
2- {% %} - for statements, like for loops and if statements
3- {# #} - for comments not included in the template output'''    