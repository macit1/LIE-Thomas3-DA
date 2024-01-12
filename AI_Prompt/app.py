import chainlit as cl
from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    
   
    output=generator(message.content, max_length=10, num_return_sequences=2)
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {output[0]['generated_text']}",
    ).send()
@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Welcome to the AI Prompt!",
    ).send()