import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Setting page title
st.set_page_config(page_title="Heart Failure APP")
st.title("Heart Failure App")
st.subheader("Heart Fialure")

#import Heart failure dataset
hf_data=pd.read_csv('heart_failure.csv')
st.write(hf_data)

#side bar
st.sidebar.header("Pick two variables for your Scatterplot")
x_val= st.sidebar.selectbox("Pick your x-axis", list(hf_data.select_dtypes(include=np.number).columns.tolist()))
y_val= st.sidebar.selectbox("Pick your y-axis", list(hf_data.select_dtypes(include=np.number).columns.tolist()))

#create Scatterplot
scatter=alt.Chart(hf_data,title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip=[x_val,y_val]
)
#Display the Scatterplot
st.altair_chart(scatter,use_container_width=True)

#calculate the correlation
corr=round(hf_data[x_val].corr(hf_data[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val}is {corr}")