#!/usr/bin/python
import MySQLdb
import mysql.connector

#mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

# Base = declarative_base()
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rienwave1@localhost/ObjectVC'
# db = SQLAlchemy(app)

# cursor.execute("CREATE TABLE objects (id INT AUTO_INCREMENT PRIMARY KEY, label VARCHAR(255), confidence FLOAT)")


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rienwave1",
  database="ObjectVC"
)

cursor = db.cursor()





# cursor.lastrowid   # gets id of last insert















### Reference SQL Commands     TODO: remove after databasehelper is completed

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
