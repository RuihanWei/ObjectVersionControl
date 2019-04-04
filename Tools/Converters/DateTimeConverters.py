import datetime

def pyDT_TO_MysqlDT(datetimeI):
  return datetimeI.strftime("%Y-%m-%d %H:%M:%S")

def MysqlDT_TO_PyDT(datetimeStr):
  return datetime.strptime(datetimeStr, "%Y-%m-%dT%H:%M:%S")
