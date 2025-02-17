import requests
import streamlit as st
from datetime import datetime
import pandas as pd

from tornado.options import options

API_url="http://localhost:8000"

def analytics_month_tab():
    selected_month = st.number_input("Enter Date", label_visibility="collapsed")
    if st.button("Get Analytics for month"):
        response = requests.get(f"{API_url}/expenses/by_month/{selected_month}")
        if response.status_code==200:
            response=response.json()

        else:
            st.error("Failed retrieve Expenses")
            existing_responses=[]
        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown By Category")

        st.bar_chart(data=df_sorted.set_index("Category")['Percentage'], width=0, height=0, use_container_width=True)

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)