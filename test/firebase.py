import firebase_admin
from firebase_admin import credentials, storage
import pandas as pd
import requests
import os

# 파이어베이스 서비스 계정 키 다운로드한 JSON 파일 경로
cred = credentials.Certificate(r"C:\dev\hope_project\hopeimage-74788-firebase-adminsdk-qxan6-dc45fd4c42.json")

# 파이어베이스 앱 초기화
firebase_admin.initialize_app(cred, {
    'storageBucket': 'hopeimage-74788.appspot.com' # gs:// 이후 경로부터 작성
})

# 업로드할 로컬 디렉토리 경로
local_directory = r"C:\dev\hope_project\medical_dataset\image"

# Firebase 스토리지의 업로드 경로 (저장될 디렉토리 경로)
firebase_storage_path = "image"

# 이미지 다운로드
def download_image():
    # 이미지 링크가 있는 xlsx 파일 경로
    df = pd.read_excel(r"C:\dev\hope_project\medical_dataset\medicine_image.xlsx")

    for idx, row in df.iterrows():
        code = row['ITEM_SEQ']
        img = row['ITEM_IMAGE']
        if img != '':
            response = requests.get(img)
            with open(f"C:\dev\hope_project\medical_dataset\image\img_{code}.jpg", 'wb') as f:
                f.write(response.content)
        if idx % 500 == 0:
            print(f"{idx} rows processed")

download_image()