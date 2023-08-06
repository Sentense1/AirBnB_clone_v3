#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    try:
        r = requests.get("http://0.0.0.0:5050/api/v1/users")
        r.raise_for_status()  # Raise an exception for 4xx and 5xx status codes.
        r_j = r.json()
        for user_j in r_j:
            if user_j.get("password") is None:
                print("OK")
            else:
                print("Password is still present in User: {} - {}".format(user_j.get("email"), user_j.get("password")))
    except requests.exceptions.RequestException as e:
        print("Error making the request:", e)
    except json.JSONDecodeError as e:
        print("Error decoding JSON response:", e)
