"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


###
# Routing for your application.
###
@app.route('/')
def home():
    return "Hello cưng, đây là homepage"

@app.route('/about')
def about():
    return "About CCCC"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    c = a + b
    return "{0} em ạ, hỏi ccc".format(c)

@app.route("/html-sample")
def html_sample():
    return render_template("sample.html")  #serve html

@app.route("/school")
def school():
    pass

@app.route("/bai2")
def html_bai_2():
    return render_template("bai_2.html")

@app.route("/bmi/<int:w>/<float:h>")
# CÔNG THỨC TÍNH CHỈ SỐ BMI = Cân nặng (kg) / ( Chiều cao(m)* Chiều cao(m))

def bmi( w, h):
    bmi = w/ h
    notice = "XXX"
    if bmi < 16:
        notice = "Bạn bị còi xương."
    elif bmi <= 18.5:
        notice = "Bạn bị thiếu cân"
    elif bmi <= 25:
        notice = "Cơ thể bạn hoàn toàn bình thường"
    elif bmi <= 30:
        notice = "Bạn bị thừa cân"
    else:
        notice = "Bạn bị béo phì"
    return "Chỉ số BMI của bạn là {0},\n {1}".format(bmi, notice)
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
