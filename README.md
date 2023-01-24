** Check out the screenshots! I documented how I got here using ChatGPT :D

------------------------------------------------------

## Introduction
OpenAI API Bash Wrapper to generate Linux CLI Commands using the ChatGPT models.
- Initial: prompt="You are a Linux Terminal. Only respond with $: $1"

## Prerequisites
Before using this script, you will need:
- An API key for the OpenAI API. You can get one by signing up for an account on the OpenAI website.
- `curl` command line tool. This is used to make the API call.

## Usage
Add your OpenAI "API_KEY" in the script. Executing the script will then make an API call to the OpenAI API, using the provided prompt to generate text. 

Here are some examples of how to use the script:

./chatgpt.sh "find registrar information of domain" <p>
$ whois domainname.com
  
./chatgpt.sh "AWS CLI to determine FQDN of EC2 instance" <p>
$ aws ec2 describe-instances --instance-ids <instance-id> | grep PublicDnsName | awk {print $2}


## Additional parameters
The script also accept some additional parameters such as temperature, max_tokens, top_p, frequency_penalty, presence_penalty, etc.

./chatgpt.sh "Show disk space" -t 0.7 -m 20 -p 1 -f 0 -r 0 <p>
$ df -h

You can find more information about these parameters in the OpenAI API documentation.
