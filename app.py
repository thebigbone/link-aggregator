from flask import Flask, render_template, request
from database import configure_mysql, mysql

app = Flask(__name__)
configure_mysql(app)


@app.route('/add', methods=['GET', 'POST'])
def add():
    msg = ''
    if request.method == 'POST':
        try:
            name = request.form['name']
            links = request.form['links']
            date = request.form['date']
            category = request.form['category']

            cursor = mysql.connection.cursor()

            check_comma = is_comma_separated(name)

            if check_comma:
                name_split = name.split(",")
                links_split = links.split(",")

                for n, l in zip(name_split, links_split):
                    sql = f"INSERT IGNORE INTO links.{category} (name, date, link) VALUES (%s, %s, %s)"
                    values = (n, date, l)
                    cursor.execute(sql, values)
                    mysql.connection.commit()
            else:
                sql = f"INSERT IGNORE INTO links.{category} (name, date, link) VALUES (%s, %s, %s)"
                values = (name, date, links)

                cursor.execute(sql, values)
                mysql.connection.commit()

            print(name)
            msg = 'Links added!'
            return render_template('add.html', msg=msg)
        except Exception as e:
            error = f"something went wrong: {e}"
            return render_template('add.html', error=error)

    return render_template('add.html')


@app.route('/')
@app.route('/links')
def index():
    result = get_links('links')

    return render_template('home.html', result=result)


@app.route('/papers')
def papers():
    result = get_links('papers')

    return render_template('papers.html', result=result)


@app.route('/books')
def books():
    return render_template('books.html')


def get_links(table_name):
    cursor = mysql.connection.cursor()

    cursor.execute(f'select * from links.{table_name} ORDER BY id DESC')
    result = cursor.fetchall()

    return result


def is_comma_separated(s):
    return len(s.split(",")) > 1


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
