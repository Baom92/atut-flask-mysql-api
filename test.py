#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 11:07:36 2023

@author: baom
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/hello/<string:name>", methods=["GET", "POST"])
def hello(name):
    data = {
        "message": "Hello ATUT World from "+name
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
