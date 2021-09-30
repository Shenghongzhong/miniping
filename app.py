from flask import Flask, render_template, request
# the request above is from Flask
# the requests below is another library name
import requests
import time

app = Flask(__name__)

@app.route("/")
def home():
    

    panels = [
        {"title":"SuperHi API",'url':"https://api.superhi.com"}, 
        {"title":"SuperHi Editor",'url':'https://editor.superhi.com'},
        {"title":" Superhi Website",'url':'https://superhi.com'},
        {'title':'BBC News','url':'https://www.bbc.com/news'}
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
