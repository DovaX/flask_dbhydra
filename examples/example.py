
#Example Template

from flask import Flask
from flask_mysqldb import MySQL 
from flask_cors import CORS
import dbhydra.dbhydra_core as dm
import flask_dbhydra.flask_dbhydra_core as flaskhydra

app = Flask(__name__)
db1=dm.Mysqldb("config.ini") #Need to specify connection parameters to MySQL DB
db1.close_connection()

app.config['MYSQL_USER'] = db1.DB_USERNAME
app.config['MYSQL_PASSWORD'] = db1.DB_PASSWORD
app.config['MYSQL_DB'] = db1.DB_DATABASE
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'

mysql = MySQL(app)
CORS(app)

TABLE_NAME="users"

item_name="item"
column1_name="column1"
column2_name="column2"

flask_dbhydra_dict={'users':'read','items':'read'}


flaskhydra.initialize_api(app,flask_dbhydra_dict,["name","data","user_id","running"],mysql,column1_name=column1_name)
    
app.run(debug=True)