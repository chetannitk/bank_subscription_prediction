import socket
import re
import json
import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import os
from flask import Flask, render_template, url_for, request, Markup, jsonify
from flask_script import Manager

app = Flask(__name__)
df = pd.read_csv("./data/bank-additional/bank-additional-full.csv", sep=";")

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/_get_observation')
def get_observation():
    return jsonify(result = df.shape[0])

@app.route('/_get_subscriber_count')
def get_subscriber_count():
    return jsonify(result = df[df.y=="yes"].shape[0])

@app.route('/get_profile_report')
def get_profile_report():
    return render_template('profile_report.html')

@app.route('/get_chart')
def get_chart():
    return render_template('charts.html')

@app.route('/chart1')
def chart1():
    data = json.dumps(df_list)
    return render_template('charts.html', data=data)


if __name__ == '__main__':
    app.run()
