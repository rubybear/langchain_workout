from typing import List, Optional, Literal

from pydantic import BaseModel, Field


class DumbbellBarbellExercises(BaseModel):
    """A dumbbell or barbell exercise with sets, reps, and weight"""
    name: str = Field(description="The name of the exercise")
    explanation: str = Field(description="The explanation or description of the exercise")
    sets: int = Field(description="The number of sets. Required for barbell exercises.")
    reps: int = Field(description="The number of reps. Required for barbell exercises.")
    weight: int = Field(description="The weight in pounds. Required for barbell exercises.")


class BodyWeightExercise(BaseModel):
    """A body weight exercise with optional sets, reps, and time and no weight"""
    name: str = Field(description="The name of the exercise")
    explanation: str = Field(description="The explanation or description of the exercise")
    sets: Optional[int] = Field(description="The number of sets")
    reps: Optional[int] = Field(description="The number of reps")
    time: Optional[int] = Field(description="The time in seconds. Example: 30 seconds = 30")


class KettlebellExercise(BaseModel):
    """A kettlebell exercise with sets, reps, and weight"""
    name: str = Field(description="The name of the exercise")
    explanation: str = Field(description="The explanation or description of the exercise")
    sets: int = Field(description="The number of sets")
    reps: int = Field(description="The number of reps")
    weight: Literal[16, 32, 48, 64] = Field(description="The weight in kilos. Required for kettlebell exercises.")




class Day(BaseModel):
    """A day of the week"""
    day: str = Field(description="The day of the week")
    body_weight_exercises: Optional[List[BodyWeightExercise]] = Field(
        description="The body weight exercises for the day")
    dumbbell_exercises: Optional[List[DumbbellBarbellExercises]] = Field(description="The dumbbell exercises for the day")
    kettlebell_exercises: Optional[List[KettlebellExercise]] = Field(description="The kettlebell exercises for the day")


class Workout(BaseModel):
    """A workout plan containing a list of exercises for each day of the week"""
    days: List[Day] = Field(description="The days of the week")
