### install requirements
```pip install -r requirements```

### create database.py
```python
    
from flask_mysqldb import MySQL

mysql = MySQL()


def configure_mysql(app):
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'

    mysql.init_app(app)
```

### create database schema from database.txt

### run
```flask run```
