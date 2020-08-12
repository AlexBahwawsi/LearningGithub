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

count = 1

for joke in jokes:
    print(str(count) + '. ' + joke + "\n")
    count+=1
