
# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask
from flask import render_template
from flask import request, render_template
from urllib.request import urlopen
from json import load
import pandas as pd
import csv
from flask import send_file
import speedtest
from hurry.filesize import size


app = Flask(__name__)
path = 'userinfoToCsv.bat'

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.form:
        username = request.form.get('userName')

        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()

        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        url = 'https://ipinfo.io/' + ip + '/json'
        res = urlopen(url)
        data = load(res)
        for attr in data.keys():
            if attr == 'country':
                country = data[attr]
            if attr == 'region':
                region = data[attr]
            if attr == 'city':
                city = data[attr]
            if attr == 'ip':
                ip = data[attr]

        response = {
            'name': username,
            'ip': ip,
            'country': country,
            'city': city,
            'region': region
        }
        response = {
            'name': 'abc',
            'ip': '192',
            'country': 'India',
            'city': 'Mumbai',
            'region': 'maha',
            'download': size(int(res["download"]))
        }
        return render_template("viewPage.html", user_info=response)
    return render_template("input_name.html")


@app.route("/downloadlogfile")
def DownloadLogFile():
    return send_file(path, as_attachment=True)