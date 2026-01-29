import json


def process_server_data(json_string):


    try:
        data=json.loads(json_string)
        for server in data["servers"]:
            print(f"server {server ['name']} is {server['status']}")
    except json.JSONDecodeError:
        print("Error: invalid JSON data")
    



mock_api = '{"servers": [{"name": "web-01", "status": "up"}, {"name": "db-01", "status": "down"}]}'

process_server_data(mock_api)