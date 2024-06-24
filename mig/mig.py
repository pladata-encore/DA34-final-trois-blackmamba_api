import pandas as pd
import requests

# CSV 파일 읽기
df = pd.read_csv('car.csv')

# FastAPI 서버 URL
API_URL = "http://127.0.0.1:8000/cars/"

# 각 레코드를 FastAPI 서버에 추가하는 함수
def add_car_to_api(car_data):
    response = requests.post(API_URL, json=car_data)
    if response.status_code == 200:
        print(f"Successfully added car: {car_data['carName']}")
    else:
        print(f"Failed to add car: {car_data['carName']}, Status Code: {response.status_code}, Error: {response.text}")

# 각 레코드를 API에 추가
for _, row in df.iterrows():
    car_data = {
        "cid": row['cid'],
        "carCompany": row['carCompany'],
        "carName": row['carName'],
        "carYear": row['carYear'],
        "carCode": row['carCode'],
    }
    add_car_to_api(car_data)