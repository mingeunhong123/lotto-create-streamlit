
#%%
import streamlit as st
import random

# Streamlit 애플리케이션 제목
st.title("로또 번호 생성기")

# 설명 텍스트
st.write("\U0001F3B2 버튼을 눌러 로또 번호를 생성하세요! \U0001F680")

# 로또 번호 생성 함수
def generate_lotto_numbers():
    lotto_numbers = []
    for i in range(5):
        lotto = sorted(random.sample(range(1, 46), 6))
        lotto_numbers.append(lotto)
    return lotto_numbers

# 버튼 생성 및 번호 출력
if st.button("로또 번호 생성하기"):
    lotto_results = generate_lotto_numbers()
    st.write("### 생성된 로또 번호:")
    for idx, lotto in enumerate(lotto_results, 1):
        lotto = ", ".join(map(str, lotto))
        
        st.subheader(f"행운의 번호 {idx} : :green[{lotto}]")

st.write('')
st.markdown("### 행운을 빕니다! \U0001F3C6")

# %%
