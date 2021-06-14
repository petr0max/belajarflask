from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'udin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool'
        }
    ]
    return render_template('index.html', title='Beranda', user=user, posts=posts)
