#!/bin/bash

# Grab prompt from input
prompt="$1"

# Make API call
response=$(curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d "{\"prompt\":\"$prompt\", \"temperature\": 0.7, \"max_tokens\": 260, \"top_p\":1, \"frequency_penalty\":0,\"presence_penalty\":0 }" https://api.openai.com/v1/engines/text-davinci-002/completions)

# Extract text from response
text=$(echo $response | jq -r '.choices[0].text')

# Speak response
# espeak -ven-us+f4 -s170 "$text"
# flite -voice slt --setf duration_stretch=1.15 --setf int_f0_target_mean=160 -pw -t "$text"
echo "$text"
