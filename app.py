import streamlit as st
from app_pages.multipage import MultiPage

app = MultiPage(app_name="Cherry Leaves Mildew Detector")

#page scripts
from app_pages.summary_page import summary_page_body


app.run()