import requests

def test_api(url):
    client = {
        "lead_source": "organic_search",
        "number_of_courses_viewed": 4,
        "annual_income": 80304.0
    }
    response = requests.post(url, json=client)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.json()

if __name__ == "__main__":
    # Test local
    test_api("http://localhost:8000/predict")
