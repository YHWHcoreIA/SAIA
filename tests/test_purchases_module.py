from app import app

def test_vendors_list():
    client = app.test_client()
    response = client.get('/purchases/vendors')
    # Comprueba que la página carga y muestra la palabra "Proveedor"
    assert response.status_code == 200
    assert b"Proveedor" in response.data or b"Proveedores" in response.data

def test_add_vendor_form():
    client = app.test_client()
    response = client.get('/purchases/vendors/add')
    assert response.status_code == 200
    assert b"Agregar proveedor" in response.data or b"Nuevo proveedor" in response.data