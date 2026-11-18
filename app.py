import logging
from flask import Flask, render_template, jsonify, request, abort
from werkzeug.exceptions import HTTPException
from models import db
import controlador_juegos

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tienda_juegos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

file_handler = logging.FileHandler("errors.log", encoding="utf-8")
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

@app.route("/")
def juegos():
    lista_juegos = controlador_juegos.obtener_juegos()
    return render_template("juegos.html", juegos=lista_juegos)

@app.errorhandler(400)
def bad_request_error(error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "Bad Request"}), 400
    return render_template("400.html"), 400

@app.errorhandler(404)
def not_found_error(error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "Not Found"}), 404
    return render_template("404.html"), 404

@app.errorhandler(405)
def method_not_allowed_error(error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "Method Not Allowed"}), 405
    return render_template("405.html"), 405

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error(f"Excepción 500 provocada en {request.path}: {error}")
    if request.path.startswith("/api/"):
        return jsonify({"error": "Internal Server Error"}), 500
    return render_template("500.html"), 500

@app.route("/test-error/400")
def test_400():
    abort(400)

@app.route("/test-error/405", methods=["POST"])
def test_405():
    return "OK"

@app.route("/test-error/500")
def test_500():
    abort(500)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
