import streamlit as st
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

st.info('🚘 조회 가능 차량 List')

data = {
    '차종' : ['포터' ,'펠리세이드','티볼리','i30', 'G4렉스턴', 'K3', 'K5', 'K7', 'k9', 'QM3', 'QM6', 'SM3', 'SM5', 'SM6', 'SM7', 'XM3', '그랜저', '니로', '다마스', '레이', '렉스턴스포츠', '맥스크루즈', '모닝', '모하비', '베뉴', '벨로스터', '봉고', '셀토스', '스타렉스', '스토닉', '스팅어', '스포티지', '싼타페', '쏘나타', '쏘렌토', '쏘울', '아반떼', '아이오닉', '엑센트', '카니발', '코나', '코란도', '코란도투리스모', '코란도C', '투싼', '클리오'],
    '연식' : ['2017 ~ 2021', '2019 ~ 2021', '2017 ~ 2021', '2017 ~ 2019', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2019', '2017 ~ 2021', '2017 ~ 2019', '2017 ~ 2020', '2017 ~ 2020', '2017 ~ 2019', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2018', '2017 ~ 2021', '2017 ~ 2021', '2019 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2019', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2019', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2021', '2017 ~ 2019', '2017 ~ 2019', '2017 ~ 2021', '2017 ~ 2021']
    }
df = pd.DataFrame(data)
st.dataframe(df, width=800)  # 표의 너비를 800 픽셀로 설정

st.info('🚘 조회 가능 차량 제원')

df = pd.read_csv('/Users/imhogyun/my_project/streamit_web_deploy/car_info (1).csv')
st.dataframe(df)


image_url = "https://ifh.cc/g/vbmRgR.jpg"
# 이미지를 sidebar에 추가
st.sidebar.image(image_url, width=200)