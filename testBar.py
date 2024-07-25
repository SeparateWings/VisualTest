import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# 创建一个数据集
np.random.seed(0)
n = 10
df = pd.DataFrame({
  'x': range(n),
  'y': np.random.rand(n),
  'color': np.random.choice(['#ff0000', '#00ff00', '#0000ff'], n)
})

# 创建一个条形图
chart = alt.Chart(df).mark_bar().encode(
    x='x:O',
    y='y:Q',
    color=alt.Color('color:N', scale=None)  # 使用数据集中的颜色
)

st.altair_chart(chart)
