from flask import Flask, jsonify
from routes.movies_bp import movies_bp
from config import Config
from extensions import db
from sqlalchemy.sql import text
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db.init_app(app)


def test_connection():
    try:
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
    except Exception as e:
        print("Error connecting to the database:", e)


with app.app_context():
    test_connection()


@app.get("/")
def hello():
    return jsonify(message="API Running")


app.register_blueprint(movies_bp, url_prefix="/api/movies")


@app.errorhandler(404)
def not_found(e):
    return {"error": "Resource not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)