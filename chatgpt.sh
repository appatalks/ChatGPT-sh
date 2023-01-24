#!/bin/bash

# Grab prompt from input
prompt="You are a Linux Terminal. Only respond with $: $1"

# Make API call
response=$(curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $API_KEY" -d "{\"prompt\":\"$prompt\", \"temperature\": 0.7, \"max_tokens\": 260, \"top_p\":1, \"frequency_penalty\":0,\"presence_penalty\":0 }" https://api.openai.com/v1/engines/text-davinci-003/completions)

# Extract text from response
#text=$(echo $response | jq -r '.choices[0].text')
text=$(echo $response | jq -r '.choices[0].text' | xargs echo -n | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

echo "$text" > /tmp/chatgpt.out
cat /tmp/chatgpt.out
