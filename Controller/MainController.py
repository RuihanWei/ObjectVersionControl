import os

from flask import Flask, request, url_for, render_template
import datetime

from werkzeug.utils import redirect

from Controller import ControllerTools

template_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View/')
static_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View/static/')
app = Flask(__name__, template_folder=template_folder, static_url_path="/static", static_folder=static_folder)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
  # error = None
  # if request.method == 'POST':
  #   if request.form['username'] != 'admin' or request.form['password'] != 'admin':
  #     error = 'Invalid Credentials. Please try again.'
  #   else:
  #     return redirect(url_for('login'))
  return render_template('/login_form/LoginTemplate.html')#, error=error)


@app.route('/SelectionPage')
def sessionRequest():
  session1_datetime = datetime.datetime(2019, 4, 1, 23, 58, 25)
  session2_datetime = datetime.datetime(2019, 4, 3, 1, 26, 18)
  ComprisonList = ControllerTools.Diff(session1_datetime, session2_datetime)
  output = ''
  for comparison in ComprisonList:
    output += comparison
    output += '</br>'
  return output


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=5000)
