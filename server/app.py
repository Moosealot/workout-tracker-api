from flask import Flask
from flask_migrate import Migrate

from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)

duration_minutes = db.Column(
    db.Integer,
    nullable=False
)

name = db.Column(
    db.String(100),
    nullable=False,
    unique=True
)

@validates("duration_minutes")
def validate_duration(self, key, value):

    if value <= 0:
        raise ValueError("Duration must be positive.")

    return value

@validates("name")
def validate_name(self, key, value):

    if len(value) < 3:
        raise ValueError("Exercise name too short.")

    return value

@validates("reps")
def validate_reps(self, key, value):

    if value is not None and value < 0:
        raise ValueError("Reps cannot be negative.")

    return value

if __name__ == "__main__":
    app.run(port=5555, debug=True)