import requests

# array for jokes to be stored in
jokes = []

# call icanhazdadjoke API request 5 times
for i in range(5):
    response = requests.get('https://icanhazdadjoke.com/',
        headers = {'Accept': 'application/json'}
    )
    #take response, turn into json and then take joke element
    oneJoke = response.json()
    jokes.append(oneJoke['joke'])

print(*jokes, sep = "\n") #print each joke on a separate line
