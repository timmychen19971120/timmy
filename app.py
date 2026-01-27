import streamlit as st
import pandas as pd
import datetime
import os

st.set_page_config(page_title="Timmy 的體重紀錄", page_icon="⚖️")

st.title("⚖️ 體重快速紀錄")

# 輸入區
with st.form("weight_form", clear_on_submit=True):
    date = st.date_input("日期", datetime.date.today())
    weight = st.number_input("體重 (kg)", min_value=30.0, max_value=150.0, step=0.1)
    note = st.text_input("備註")
    submit = st.form_submit_button("確認儲存")

    if submit:
        new_row = pd.DataFrame([[date, weight, note]], columns=["日期", "體重", "備註"])
        file = "data.csv"
        if not os.path.isfile(file):
            new_row.to_csv(file, index=False)
        else:
            new_row.to_csv(file, mode='a', header=False, index=False)
        st.success(f"已紀錄：{weight} kg")

# 顯示區
st.divider()
if os.path.isfile("data.csv"):
    df = pd.read_csv("data.csv")
    st.line_chart(df.set_index("日期")["體重"])
    st.dataframe(df.tail(10), use_container_width=True)
