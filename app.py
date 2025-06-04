import streamlit as st
import pandas as pd

st.title("H1B Job Title Insight Dashboard")
df = pd.read_csv("h1b_clean_2025.csv")


st.write("Preview of H1B Data:")
st.dataframe(df.head()) # to show just 5 lines of the df by default

keyword = st.text_input("Enter a job title keyword (e.g., 'Data', 'Software'):") #the input from the user

if keyword:
    filtered_df = df[df["job_title"].str.contains(keyword, case=False, na=False)]
    st.write(f"Found {len(filtered_df)} records matching '{keyword}'") #f-string in python is suitable for dynamic strings
    st.dataframe(filtered_df[["employer", "job_title", "state", "avg_salary", "case_status"]].head(20))
else:
    st.write("Please enter a keyword to explore job titles.")

