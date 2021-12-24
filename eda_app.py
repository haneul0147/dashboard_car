import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.proto.RootContainer_pb2 import SIDEBAR


def run_eda_app() : 
    st.subheader('EDA 화면입니다.')

    df=pd.read_csv('data/car.txt',encoding='ISO-8859-1')
    if st.checkbox('데이터 보기'):
        box_menu=['전체 데이터보기','데이터 통계보기']
        selected_radio =st.selectbox('선택하세요',box_menu)

        if selected_radio == '전체 데이터보기':
            st.dataframe(df)
        elif selected_radio=='데이터 통계보기':
            st.dataframe(df.describe())


    # 컬럼을 선택하면, 해당 컬럼들만 데이터 프레임 표시하는 화면 
    if st.sidebar.checkbox('컬럼 하나씩 비교해보기'):
        selected_columns=st.multiselect('컬럼을 선택하세요',df.columns)
        if len(selected_columns) !=0 :
            st.dataframe(df[selected_columns])    
        else :
            st.write('선택된 컬럼이 없습니다.')

    # 상관관계 분석을 위한, 상관계수 보여주는 화면 개발
    if st.sidebar.checkbox('데이터별 상관계수보기'):
        st.subheader('상관계수')
        # st.dataframe(df.corr())
        df_corr = df.iloc[:,3 :]
        selected_corr=st.multiselect('상관계수 컬럼 선택',df_corr.columns)
        ('유저가 1개라도 컬럼을 선택했을 경우')
        if len(selected_corr)>0:
            st.dataframe(df_corr[selected_corr].corr())

        # 상관계수를 수치로도 구하고, 차트로도 표시해라 .

        
            fig1 = sns.pairplot(data=df_corr[selected_corr])
            st.pyplot(fig1)
    # 유저가 컬럼을 선택하지 않은 경우 
        else:
            st.write('선택한 컬럼이 없습니다.')

        # 컬럼을 선택하면,
        #  해당컬럼의 min 과 max 에 해당괴는 사람이 이 누구인지
        # 그 사람의 데이터를 화면에 보여주는 기능개발 

        # 문자열 데이테가 아닌, 컬럼들만 사용하는 코드!!!!!!!
    if st.sidebar.checkbox('최대 최소 값 보기'):
        st.subheader('최대 최소 값')
        print(df.columns)
        print(df.dtypes != object)

        number_colums=df.columns[df.dtypes != object]
        selected_minmax_columns=st.selectbox('컬럼 선택',number_colums)
        
        
    
        # 선택한 컬럼의 최소값에 해당되는 사람의 데이터 출력
        #df[selected_minmax_columns] == df[selected_minmax_columns].min()
        min_data=df.loc[df[selected_minmax_columns] == df[selected_minmax_columns].min(),]
        st.dataframe(min_data)
        # 선택한 컬럼의 최대값에 해당되는 사람의 데이터 출력
        # df[selected_minmax_columns] == df[selected_minmax_columns].max()
        max_data=df.loc[df[selected_minmax_columns] == df[selected_minmax_columns].max(),]
        st.dataframe(max_data)
        
    
    if st.sidebar.checkbox('search peoples'):
        st.subheader('사람 검색')
        # 고객의 이름을 검색할 수 있는 기능 개발 
        # 1. 유저한테 검색어 입력을 받습니다.
        word=st.text_input('검색어를 입력하세요')
        print(word)
        # 검색을 위해서 소문자로 만든다.
        word=word.lower()
        # 2. 검색어를 데이터 프레임의 Customer Name 컬럼에서 검색해서가져오기
        df_search=df.loc[ df['Customer Name'].str.lower().str.contains(word),]
        # 3. 화면에 결과를 보여준다
    
        st.dataframe(df_search)