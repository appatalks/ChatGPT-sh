import openai
import subprocess

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
        n=2,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Extract text from response
    text = response.choices[0].text

    # Speak the text using flite
    subprocess.run(["flite", "-voice", "slt", "--setf", "duration_stretch=1.15", "--setf", "int_f0_target_mean=160", "-pw", "-t", text])
    
    # Concatenate the prompt with the previous question and response
    # Still a little bit finiky compared to the website... Still needs work in response handling.
    user_input = input("You: ")
    prompt = user_input + " " + text
