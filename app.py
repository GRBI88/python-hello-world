import requests, json

for user in range(1, 6):
    getRequests = requests.get('https://randomuser.me/api/')
    if getRequests.status_code == 200:
        userData = getRequests.json()
        print(f"User {user}: {userData['results'][0]['name']['first']} {userData['results'][0]['name']['last']}")
        json.dump(userData, open(f"out/user_{user}.json", "w"), indent=4)    
    else:
        print(f"Failed to retrieve user {user}. Status code: {getRequests.status_code}")
        print(f"Error: {getRequests.text}")
        break
else:
    print("All users retrieved successfully.") 


