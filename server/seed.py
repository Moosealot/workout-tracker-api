#!/usr/bin/env python3

from datetime import date

from app import app
from models import db, Workout, Exercise, WorkoutExercise


with app.app_context():

    print("Deleting old data...")

    db.drop_all()
    db.create_all()

    squat = Exercise(
        name="Squat",
        category="Legs",
        equipment_needed=True
    )

    pushup = Exercise(
        name="Push Up",
        category="Chest",
        equipment_needed=False
    )

    plank = Exercise(
        name="Plank",
        category="Core",
        equipment_needed=False
    )

    db.session.add_all([
        squat,
        pushup,
        plank
    ])

    db.session.commit()

    workout = Workout(
        date=date.today(),
        duration_minutes=60,
        notes="Full Body Workout"
    )

    db.session.add(workout)
    db.session.commit()

    we1 = WorkoutExercise(
        workout_id=workout.id,
        exercise_id=squat.id,
        reps=10,
        sets=4,
        duration_seconds=None
    )

    we2 = WorkoutExercise(
        workout_id=workout.id,
        exercise_id=pushup.id,
        reps=15,
        sets=3,
        duration_seconds=None
    )

    db.session.add_all([we1, we2])
    db.session.commit()

    print("Database seeded successfully!")