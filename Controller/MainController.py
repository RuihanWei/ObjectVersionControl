from flask import Flask, request
import datetime

from Controller import ControllerTools

app = Flask(__name__)


@app.route('/')
@app.route('/diff')
def HelloWorld():
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
