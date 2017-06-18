"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
import mlab
from mongoengine import *
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

mlab.connect()

class Item(Document):
    image = StringField()
    title = StringField()
    link = StringField()
    describtion = StringField()

item1 = Item( image =  "http://pics.dmm.co.jp/mono/movie/adult/1star606/1star606ps.jpg"
              ,title = "STAR-606",
              link = "http://www.javlibrary.com/en/?v=javliir44m",
              describtion = "Repeat Senna Matsuoka ... Kiss Instinct Bare Thick 4 Sex"
              )

# item1.save()


###
# Routing for your application.
###


items = [
    {
        "image": "http://lpjp-dunebuggysrl.netdna-ssl.com/media/catalog/product/LCI/Gb/4L/U6EaumnQPaAuYvkq7-w-i-V09RyV0SkLRlceNaJ7ImRzIjoic21hbGxfaW1hZ2UiLCJmIjoiXC9DXC9GXC9JXC9MXC9QXC9EXC85XC8wXC82XC83XC82XC8wXC9DRklMUEQ5MDY3NjBfTlIwMDAyXzEwMF8xLmpwZyIsImZhIjoxLCJmZiI6MSwiZmgiOjYwMSwiZnEiOjkwLCJmdCI6MSwiZnciOjQxMH0~.jpg"
        ,"title": "Bodice"
        ,"price": "1335"
    },

    {
        "image":"http://lpjp-dunebuggysrl.netdna-ssl.com/media/catalog/product/LCI/kx/VK/Grj4NVrJjagbdhpfg40LwlAhOtDfjociKGw6ktl7ImRzIjoic21hbGxfaW1hZ2UiLCJmIjoiXC9DXC9GXC9JXC9MXC9QXC9EXC8wXC8wXC8yXC8yXC85XC81XC9DRklMUEQwMDIyOTU1X05SMDAwMl8xMDBfMS5qcGciLCJmYSI6MSwiZmYiOjEsImZoIjo2MDEsImZxIjo5MCwiZnQiOjEsImZ3Ijo0MTB9.jpg"
        ,"title":"Thong in"
        ,"price": "234"
    },

    {
        "image":"http://lpjp-dunebuggysrl.netdna-ssl.com/media/catalog/product/LCI/Bc/B4/swCYODnJGzU4cfprkDL-ifgzM1NNMNZY832oUV97ImRzIjoic21hbGxfaW1hZ2UiLCJmIjoiXC9DXC9GXC9JXC9MXC9QXC9EXC8wXC8wXC8yXC8yXC85XC81XC9DRklMUEQwMDIyOTUwX05SMDAwMl8xMDAuanBnIiwiZmEiOjEsImZmIjoxLCJmaCI6NjAxLCJmcSI6OTAsImZ0IjoxLCJmdyI6NDEwfQ~~.jpg"
        ,"title": "Crepe-de-chine"
        ,"price": "813"
    }
]

@app.route('/')
def index():
    return render_template("index.html", items = Item.objects() )


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


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
    # app.run(debug=True)  => làm sever restart => chạy 2 lần
    app.run()
