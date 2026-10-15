from flask import Flask, render_template,request


app = Flask(__name__)  

@app.route("/")
def welcome():
    return "<html><H2>Welcome to this application....</H2></html>"

@app.route("/about", methods = ['GET'])
def about():
    return render_template("index.html ")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # You can process the form data here (e.g., save it to a database, send an email, etc.)
        return f"Form submitted! Name: {name}, Email: {email}"
    return render_template("form.html")

if __name__ == "__main__":  
    app.run(debug=True) 