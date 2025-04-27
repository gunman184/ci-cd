import requests
endpoint = 'https://ij6onx27l6.execute-api.us-east-1.amazonaws.com/prod/api_processing'

def test_call_endpoint():
    response = requests.get(endpoint)
    assert response.status_code == 200

def test_can_increase():
    response = requests.post(endpoint)
    assert response.status_code == 200
    data  =response.json()
    print(data)