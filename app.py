from typing import Annotated

from litestar import Litestar, get, put
from litestar.openapi import OpenAPIConfig
from litestar.params import Body

from models.chat import mem, ChatMemory
from models.workout import Workout


@get("/")
async def hello_world() -> str:
    return "Hello, world!"


@get("/prompt")
async def prompt() -> ChatMemory:
    return mem


@put("/submit")
async def submit(data: Annotated[ChatMemory, Body(title='Submit prompt')]) -> Workout:
    return data


app = Litestar([hello_world, prompt, submit], openapi_config=OpenAPIConfig(title="My API", version="1.0.0"))
