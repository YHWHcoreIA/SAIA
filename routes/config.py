from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Account

bp = Blueprint('config', __name__)

@bp.route('/coa')
def coa():
    accounts = Account.query.all()
    return render_template('config/coa.html', accounts=accounts)

@bp.route('/coa/add', methods=('GET', 'POST'))
def add_account():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        acc_type = request.form['type']
        if not code or not name:
            flash('Código y Nombre requeridos.', 'danger')
        elif Account.query.filter_by(code=code).first():
            flash(f'La cuenta con código {code} ya existe.', 'danger')
        else:
            new_account = Account(code=code, name=name, type=acc_type)
            db.session.add(new_account)
            db.session.commit()
            flash('Cuenta añadida exitosamente.', 'success')
            return redirect(url_for('config.coa'))
    account_types = ['Activo', 'Pasivo', 'Capital', 'Ingresos', 'Gastos']
    return render_template('config/add_account.html', account_types=account_types)