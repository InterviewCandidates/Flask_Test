from flask import render_template, redirect
from . import app, db
from .model import Interview, Interviewee
from .data_setup import do_setup

do_setup()


@app.route('/')
def index():
    return redirect('/interviewee/')


@app.route('/interviewee/')
def get_interviewees():
    interviewees = db.session.query(Interviewee).all()
    return render_template('interviewee.html', interviewees=interviewees)

"""
Create an interview endpoint below. This endpoint should display information about interviews.

Can you show the interviewee's name?
"""






if __name__ == '__main__':
    app.run()
