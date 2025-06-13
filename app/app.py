import streamlit as st
import pandas as pd
import plotly.express as px
import os
import io

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) 
csv_path = os.path.join(BASE_DIR, "data", "h1b_clean_2025.csv")

df = pd.read_csv(csv_path)

st.title("H1B Job Title Insight Dashboard")
# df = pd.read_csv("data/h1b_clean_2025.csv")


st.write("Preview of H1B Data:")
st.dataframe(df.head()) # to show just 5 lines of the df by default

with st.sidebar:
        st.header("🔍 Filter")
        keyword = st.text_input("Enter a job title keyword", placeholder="e.g. Data, Software")

if keyword:
    filtered_df = df[df["job_title"].str.contains(keyword, case=False, na=False)]
    st.write(f"Found {len(filtered_df)} records matching '{keyword}'") #f-string in python is suitable for dynamic strings
    
    tab1, tab2, tab3 = st.tabs(["📋 Table View", "📊 Salary Chart", "🥧 Approval Pie"])
    
    with tab1:
        st.dataframe(filtered_df[["employer", "job_title", "state", "estimated_yearly_salary", "case_status"]].head(20))
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download Filtered Data as CSV",
            data=csv,
            file_name="filtered_h1b_data.csv",
            mime="text/csv"
        )

    
    with tab2:
        top_salary = (
            filtered_df[filtered_df["case_status"] == "Certified"]
            .groupby("employer")["estimated_yearly_salary"]
            .median()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
        
        st.write("Top 10 salaries:")
        st.dataframe(top_salary)
        
        fig1 = px.bar(
            top_salary,
            x="employer",
            y="estimated_yearly_salary",
            title=f"Top 10 Employers by estimated_yearly_salary for '{keyword}'",
            labels={"estimated_yearly_salary": "estimated_yearly_salary", "employer": "Employer"},
        )
        st.plotly_chart(fig1)
        
    with tab3:
        case_counts = (
            filtered_df["case_status"]
            .value_counts()
            .reset_index()
        )
        
        case_counts.columns = ["status", "count"]

        fig2 = px.pie(
            case_counts,
            values="count",
            names="status",
            title=f"Approval vs Denial for '{keyword}'"
        )
        st.plotly_chart(fig2)
else:
    st.write("Please enter a keyword to explore job titles.")
    


