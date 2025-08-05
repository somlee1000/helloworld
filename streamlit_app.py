import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write("our table is below:")

# Example 3

df = pd.DataFrame({
     '이름': ["형원", 2, 3, 4],
     '소속': ["몬스타엑스", 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('최근 들은 노래:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['배고픔', '잠옴', '스트레스'])
c = alt.Chart(df2).mark_circle().encode(
     x='배고픔', y='잠옴', size='스트레스', color='스트레스', tooltip=['배고픔', '잠옴', '스트레스'])
st.write(c)