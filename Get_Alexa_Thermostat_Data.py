import time
import requests
import threading

# Replace with your actual API endpoint and authentication details
API_ENDPOINT = "https://api.amazon.com/thermostat"
AUTH_TOKEN = "your_auth_token"

def get_thermostat_data():
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(API_ENDPOINT, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data:", response.status_code)
        return None

def main():
    last_setpoint = None

    while True:
        data = get_thermostat_data()
        if data:
            current_temp = data.get('current_temperature')
            current_setpoint = data.get('setpoint')

            print(f"Current Temperature: {current_temp}°F")
            
            if current_setpoint != last_setpoint:
                print(f"Setpoint changed to: {current_setpoint}°F")
                last_setpoint = current_setpoint
            
            def check_setpoint_change():
                global last_setpoint
                data = get_thermostat_data()
                if data:
                    current_setpoint = data.get('setpoint')
                    if current_setpoint != last_setpoint:
                        print(f"Setpoint changed to: {current_setpoint}°F")
                        last_setpoint = current_setpoint
                # Schedule the next check
                threading.Timer(10, check_setpoint_change).start()

            # Start the first check
            check_setpoint_change()
        else:
            time.sleep(30)  # Wait before retrying if data retrieval failed

if __name__ == "__main__":
    main()