from flask import Flask


app = Flask(__name__)

from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'navgurukul'
app.config['MYSQL_DATABASE_DB'] = 'eunimart_detail'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)