workout_exercises = db.relationship(
    "WorkoutExercise",
    back_populates="workout",
    cascade="all, delete-orphan"
)

exercises = db.relationship(
    "Exercise",
    secondary="workout_exercises",
    viewonly=True
)

workout_exercises = db.relationship(
    "WorkoutExercise",
    back_populates="exercise",
    cascade="all, delete-orphan"
)

workouts = db.relationship(
    "Workout",
    secondary="workout_exercises",
    viewonly=True
)

workout = db.relationship(
    "Workout",
    back_populates="workout_exercises"
)

exercise = db.relationship(
    "Exercise",
    back_populates="workout_exercises"
)

