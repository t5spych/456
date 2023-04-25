from collections import namedtuple
import os

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route('/', methods=['GET', 'POST'])
def hw():
    return render_template('baza.html')


@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/napit', methods=['GET', 'POST'])
def napit():
    return render_template('napit.html')


@app.route('/kont', methods=['GET', 'POST'])
def kont():
    return render_template('kont.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')