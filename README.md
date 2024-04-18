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
```
CREATE database links;

CREATE TABLE links, papers, books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    link VARCHAR(255) NOT NULL,
    CONSTRAINT unqiue_fields UNIQUE (name, link)
);

```

### run
```flask run```
