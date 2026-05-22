# 남자 모델만 출력 


import sys
import os
import subprocess

# 필요한 패키지 자동 설치
required_packages = ['streamlit', 'numpy', 'joblib', 'scikit-learn']

for package in required_packages:
    try:
        __import__(package if package != 'scikit-learn' else 'sklearn')


# streamlit run으로 자동 재실행
if os.environ.get('STREAMLIT_RUNNING') != '1':
    os.environ['STREAMLIT_RUNNING'] = '1'
    from streamlit.web import cli as stcli
    sys.argv = ["streamlit", "run", os.path.abspath(__file__)]
    sys.exit(stcli.main())
import streamlit as st
import numpy as np
import joblib

st.title("신체 정보를 이용한 몸무게 예측 머신러닝 모델")
st.write("신체 정보를 입력하면 몸무게를 예측합니다.")

model = joblib.load("weight male.pkl")

st.sidebar.header("머신러닝 모델 설계 실습 (다중회귀)")

height = st.slider("허리 둘레(cm)", 140.0, 190.0, 170.0)
waist = st.slider("가슴 둘레 (cm)", 50.0, 120.0, 80.0)
hip = st.slider("엉덩이 둘레 (cm)", 85.0, 120.0, 100.0)

X = np.array([[height, waist, hip]])

if st.button("몸무게 예측하기"):
    prediction = model.predict(X)
    st.success(f"예측 몸무게 : {prediction[0]:.1f} kg")
