from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with, reqparse, abort
from models import db, Juego

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

juego_fields = {
    'id': fields.Integer,
    'nombre': fields.String,
    'descripcion': fields.String,
    'precio': fields.Float
}

juego_parser = reqparse.RequestParser()
juego_parser.add_argument('nombre', type=str, required=True, help='El nombre es obligatorio')
juego_parser.add_argument('descripcion', type=str, required=True, help='La descripcion es obligatoria')
juego_parser.add_argument('precio', type=float, required=True, help='El precio es obligatorio')

juego_update_parser = reqparse.RequestParser()
juego_update_parser.add_argument('nombre', type=str)
juego_update_parser.add_argument('descripcion', type=str)
juego_update_parser.add_argument('precio', type=float)

class JuegoList(Resource):
    @marshal_with(juego_fields)
    def get(self):
        return Juego.query.all(), 200

    @marshal_with(juego_fields)
    def post(self):
        args = juego_parser.parse_args()
        nuevo_juego = Juego(nombre=args['nombre'], descripcion=args['descripcion'], precio=args['precio'])
        db.session.add(nuevo_juego)
        db.session.commit()
        return nuevo_juego, 201

class JuegoResource(Resource):
    @marshal_with(juego_fields)
    def get(self, id):
        juego = Juego.query.get(id)
        if not juego:
            abort(404, message='Videojuego no encontrado')
        return juego, 200

    @marshal_with(juego_fields)
    def put(self, id):
        juego = Juego.query.get(id)
        if not juego:
            abort(404, message='Videojuego no encontrado')
        args = juego_update_parser.parse_args()
        if args['nombre'] is not None:
            juego.nombre = args['nombre']
        if args['descripcion'] is not None:
            juego.descripcion = args['descripcion']
        if args['precio'] is not None:
            juego.precio = args['precio']
        db.session.commit()
        return juego, 200

    def delete(self, id):
        juego = Juego.query.get(id)
        if not juego:
            abort(404, message='Videojuego no encontrado')
        db.session.delete(juego)
        db.session.commit()
        return '', 204

api.add_resource(JuegoList, '/juegos')
api.add_resource(JuegoResource, '/juegos/<int:id>')
