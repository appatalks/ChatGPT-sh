import openai
import subprocess
from loguru import logger

# Remove the default logger
logger.remove()

# Set up loguru logger 
logger.add("/tmp/ai.log", format="{message}")

# Variables
openai.api_key = "API_KEY"

# Prompt the user for their initial input
initial_prompt = input("You: ") 
prompt = initial_prompt

# Generate a response
while True:
    # Make API call
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=160,
        n=1,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Extract text from response
    text = response.choices[0].text

    # Remove leading and trailing whitespace from the text
    text = text.strip()

    # Print the text to the console
    print("AI: " + text)

    # Speak the text using flite
    subprocess.run(["flite", "-voice", "slt", "--setf", "duration_stretch=1.15", "--setf", "int_f0_target_mean=160", "-pw", "-t", text], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Log the conversation
    logger.info("User: {}", initial_prompt)
    logger.info("AI: {}", text)
    # Concatenate the prompt with the previous question and response
    user_input = input("You: ")
    prompt = user_input + " " + text
    initial_prompt=user_input
