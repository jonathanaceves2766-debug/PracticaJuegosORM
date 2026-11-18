from models import db, Juego

def obtener_juegos():
    return Juego.query.all()

def obtener_juego_por_id(id):
    return Juego.query.get(id)

def insertar_juego(nombre, descripcion, precio):
    nuevo = Juego(nombre=nombre, descripcion=descripcion, precio=precio)
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def actualizar_juego(id, nombre, descripcion, precio):
    juego = Juego.query.get(id)
    if juego:
        juego.nombre = nombre
        juego.descripcion = descripcion
        juego.precio = precio
        db.session.commit()
    return juego

def eliminar_juego(id):
    juego = Juego.query.get(id)
    if juego:
        db.session.delete(juego)
        db.session.commit()
    return juego
