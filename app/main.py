from functools import lru_cache
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Body, Depends

from llm.llm_parser import LLMParser
from models.chat import mem, ChatMemory
from models.workout import Workout
from settings import Settings

app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()


@app.get("/prompt")
async def prompt() -> ChatMemory:
    return mem


@app.put("/submit")
async def submit(data: ChatMemory, settings: Annotated[Settings, Depends(get_settings)]) -> Workout:
    workout = LLMParser(memory=data, api_key=settings.openai_api_key)
    parsed_workout = workout.parse_workout()
    return parsed_workout