
from flask import Flask, render_template, request, redirect
from scanner import scan
from database import init_db, save_scan, get_scans

app=Flask(__name__)
init_db()

@app.route("/",methods=["GET","POST"])
def home():
    result=None
    if request.method=="POST":
        url=request.form["url"]
        result=scan(url)
        save_scan(url, ", ".join(result))
    return render_template("index.html", result=result)

@app.route("/history")
def history():
    return render_template("history.html", scans=get_scans())

app.run(host="0.0.0.0",port=5000)
