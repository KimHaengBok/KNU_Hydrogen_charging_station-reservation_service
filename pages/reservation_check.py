import streamlit as st
from api import nav_page, send_res_val
from streamlit.components.v1 import html
import json 

# 슬라이드바 제거
hide_navi = """
<style>
    /* Hide the sidebar navigation */
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
"""

st.markdown(hide_navi, unsafe_allow_html=True)

# 세션 저장 값 호출
# 1. 충전소 명
# 2. 차량번호 (뒤 4자리)
# 3. 예약자 성함
# 4. 전화번호
# 5. 예약시간

chr_name = st.session_state.user_input1
car_num = st.session_state.user_input2
name = st.session_state.user_input3
ph_num = st.session_state.user_input4
res_date = st.session_state.user_input5
res_time = st.session_state.user_input6

# 예약자 정보 출력
st.header("예약 정보 확인")
st.write("충전소 : " + chr_name)
st.write("차량번호 : " + car_num)
st.write("성함 : " + name)
st.write("전화번호 : " + ph_num)
st.write("예약 시간 : " + res_date + res_time)

res_info = {
    "chr_name" : chr_name,
    "car_num" : car_num,
    "name" : name,
    "ph_num" : ph_num,
    "res_time" : f"{res_date} {res_time}"
}

col1, col2, col3 = st.columns([0.3,0.9,1])
with col1 :
    if st.button("예약 확정") :
        if(send_res_val(res_info) == '1') :
            try :
                nav_page("sucsess")
            except :
                pass
        else :
            try :
                # send_res_val(res_info)
                my_js = """
                    alert("이미 예약이 되어있습니다.");
                    """
                my_html = f"<script>{my_js}</script>"
                html(my_html)
                nav_page("reservation")
            except :
                pass

        

with col2 :
    if st.button("돌아가기") :
        nav_page("myres_chg")