#!/bin/bash
prompt="$1"

response=$(curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d "{\"prompt\":\"$prompt\", \"stop\":\"\", \"temperature\": 0.7, \"max_tokens\": 20, \"top_p\":1, \"frequency_penalty\":0,\"presence_penalty\":0 }" https://api.openai.com/v1/engines/text-davinci-002/completions)

echo $(echo $response | jq -r '.choices[0].text')
