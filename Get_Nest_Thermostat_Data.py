import requests

# Replace with your own access token
access_token = "YOUR_ACCESS_TOKEN"

# Replace with your thermostat ID
thermostat_id = "YOUR_THERMOSTAT_ID"

# API endpoint to get thermostat data
url = f"https://smartdevicemanagement.googleapis.com/v1/enterprises/{thermostat_id}/devices/{thermostat_id}:executeCommand"

# Headers with authorization
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# Payload to get thermostat data
payload = {
    "command": "sdm.devices.commands.ThermostatMode.GetMode",
    "params": {}
}

# Send the API request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    thermostat_data = response.json()
    temperature = thermostat_data["data"]["thermostatTemperatureAmbientCelsius"]
    setpoint = thermostat_data["data"]["thermostatTemperatureSetpointCelsius"]
    settings = thermostat_data["data"]["thermostatMode"]
    print(f"Temperature: {temperature}°C")
    print(f"Setpoint: {setpoint}°C")
    print(f"Settings: {settings}")
else:
    print("Failed to retrieve thermostat data.")