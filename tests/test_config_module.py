from app import app

def test_coa_route():
    client = app.test_client()
    response = client.get('/config/coa')
    assert response.status_code == 200
    assert b"Cuenta" in response.data or b"Cuentas" in response.data