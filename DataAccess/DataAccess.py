#!/usr/bin/python
import MySQLdb
import mysql.connector
import Tools.Converters.DateTimeConverters as dateTimeConverters

import datetime

# potential ORM
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

# Base = declarative_base()
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rienwave1@localhost/ObjectVC'
# db = SQLAlchemy(app)

# cursor.execute("CREATE TABLE objects (id INT AUTO_INCREMENT PRIMARY KEY, label VARCHAR(255), confidence FLOAT)")

# todo: add Bleach
# todo: further protection against injection

class DataAccess:
  def __init__(self):
    self.db = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="rienwave1",
      database="ObjectVC"
    )
    self.cursor = self.db.cursor()

  def InsertImage(self, identifier, currentTime):
    # self.cursor.execute("DELETE FROM images WHERE id = 1")
    current_time = dateTimeConverters.pyDT_TO_MysqlDT(currentTime)

    sqlStr = "INSERT INTO images (identifier, datetime) VALUES (%s, %s)"
    val = (identifier, current_time)
    self.cursor.execute(sqlStr, val)
    last_id = self.cursor.lastrowid
    self.db.commit()
    return last_id

    # reverse
    # birthday = datetime.strptime(str(birthday), "%Y-%m-%dT%H:%M:%S")

  def InsertObject(self, image_id, label, confidence, reference_path):
    sqlStr = "INSERT INTO objects (images_id, label, confidence, reference_path) VALUES (%s, %s, %s, %s)"
    val = (image_id, label, confidence, reference_path)
    self.cursor.execute(sqlStr, val)
    last_id = self.cursor.lastrowid
    self.db.commit()
    return last_id

    # def InsertBoundingBox(self, objects_id, midpoint):

  def InsertBoundingBox(self, object_id, midpoint_x, midpoint_y, length, width):
    sqlStr = "INSERT INTO boundingboxes (objects_id, midpoint_x, midpoint_y, length, width) VALUES (%s, %s, %s, %s, %s)"
    val = (object_id, midpoint_x, midpoint_y, length, width)
    self.cursor.execute(sqlStr, val)
    self.db.commit()

  # def FetchByDateTime(self, session_datetime):
  #   sqlStr = "SELECT identifier,  boundingboxes (objects_id, midpoint, length, width) VALUES (%s, %s, %s, %s)"
  #   images =

if __name__ == "__main__":
  dataAccess = DataAccess()
  dataAccess.cursor.execute("DELETE FROM objects; ")
  #dataAccess.db.commit()

  dataAccess = DataAccess()
  dataAccess.cursor.execute("DELETE FROM images; ")
  #dataAccess.db.commit()



  # dataAccess.InsertBoundingBox(3, 20, 100, 100)
  # dataAccess.InsertObject(2, "cup", 0.6, "D:\\")

# cursor.lastrowid   # gets id of last insert

### Reference SQL Commands     TODO: remove after databasehelper is completed

# cursor.execute("CREATE TABLE relations (id INT AUTO_INCREMENT PRIMARY KEY, "
#                "main_objects_id INT, "
#                "relative_objects_id INT, "
#                " clock_position INT, "
#                "distance FLOAT, "
#                "FOREIGN KEY (main_objects_id) REFERENCES objects(id), "
#                "FOREIGN KEY (relative_objects_id) REFERENCES objects(id))")

# cursor.execute("DROP TABLE relations")

# cursor.execute("ALTER TABLE relations "
# #                "ADD COLUMN _right FLOAT, "
# #                "ADD COLUMN _left FLOAT "
# #                ";")

# cursor.execute("ALTER TABLE relations "
# #                "ADD COLUMN _right FLOAT, "
# #                "ADD COLUMN _left FLOAT "
# #                ";")

# cursor.execute("ALTER TABLE objects "
#                "ADD COLUMN reference_path VARCHAR(255);")

# cursor.execute("DROP TABLE objects")

# cursor.execute("CREATE TABLE images (id INT AUTO_INCREMENT PRIMARY KEY, identifier VARCHAR(255), datetime DATETIME)")

# cursor.execute("CREATE TABLE relations (id INT AUTO_INCREMENT PRIMARY KEY, objects_id INT, clock_position INT, "
#                "distance FLOAT, FOREIGN KEY (objects_id) REFERENCES objects(id))")

# cursor.execute("CREATE TABLE relations (id INT AUTO_INCREMENT PRIMARY KEY, objects_id INT, "
#               "midpoint VARCHAR(255), length FLOAT, width FLOAT,"
#               "FOREIGN KEY (objects_id) REFERENCES objects(id))")

# cursor.execute("CREATE TABLE boundingboxes (id INT AUTO_INCREMENT PRIMARY KEY, objects_id INT, midpoint VARCHAR(255), length FLOAT, width FLOAT,"
#               "FOREIGN KEY (objects_id) REFERENCES objects(id))")

# cursor.execute("CREATE TABLE objects (id INT AUTO_INCREMENT PRIMARY KEY, images_id INT, label VARCHAR(255), confidence FLOAT,"
#               "FOREIGN KEY (images_id) REFERENCES images(id))")

# cursor.execute("CREATE TABLE objects (id INT AUTO_INCREMENT PRIMARY KEY, label VARCHAR(255), confidence FLOAT)")

# cursor.execute("CREATE DATABASE ObjectVC")
# cursor.execute("DROP TABLE objects")

# class ObjectVcConnector:
# def __init__(self):

# def insert(self, label, confidence):
#  cursor = db.cursor()
#  sql = "INSERT INTO objects (label, confidence) VALUES (%s, %s)"
#  val = (label, confidence)
#  cursor.execute(sql, val)

# class Objects():
#   __tablename__ = 'objects'
#   id = Column('id', Integer, primary_key=True)
#   label = db.Column('data', String(32))
