from models import db, Account

def test_create_account(client):
    # Crea una cuenta contable y verifica que se guarda
    new_account = Account(code='1010', name='Caja', type='Activo')
    db.session.add(new_account)
    db.session.commit()
    found = Account.query.filter_by(code='1010').first()
    assert found is not None
    assert found.name == 'Caja'