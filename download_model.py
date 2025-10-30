import requests

def download_model():
    url = "https://github.com/DataTalksClub/machine-learning-zoomcamp/raw/refs/heads/master/cohorts/2025/05-deployment/pipeline_v1.bin"
    print("Downloading model...")
    response = requests.get(url)
    with open('pipeline_v1.bin', 'wb') as f:
        f.write(response.content)
    print("Model downloaded successfully!")

if __name__ == "__main__":
    download_model()
