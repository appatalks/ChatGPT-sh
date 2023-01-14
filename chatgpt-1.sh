#!/bin/bash
#

# Variables
API_KEY="API_KEY"

# Set initial prompt
prompt="I would like to ask a question please."

while true; do
    # Make API call
    response=$(curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $API_KEY" -d "{\"prompt\":\"$prompt\", \"temperature\": 0.7, \"max_tokens\": 260, \"top_p\":1, \"frequency_penalty\":0,\"presence_penalty\":0 }" https://api.openai.com/v1/engines/text-davinci-002/completions)

    # Extract text from response
    text=$(echo $response | jq -r '.choices[0].text')
    echo $text
    flite -voice slt --setf duration_stretch=1.15 --setf int_f0_target_mean=160 -t "$text"
    prompt=$text

    # Prompt the user for their next input
    read -p "You: " user_input
    prompt="$user_input"
done
