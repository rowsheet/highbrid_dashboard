from flask import Flask, request, render_template, jsonify, send_from_directory
import json
import os
import requests
import base64
app = Flask(__name__,template_folder="templates")

@app.route('/public/<path:path>')
def public(path):
    return send_from_directory('public', path)

@app.route("/", methods=["GET", "POST"])
def home():
        return render_template("pages/home.html")

@app.route("/blog", methods=["GET", "POST"])
def blog():
        return render_template("pages/blog.html")
@app.route("/catalog", methods=["GET", "POST"])
def catalog():
        return render_template("pages/catalog.html")
@app.route("/email", methods=["GET", "POST"])
def email():
        return render_template("pages/email.html")
@app.route("/facebook", methods=["GET", "POST"])
def facebook():
        return render_template("pages/facebook.html")
@app.route("/instagram", methods=["GET", "POST"])
def instagram():
        return render_template("pages/instagram.html")
@app.route("/inventory", methods=["GET", "POST"])
def inventory():
        return render_template("pages/inventory.html")
@app.route("/loyalty_members", methods=["GET", "POST"])
def loyalty_members():
        return render_template("pages/loyalty_members.html")
@app.route("/metrc", methods=["GET", "POST"])
def metrc():
        return render_template("pages/metrc.html")
@app.route("/orders_and_sales", methods=["GET", "POST"])
def orders_and_sales():
        return render_template("pages/orders_and_sales.html")
@app.route("/pages", methods=["GET", "POST"])
def pages():
        return render_template("pages/pages.html")
@app.route("/promotions", methods=["GET", "POST"])
def promotions():
        return render_template("pages/promotions.html")
@app.route("/seo", methods=["GET", "POST"])
def seo():
        return render_template("pages/seo.html")
@app.route("/subscribers", methods=["GET", "POST"])
def subscribers():
        return render_template("pages/subscribers.html")
@app.route("/text", methods=["GET", "POST"])
def text():
        return render_template("pages/text.html")
@app.route("/yelp", methods=["GET", "POST"])
def yelp():
        return render_template("pages/yelp.html")

#-------------------------------------------------------------------------------
# Demo pages.
#-------------------------------------------------------------------------------

@app.route("/demo/home", methods=["GET", "POST"])
def demo_home():
        return render_template("pages/demo/home.html", foo="Foo")

@app.route("/demo/buttons", methods=["GET", "POST"])
def demo_buttons():
        return render_template("pages/demo/buttons.html")

@app.route("/demo/cards", methods=["GET", "POST"])
def demo_cards():
        return render_template("pages/demo/cards.html")

@app.route("/demo/colors", methods=["GET", "POST"])
def demo_colors():
        return render_template("pages/demo/colors.html")

@app.route("/demo/borders", methods=["GET", "POST"])
def demo_borders():
        return render_template("pages/demo/borders.html")

@app.route("/demo/animations", methods=["GET", "POST"])
def demo_animations():
        return render_template("pages/demo/animations.html")

@app.route("/demo/other", methods=["GET", "POST"])
def demo_other():
        return render_template("pages/demo/other.html")

@app.route("/demo/login", methods=["GET", "POST"])
def demo_login():
        return render_template("pages/demo/login.html")

@app.route("/demo/register", methods=["GET", "POST"])
def demo_register():
        return render_template("pages/demo/register.html")

@app.route("/demo/forgot-password", methods=["GET", "POST"])
def demo_forgot_password():
        return render_template("pages/demo/forgot_password.html")

@app.route("/demo/404", methods=["GET", "POST"])
def demo_not_found():
        return render_template("pages/demo/404.html")

@app.route("/demo/blank-page", methods=["GET", "POST"])
def demo_blank_page():
        return render_template("pages/demo/blank_page.html")

@app.route("/demo/charts", methods=["GET", "POST"])
def demo_charts():
        return render_template("pages/demo/charts.html")

@app.route("/demo/tables", methods=["GET", "POST"])
def demo_tables():
        return render_template("pages/demo/tables.html")

@app.route("/ping", methods=["POST", "GET"])
def ping():
        print("got ping")
        return "pong"

if __name__ == "__main__":
        app.run(
                host= "0.0.0.0",
                port=5400,
                debug=True
        )
