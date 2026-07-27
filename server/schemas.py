from marshmallow import Schema, fields, validates, ValidationError


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(required=True)

    @validates("name")
    def validate_name(self, value, **kwargs):
        if len(value.strip()) < 3:
            raise ValidationError("Exercise name must be at least 3 characters.")


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str(allow_none=True)

    @validates("duration_minutes")
    def validate_duration(self, value, **kwargs):
        if value <= 0:
            raise ValidationError("Duration must be greater than 0.")


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(allow_none=True)
    sets = fields.Int(allow_none=True)
    duration_seconds = fields.Int(allow_none=True)

    @validates("reps")
    def validate_reps(self, value, **kwargs):
        if value is not None and value < 0:
            raise ValidationError("Reps cannot be negative.")

    @validates("sets")
    def validate_sets(self, value, **kwargs):
        if value is not None and value < 0:
            raise ValidationError("Sets cannot be negative.")

    @validates("duration_seconds")
    def validate_duration_seconds(self, value, **kwargs):
        if value is not None and value < 0:
            raise ValidationError("Duration cannot be negative.")