from flask import Flask, redirect, render_template, request, url_for, session
import time
import re  # regular expressions

app = Flask(__name__)

# Secret key for sessions
app.secret_key = "secret"
@app.route("/", methods=['GET', 'POST'])
def index():
    balance = 0
    count=0
    if request.method=="GET":
        return render_template("temp.html",balance=balance,msg="")
    if request.method=="POST":
        if request.form["item1"]!="bread":
            count +=1
            msg = "First item should be bread"
            return render_template("temp.html",balance=balance,msg=msg)
        if request.form["item2"]!="milk":
            count +=1
            msg = "second item should be milk"
            return render_template("temp.html",balance=balance,msg=msg)
        if request.form["item3"]!="ghee":
            count +=1
            msg = "Third Item should be ghee"
            return render_template("temp.html",balance=balance,msg=msg)
        if count==0:
            balance = 40 + 30 + 20
            return render_template("temp.html",balance=balance,msg="Successfully purschased")
if __name__ == '__main__':
    app.run()