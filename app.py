from typing import Annotated

from litestar import Litestar, get, put
from litestar.openapi import OpenAPIConfig
from litestar.params import Body

from llm.llm_parser import LLMParser
from models.chat import mem, ChatMemory
from models.workout import Workout
from settings import Settings

settings = Settings()


@get("/prompt")
async def prompt() -> ChatMemory:
    return mem


@put("/submit")
async def submit(data: Annotated[ChatMemory, Body(title='Submit prompt')]) -> Workout:
    workout = LLMParser(memory=data)
    parsed_workout = workout.parse_workout()
    return parsed_workout


app = Litestar([prompt, submit], openapi_config=OpenAPIConfig(title="WorkoutGPT", version="0.0.1"))
