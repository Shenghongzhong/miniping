from flask import Flask, render_template, request
# the request above is from Flask
# the requests below is another library name
import requests
import time

app = Flask(__name__)

@app.route("/")
def home():
    

    panels = [
        {"title":"My LinkedIn",'url':"https://www.linkedin.com/in/shenghongzhong/"}, 
        {"title":"My Medium",'url':'https://medium.com/@shenghongzhong'},
        {"title":" My Jovian Profile",'url':'https://jovian.ai/shenghongzhong'},
        {'title':'My Twitter','url':'https://twitter.com/ShenghongZhong'}
        ]

    return render_template("home.html",panels=panels)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/ping')
def ping():
    url = request.args.get("url")
    
    start_time = time.time()

    r = requests.get(url)
    end_time = time.time()

    diff_time = int((end_time - start_time) * 1000)
    return {
        "url":url,
        "code":r.status_code,
        "speed":diff_time
        }
