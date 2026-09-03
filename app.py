import streamlit as st
import pandas as pd
import time 

# if 'counter' not in st.session_state :
#     st.session_state['counter'] = 0

# if st.button('Increment') :
#     st.session_state['counter'] += 1

# if st.button('초기화') :
#     st.session_state['counter'] = 0

# counter = st.session_state['counter']
# st.write(f'카운터 : {counter}')
@st.cache_data
def load_data() :
    df = pd.read_csv('2019-Oct-small.csv')
    return df

start_time = time.time()

data = load_data()
st.dataframe(data.head())

elapsed = time.time() - start_time



st.write(f'소요시간: {elapsed}')
st.write('캐시 데이터 적용')
