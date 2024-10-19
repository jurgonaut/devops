from flask import render_template, request, url_for, redirect, Blueprint, current_app
from database import get_db_connection

route_blueprint = Blueprint('route_blueprint', __name__)


@route_blueprint.route("/")
def index():
    current_app.logger.debug('Processing route /')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)


@route_blueprint.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM books where title = %s and author = %s', (title, author))
        book = cur.fetchone()
        if book:
            current_app.logger.debug("Book already exists!")
            return redirect(url_for('route_blueprint.index'))
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('route_blueprint.index'))

    return render_template('create.html')


@route_blueprint.route('/delete/', methods=('GET', 'POST'))
def delete():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM books where title = %s and author = %s', (title, author))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('route_blueprint.index'))

    return render_template('delete.html')


@route_blueprint.route("/health")
def health():
    return "OK"
