#Integrating HTML files in this flask application
from flask import Flask, render_template


app = Flask(__name__)  

@app.route("/")
def welcome():
    return "<html><H2>Welcome to this application....</H2></html>"

@app.route("/about")
def about():
    return render_template("index.html ")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":  
    app.run(debug=True)  

    #the index.html file is present in the templates folder, so we can use render_template() function to render the HTML file.
