import streamlit as st
from analytics_ui import analytics_tab
from  app_update_ui import app_update_tab
from analytics_by_month import analytics_month_tab


st.title("Expense Tracking System")

tab1,tab2,tab3=st.tabs(["Add/Update","Analytics By Category","Analytics By Month"])

with tab1:
    app_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_month_tab()