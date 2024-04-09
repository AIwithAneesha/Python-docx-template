import requests

url = 'http://localhost:7005/api/create_final_agreement_and_export_as_docx'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
data = {
    "keycloak_user_id": "0728e80e-7a0a-4827-9c27-4933aeb842a0",
    "agreement_type": ["scripter1"],
    "session_id": "9fa2e371-cb6a-46fd-bb52-6952ce797d20"
}

response = requests.post(url, headers=headers, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the file to disk
    with open("output.docx", "wb") as f:
        f.write(response.content)
    print("File downloaded successfully")
else:
    print(f"Error: {response.status_code} - {response.reason}")

