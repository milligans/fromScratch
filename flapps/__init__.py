from flask import Flask
from flask_login import LoginManager
from flask_mysqldb import MySQL





app = Flask(__name__)




if __name__ == "__main__":
    app.run()

# userpass = 'mysql+pymysql://root:@'
# basedir  = '127.0.0.1'
# dbname   = '/flask'
# socket   = '?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
# dbname   = dbname + socket
# app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/flask'
db = MySQL(app)
# login_manager=LoginManager()
# login_manager.init_app(app)


from flapps import routes



