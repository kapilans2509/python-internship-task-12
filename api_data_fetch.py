# Task 12: Consuming Public APIs Using Python

import requests
import json

API_URL = "https://randomuser.me/api/"

try:
    # 1. Send GET request
    response = requests.get(API_URL)

    # 2. Check response status code
    if response.status_code != 200:
        print("Failed to fetch data. Status code:", response.status_code)
    else:
        print("API request successful!")

        # 3. Parse JSON response
        data = response.json()

        # 4. Extract required fields from nested JSON
        user = data["results"][0]
        name = f"{user['name']['first']} {user['name']['last']}"
        email = user["email"]
        country = user["location"]["country"]

        # 5. Display clean output
        print("\n--- User Details ---")
        print("Name:", name)
        print("Email:", email)
        print("Country:", country)

        # 6. Save full response to local JSON file
        with open("api_response.json", "w") as file:
            json.dump(data, file, indent=4)

        print("\nAPI response saved to api_response.json")

except requests.exceptions.RequestException as e:
    print("API request error occurred:", e)
