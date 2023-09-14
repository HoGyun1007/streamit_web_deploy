import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
from efficientnet_pytorch import EfficientNet
import pandas as pd
import os
import mysql.connector
# from torchvision import models
from torchvision.models import efficientnet_b0
import torch.nn as nn
# 모델 파일의 경로를 설정 (로컬 PC에서 모델 파일을 저장한 경로)
os.system("git clone https://github.com/lukemelas/EfficientNet-PyTorch")
model = EfficientNet.from_pretrained("efficientnet-b0")


model_file_path = 'president_model_20230914_128batch_10epoch(1280, 46).pt'  # 여기에 모델 파일의 경로를 지정하세요

# 모델 초기화 및 가중치 적용 (예: 'efficientnet-b0')
# 저장된 state_dict와 동일한 아키텍처를 가진 사전 훈련된 모델을 로드합니다.
# model = efficientnet_b0(pretrained=True)

# 출력 클래스 수를 원하는 값 (예: 46)으로 맞추기 위해 최종 완전 연결 레이어를 수정합니다.
num_classes = 46
model._fc =nn.Linear(in_features=1280, out_features=num_classes)

# 저장된 state_dict를 로드합니다.
model.load_state_dict(torch.load(model_file_path, map_location=torch.device('cpu')))
model.eval()

st.title('Custom EfficientNet Image Classifier')

predicted_class_name = ""  # 변수 초기화

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")  # convert("RGB") 추가
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    if st.button('Predict'):
        # 이미지 전처리 및 예측 진행

        # 이미지를 텐서로 변환하기 위한 전처리 파이프라인 설정
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

        input_tensor = preprocess(image)  # 이미지 -> 텐서 변환
        input_batch = input_tensor.unsqueeze(0)  # 배치 차원 추가

        with torch.no_grad():
            prediction = model(input_batch)

        _, predicted_idx = torch.max(prediction, 1)

        class_names = ["TIVOLI", "PALISADE", "PORTER2", "I30", "G4 REXTON", "K3", "K5", "K7", "K9", "QM3", "QM6", "SM3",
                        "SM5", "SM6", "SM7", "XM3", "GRANDEUR", "NIRO", "DAMAS", "RAY", "REXTON SPORT", "MAXCRUZ",
                        "MORNING", "MOHAVE", "VENUE", "VELOSTER", "BONGO3", "SELTOS", "STAREX", "STONIC", "STINGER",
                        "SPORTAGE", "SANTAFE", "SONATA", "SORENTO", "SOUL", "AVANTE", "IONIQ", "ACCENT", "CARNIVAL",
                        "KONA", "KORANDO", "KORANDO TURISMO", "KORANDO C", "TUCSON", "CLIO"]
        # 실제 사용할 때는 여러분의 클래스 이름으로 변경

        predicted_class_name = class_names[predicted_idx.item()]

        st.write(f'차종: {predicted_class_name}')

# DBeaverFH 데이터베이스 연결 설정
def create_conn():
    conn = mysql.connector.connect(
        host="localhost",
        port='3306',
        user="root",
        password="zasx1452",
        database="sys"
    )
    return conn

def run_query(query):
    conn = create_conn()
    df = pd.read_sql_query(query,conn)
    return df
query = f"select * from car_infos where 차종='{predicted_class_name}'"
# 예측된 차종에 해당하는 데이터 필터링
# predicted_data = df[df['차종'] == predicted_class_name]
# query = "select * from car_infos where 차종='predicted_class_name'"
df1 = run_query(query)

# 필요한 정보 출력ß
# st.write(f'자동차 제원: {predicted_data}')
# st.dataframe(predicted_data)
st.dataframe(df1)
image_url = "https://ifh.cc/g/vbmRgR.jpg"
# 이미지를 sidebar에 추가
st.sidebar.image(image_url, width=200)
