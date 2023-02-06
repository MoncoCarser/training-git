from flask import Flask, redirect
from datetime import datetime

app = Flask(__name__)

date = datetime.today().strftime("%d/%b")

@app.route("/")
def index():
    my_name = "Michael Jordan"
    page = ""
    f = open("template/portfolio.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{my_name}", my_name)
    page = page.replace("{date}", date)
    page = page.replace("{blog_text}", "Entry page for blog!")
    return page

@app.route("/blog/first_blog")
def first():
    return redirect("/first_blog")

@app.route("/blog/second_blog")
def second():
    return redirect("/second_blog")

@app.route('/first_blog')
def first_blog():
    my_name = "Pasi"
    writing_date = "25th May"
    page = ""
    f = open("template/portfolio.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{my_name}", my_name)
    page = page.replace("{date}", writing_date)
    page = page.replace("{blog_text}", "My first blog. Thought I'd just write a sentence. Bye!")
    return page

@app.route('/second_blog')
def second_blog():
    my_name = "Pasi"
    writing_date = "25th NEVERRRR"
    page = ""
    f = open("template/portfolio.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{my_name}", my_name)
    page = page.replace("{date}", writing_date)
    page = page.replace("{blog_text}", "My second blog. Feeling tired. I should head to bed soon zZZZ")
    return page

app.run(host='0.0.0.0', port=81)
