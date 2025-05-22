from flask import Blueprint, render_template, request, redirect, url_for
from app.models import get_db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    db = get_db()
    os_list = db.execute('SELECT * FROM os ORDER BY id DESC').fetchall()
    return render_template('index.html', os_list=os_list)

@bp.route('/new_client', methods=('GET', 'POST'))
def new_client():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        db = get_db()
        db.execute('INSERT INTO clients (name, phone) VALUES (?, ?)', (name, phone))
        db.commit()
        return redirect(url_for('main.index'))
    return render_template('new_client.html')

@bp.route('/new_os', methods=('GET', 'POST'))
def new_os():
    if request.method == 'POST':
        client_id = request.form['client_id']
        description = request.form['description']
        db = get_db()
        db.execute('INSERT INTO os (client_id, description, status) VALUES (?, ?, ?)', (client_id, description, 'Aberto'))
        db.commit()
        return redirect(url_for('main.index'))
    db = get_db()
    clients = db.execute('SELECT * FROM clients').fetchall()
    return render_template('new_os.html', clients=clients)
