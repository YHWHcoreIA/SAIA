import pytest
from models import db, Vendor

@pytest.fixture
def preloaded_vendor(app):
    with app.app_context():
        vendor = Vendor(name="Proveedor Demo", tax_id="XOXO1234", contact_info="email@demo.com")
        db.session.add(vendor)
        db.session.commit()
        yield
        db.session.remove()
        db.drop_all()
        db.create_all()

def test_vendor_list(client, preloaded_vendor):
    response = client.get('/purchases/vendors')
    assert response.status_code == 200
    assert b"Proveedor Demo" in response.data

def test_add_vendor(client, app):
    response = client.post(
        '/purchases/vendors/add',
        data={"name": "Nuevo Proveedor", "tax_id": "RFC999", "contact_info": "nuevo@proveedor.com"},
        follow_redirects=True
    )
    assert response.status_code == 200
    # Verifica que se muestra el nuevo proveedor
    assert b"Nuevo Proveedor" in response.data
    with app.app_context():
        vendor = Vendor.query.filter_by(name="Nuevo Proveedor").first()
        assert vendor is not None
        assert vendor.tax_id == "RFC999"