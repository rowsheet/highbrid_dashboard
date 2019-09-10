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

@app.route("/customers", methods=["GET", "POST"])
def customers():
        return render_template("pages/customers_overview.html")

@app.route("/social-media", methods=["GET", "POST"])
def social_media_overview():
        return render_template("pages/social_media_overview.html")

@app.route("/sales", methods=["GET", "POST"])
def sales_overview():
        return render_template("pages/sales_overview.html")

@app.route("/storefront", methods=["GET", "POST"])
def storefront_overview():
        return render_template("pages/storefront_overview.html")

@app.route("/inventory", methods=["GET", "POST"])
def inventory_overview():
        return render_template("pages/inventory_overview.html")

@app.route("/operations", methods=["GET", "POST"])
def operations_overview():
        return render_template("pages/operations_overview.html")

@app.route("/analytics", methods=["GET", "POST"])
def analytics_overview():
        return render_template("pages/analytics_overview.html")

@app.route("/integrations", methods=["GET", "POST"])
def integrations_overview():
        return render_template("pages/integrations_overview.html")

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
