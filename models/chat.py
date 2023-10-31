from typing import Dict

from pydantic import BaseModel

from chat_memory import MEMORY


class ChatMemory(BaseModel):
    messages: dict[str, str]


mem = ChatMemory(messages=MEMORY)
