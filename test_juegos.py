import pytest
from app import app
from models import db
import controlador_juegos

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_insertar_y_obtener_juegos(client):
    with app.app_context():
        juego = controlador_juegos.insertar_juego('Zelda', 'Aventura', 1299.0)
        assert juego.id is not None
        assert juego.nombre == 'Zelda'
        juegos = controlador_juegos.obtener_juegos()
        assert len(juegos) == 1

def test_actualizar_y_eliminar_juego(client):
    with app.app_context():
        juego = controlador_juegos.insertar_juego('Hollow Knight', 'Metroidvania', 350.0)
        actualizado = controlador_juegos.actualizar_juego(juego.id, 'Silksong', 'Secuela', 499.0)
        assert actualizado.precio == 499.0
        controlador_juegos.eliminar_juego(juego.id)
        assert controlador_juegos.obtener_juego_por_id(juego.id) is None

def test_rutas_flask(client):
    assert client.get('/').status_code == 200
    assert client.get('/test-error/400').status_code == 400
    assert client.get('/no-existe').status_code == 404
