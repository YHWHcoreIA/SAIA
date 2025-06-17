from app import app

def test_items_list():
    client = app.test_client()
    response = client.get('/inventory/items')
    assert response.status_code == 200
    assert b"Inventario" in response.data or b"Item" in response.data or b"Producto" in response.data

def test_add_item_form():
    client = app.test_client()
    response = client.get('/inventory/items/add')
    assert response.status_code == 200
    assert b"Agregar" in response.data or b"Nuevo" in response.data