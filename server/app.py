import os

from flask import Flask, request, jsonify
from flask_migrate import Migrate

from schemas import (
    WorkoutSchema,
    ExerciseSchema,
    WorkoutExerciseSchema
)

from models import db, Workout, Exercise, WorkoutExercise

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)


@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts))


@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.get_json()

    validated = workout_schema.load(data)

    workout = Workout(**validated)

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout), 201


if __name__ == "__main__":
    app.run(port=5555, debug=True)