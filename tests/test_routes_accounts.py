import pytest
from models import db, Account

@pytest.fixture
def preloaded_db(app):
    with app.app_context():
        # Crea datos de ejemplo antes de cada prueba
        account = Account(code="1001", name="Caja General", type="Activo")
        db.session.add(account)
        db.session.commit()
        yield
        # Limpia la base de datos después de cada prueba
        db.session.remove()
        db.drop_all()
        db.create_all()

def test_coa_route_lists_accounts(client, preloaded_db):
    # Prueba que /config/coa muestra la cuenta creada
    response = client.get('/config/coa')
    assert response.status_code == 200
    assert b"Caja General" in response.data

def test_add_account_route_post(client, app):
    # Prueba que se puede agregar una cuenta vía POST
    response = client.post(
        '/config/coa/add',
        data={"code": "2001", "name": "Banco", "type": "Activo"},
        follow_redirects=True
    )
    assert response.status_code == 200
    # Verifica que la nueva cuenta se muestra en la lista
    assert b"Banco" in response.data
    # Verifica que la cuenta fue creada en la base de datos
    with app.app_context():
        acc = Account.query.filter_by(code="2001").first()
        assert acc is not None
        assert acc.name == "Banco"