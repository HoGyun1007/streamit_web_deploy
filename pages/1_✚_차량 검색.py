import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
from efficientnet_pytorch import EfficientNet
import pandas as pd

# 배너 이미지 추가를 위한 HTML 스타일 코드
banner_style = """
    <style>
        .banner-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 300px;  # 원하는 높이로 조정하세요.
        }
        .banner-img {
            max-width: 100%;
        }
    </style>
"""

# 배너 이미지 URL
banner_image_url = 'https://ifh.cc/g/vbmRgR.jpg'
# 배너 이미지 출력
st.markdown('<p style="text-align:center;"><img src="%s" alt="Banner Image" width="800"></p>' % banner_image_url, unsafe_allow_html=True)


# 미리 학습된 가중치 로드 (CPU로 매핑)
weights = torch.load('/Users/imhogyun/my_project/streamit_web_deploy/president_model.pt', map_location=torch.device('cpu'))

# 모델 초기화 및 가중치 적용 (예: 'efficientnet-b0')
model = EfficientNet.from_name('efficientnet-b0')
model.load_state_dict(weights)
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

        class_names = ['XC60', '티구안', '티볼리', '팰리세이드', '포터2', '프리우스'] # 실제 사용할 때는 여러분의 클래스 이름으로 변경

        predicted_class_name = class_names[predicted_idx.item()]

        st.write(f'차종: {predicted_class_name}')

data = pd.read_csv('/Users/imhogyun/my_project/streamit_web_deploy/car_info (1).csv')

# 예측된 차종에 해당하는 데이터 필터링
predicted_data = data[data['차종'] == predicted_class_name]

# 필요한 정보 출력
# st.write(f'자동차 제원: {predicted_data}')
st.dataframe(predicted_data)

image_url = "https://ifh.cc/g/vbmRgR.jpg"
# 이미지를 sidebar에 추가
st.sidebar.image(image_url, width=200)
