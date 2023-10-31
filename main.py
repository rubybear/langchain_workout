from langchain.llms.openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from langchain.output_parsers import PydanticOutputParser, RetryWithErrorOutputParser

from rich import print

import chat_memory
from models.workout import Workout

# model_name = "gpt-3.5-turbo-16k-0613"
model_name = "gpt-4"
temperature = 0.0
model = OpenAI(model_name=model_name, temperature=temperature)

memory = ConversationBufferMemory(memory_key="chat_history")
for query, response in chat_memory.MEMORY.items():
    memory.chat_memory.add_ai_message(query)
    memory.chat_memory.add_user_message(response)

parser = PydanticOutputParser(pydantic_object=Workout)

prompt = PromptTemplate(
    template="""You're a helpful assistant and expert in exercise science. 
            You can take user input in the form of workout preferences and generate a workout plan for them.
            You are very careful and pay extra attention to what type of exercise and its requirements.
            You will only generate a workout plan in the provided format instructions, nothing else.\n
            {chat_history}
            {format_instructions}
            {query}""",
    input_variables=["query", "chat_history"],
    partial_variables={"format_instructions": parser.get_format_instructions()}, )

_input = prompt.format_prompt(
    query="""
    Given your conversation with the user, generate a workout plan for them in the specified format and paying 
    special attention to what specific type of exercise is required and its required fields.
    """, chat_history=memory)

output = model(_input.to_string())

try:
    workout = parser.parse(output)
except Exception as e:
    print("retrying...")
    retry_parser = RetryWithErrorOutputParser.from_llm(
        parser=parser, llm=model
    )
    workout = retry_parser.parse_with_prompt(output, _input)
