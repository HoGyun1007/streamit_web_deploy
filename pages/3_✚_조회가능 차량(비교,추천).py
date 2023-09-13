import streamlit as st
import pandas as pd
import mysql.connector
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
# DBeaverFH 데이터베이스 연결 설정
def create_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="zasx1452",
        database="sys"
    )
    return conn

# mycursor=mydb.cursor()

# Streamlit 애플리케이션 시작
def run_query(query):
    conn = create_conn()
    df = pd.read_sql_query(query,conn)
    return df

query = "select * from car_infos"
df = run_query(query)
st.write(df)

# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title('차량 추천 받기 🌸')
# select_species 변수에 사용자가 선택한 값이 지정됩니다
car_info = st.sidebar.multiselect(
    '추천 받고 싶은 차량을 고르시요, 복수 선택 가능',
    ["TIVOLI", "PALISADE", "PORTER2", "i30", "G4 REXTON", "K3", "K5", "K7", "K9", "QM3", "QM6", "SM3",
                        "SM5", "SM6", "SM7", "XM3", "GRANDEUR", "NIRO", "DAMAS", "RAY", "REXTON SPORT", "MAXCRUZ",
                        "MORNING", "MOHAVE", "VENUE", "VELOSTER", "BONGO3", "SELTOS", "STAREX", "STONIC", "STINGER",
                        "SPORTAGE", "SANTAFE", "SONATA", "SORENTO", "SOUL", "AVANTE", "IONIQ", "ACCENT", "CARNIVAL",
                        "KONA", "KORANDO", "KORANDO TURISMO", "KORANDO C", "TUCSON", "CLIO"]
)
# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
st.info('🚘 차량 비교 하기')
tmp_df = df[df['차종'].isin(car_info)]
# 선택한 종의 맨 처음 5행을 보여줍니다 
st.table(tmp_df.head())


car_infos = ["TIVOLI", "PALISADE", "PORTER2", "i30", "G4 REXTON", "K3", "K5", "K7", "K9", "QM3", "QM6", "SM3",
                        "SM5", "SM6", "SM7", "XM3", "GRANDEUR", "NIRO", "DAMAS", "RAY", "REXTON SPORT", "MAXCRUZ",
                        "MORNING", "MOHAVE", "VENUE", "VELOSTER", "BONGO3", "SELTOS", "STAREX", "STONIC", "STINGER",
                        "SPORTAGE", "SANTAFE", "SONATA", "SORENTO", "SOUL", "AVANTE", "IONIQ", "ACCENT", "CARNIVAL",
                        "KONA", "KORANDO", "KORANDO TURISMO", "KORANDO C", "TUCSON", "CLIO"]

# 라디오에 선택한 내용을 radio_select 변수에 담습니다
radio_select = st.sidebar.radio(
    "비교 대상을 선택하시요.",
    ['가격', '연비', '출력'],
    horizontal=True
)

# 선택한 컬럼에 따라 slider_range 값을 다르게 설정
if radio_select == '가격':
    # 가격에 따른 범위 설정
    slider_range = st.sidebar.slider(
        "choose range of 가격 column",
        0,  # 시작 값
        10000,  # 끝 값
        (1000, 5000)  # 기본값, 앞 뒤로 2개 설정
    )
elif radio_select == '연비':
    # 연비에 따른 범위 설정
    slider_range = st.sidebar.slider(
        "choose range of 연비 column",
        0,  # 시작 값
        50,  # 끝 값
        (10, 40)  # 기본값, 앞 뒤로 2개 설정
    )
elif radio_select == '출력':
    # 출력에 따른 범위 설정
    slider_range = st.sidebar.slider(
        "choose range of 출력 column",
        0,  # 시작 값
        500,  # 끝 값
        (50, 300)  # 기본값, 앞 뒤로 2개 설정
    )

start_button = st.sidebar.button("Filter Apply 📊")

if start_button:
    # 선택한 종들로 데이터프레임을 필터링
    tmp_dfs = df[df['차종'].isin(car_infos)].copy()  # .copy()를 사용하여 복사본 생성

    price_range = tmp_dfs['가격'].str.split('~')
    prices = price_range.apply(lambda x: [int(val.replace(',', '').replace('만원', '').replace('달러', '')) if val else 0 for val in x])
    
    # 가격 범위의 최소값과 최대값을 별도의 열에 저장
    tmp_dfs['가격_최소'] = prices.apply(lambda x: x[0])
    tmp_dfs['가격_최대'] = prices.apply(lambda x: x[1] if len(x) > 1 else x[0])

    tmp_dfs['연비'] = tmp_dfs['연비'].str.extract('(\d+\.?\d*)', expand=False).astype(float)
    tmp_dfs['출력'] = tmp_dfs['출력'].str.extract('(\d+\.?\d*)', expand=False).astype(int)

    # 선택한 컬럼에 따라 필터링 조건 설정
    filter_condition = None
    if radio_select == '가격':
        filter_condition = (tmp_dfs['가격_최소'] >= slider_range[0]) & (tmp_dfs['가격_최대'] <= slider_range[1])
    elif radio_select == '연비':
        filter_condition = (tmp_dfs['연비'] >= slider_range[0]) & (tmp_dfs['연비'] <= slider_range[1])
    elif radio_select == '출력':
        filter_condition = (tmp_dfs['출력'] >= slider_range[0]) & (tmp_dfs['출력'] <= slider_range[1])

    # 원본 데이터에서 필터링된 행을 다시 선택하여 출력
    output_df = df.loc[tmp_dfs[filter_condition].index]
    st.info('🚘 차량 조건 비교 하기')
    st.table(output_df)


image_url = "https://ifh.cc/g/vbmRgR.jpg"
# 이미지를 sidebar에 추가
st.sidebar.image(image_url, width=200)
