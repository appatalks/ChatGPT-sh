import openai
import subprocess

# Variables
openai.api_key = "API_KEY"

# Set initial prompt
prompt = "I would like to ask a question please."
while True:
    # Make API call
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=260,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Extract text from response
    text = response.choices[0].text
    # print(text)

    # Speak the text using flite
    subprocess.run(["flite", "-voice", "slt", "--setf", "duration_stretch=1.15", "--setf", "int_f0_target_mean=160", "-pw", "-t", text])

    # Update prompt
    prompt = text

    # Prompt the user for their next input
    user_input = input("You: ")
    prompt = user_input
