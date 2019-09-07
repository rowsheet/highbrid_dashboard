from flask import Flask, request, render_template, jsonify
import json
import os
import requests
import base64
app = Flask(__name__,template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def home():
        return render_template("pages/home.html", foo="Foo")

@app.route("/customers", methods=["GET", "POST"])
def customers():
        return render_template("pages/customers.html", foo="Foo")

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
