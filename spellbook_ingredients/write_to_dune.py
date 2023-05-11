import csv
import json
import requests

def write_to_dune(api_key, csv_path):

    url = 'https://api.dune.com/api/v1/table/upload/csv'
    with open(csv_path) as open_file:
        data = open_file.read()
        headers = {'X-Dune-Api-Key': api_key}
        payload = {
            "table_name": "resource_names_spellbook",
            "description": "Table with resource names used on Spellbook",
            "data": str(data)
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if(response.status_code == 200 and response.json()['success']):
            print('Success writing CSV to Dune.com!', flush=True)
        else:
            print('Error writing CSV to Dune.com!')
            print(response.content)
