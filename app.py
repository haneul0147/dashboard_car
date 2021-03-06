import streamlit as st
import numpy as np
import os
import pickle

from eda_app import run_eda_app
from ml_app import run_ml_app

def main():

    # 사이드바 메뉴
    menu = ['home','Data','나의 차량 찾기']
    choice=st.sidebar.selectbox('메뉴',menu)

    if choice == 'home':
        st.title('would you like car??')
        if st.button('Click here') :
            st.video('https://youtu.be/T8YOJIoOifc',format='video/mp4')
    
    elif choice == 'Data':
        run_eda_app()
    elif choice == '나의 차량 찾기':
        run_ml_app()

if __name__ == '__main__':
    main()