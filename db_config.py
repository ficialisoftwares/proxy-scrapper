from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'maazqkxy_dev'
app.config['MYSQL_DATABASE_PASSWORD'] = '#KyQM#T(Gc4E'
app.config['MYSQL_DATABASE_DB'] = 'maazqkxy_proxy_host'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_PORT'] = 5522
mysql.init_app(app)
