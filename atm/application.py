from flask import Flask,redirect,render_template,request,url_for,session

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/",methods=['GET','POST'])

def index():
    try:
        balance = session["balance"]
    except KeyError:
        balance = session["balance"] = 8000

    if request.method == "GET":
        return render_template("index.html",balance=balance,msg="")

    if request.method=="POST":
        if request.form["action"]=="Withdraw":
            msg = "Kaat liya na"
            balance = balance-int(request.form["amount"])
            session["balance"] = balance
            return render_template("index.html",balance=balance,msg=msg)
        elif request.form["action"] == "Deposit":
            msg = "Bahut ameer aadmi he"
            balance = balance+int(request.form["amount"])
            session["balance"] = balance
            return render_template("index.html",balance=balance,msg=msg)
if __name__ == '__main__':
    app.run()
