import os

from flask import Flask, request, url_for, render_template, jsonify
import datetime

from werkzeug.utils import redirect, secure_filename

from Controller import ControllerTools

class Session:
  def __init__(self, datetime, identifier):
    self.identifier = identifier
    self.datetime = datetime

  def serialize(self):
    return {self.identifier: self.datetime}


template_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View/templates')
static_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View/static/')
app = Flask(__name__, template_folder=template_folder, static_url_path = '/'+static_folder,static_folder=static_folder)
username = ""


# @app.route('/')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#   global username
#   error = None
#   if request.method == 'POST':
#     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#       print('invalid')
#       error = 'Invalid Credentials. Please try again.'
#       return redirect(url_for('selection'))
#     else:
#       print('valid')
#       print(username)
#       username = request.form['username']
#       return redirect(url_for('selection'))
#   # todo: incorporate error into HTML
#   return render_template('/LoginTemplate.html', error=error)
#
#
# @app.route('/selection')
# def selection():
#   # todo: retrieve from database
#   sessions = []
#   session1_datetime = datetime.datetime(2019, 4, 1, 23, 58, 25)
#   session2_datetime = datetime.datetime(2019, 4, 3, 1, 26, 18)
#   sessions.append(Session(str(session1_datetime), "desk area"))
#   sessions.append(Session(str(session2_datetime), "desk area"))
#   print(username)
#   return render_template('/SelectionView.html', sessions=sessions, username=username)


@app.route('/selection/api')
def selectionapi():
  # todo: retrieve from database
  sessions = []
  session1_datetime = datetime.datetime(2019, 4, 1, 23, 58, 25)
  session2_datetime = datetime.datetime(2019, 4, 3, 1, 26, 18)
  sessions.append(Session(str(session1_datetime), "desk area"))
  sessions.append(Session(str(session2_datetime), "desk area"))
  print(username)
  json_result = jsonify([x.serialize() for x in sessions])
  return json_result
  # return jsonify({'12' : '34'})



@app.route('/diff')
def sessionRequest():
  session1_datetime = datetime.datetime(2019, 4, 1, 23, 58, 25)
  session2_datetime = datetime.datetime(2019, 4, 3, 1, 26, 18)
  ComprisonList = ControllerTools.Diff(session1_datetime, session2_datetime)
  output = ''
  for comparison in ComprisonList:
    output += comparison
    output += '</br>'
  return output

@app.route('/diff/api')
def sessionRequestAPI():
  session1_datetime = datetime.datetime(2019, 4, 1, 23, 58, 25)
  session2_datetime = datetime.datetime(2019, 4, 3, 1, 26, 18)
  ComprisonList = ControllerTools.Diff(session1_datetime, session2_datetime)
  jsonCompare = []
  for i in range(0,len(ComprisonList)):
    jsonCompare.append({"comparison " + str(i) : ComprisonList[i]})
  return jsonify(jsonCompare)



#@app.route('/upload')
@app.route('/')
def upload_file():
  return render_template('/upload.html')


@app.route('/uploader1', methods=['GET', 'POST'])
def uploader():
  if request.method == 'POST':
    f = request.files['file']
    #f.save(secure_filename(f.filename))
    f.save(os.path.join("../View/static", "image1.jpg"))
    return render_template('/upload_image1.html')

@app.route('/uploader2', methods=['GET', 'POST'])
def uploader_image1():
  if request.method == 'POST':
    f = request.files['file']
    f.save(os.path.join("../View/static", "image2.jpg"))
    return render_template('/upload_image2.html')



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=5000)
