# main.py

""" This script pings the live backend to ensure it is up and running.
It prints the current time, the URL being pinged, and the response status code.
If the backend is not reachable, it will print an error message."""

import requests
import datetime

def ping_backend():
    url = "https://smart-grievance-management-backend.onrender.com/"  # Your live backend URL
    
    try:
        print(f"{datetime.datetime.now()}: Pinging {url}")
        response = requests.get(url, timeout=30)
        print(f"Response: {response.status_code}")
        
        if response.status_code == 200:
            print("Backend is alive")
        else:
            print(f"⚠️ Unexpected status code: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ping_backend()
