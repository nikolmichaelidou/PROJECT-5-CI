import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.summary_page import summary_page_body
from app_pages.visualization import visualization_leaves_page_body

app = MultiPage(app_name="Cherry Leaves Mildew Detector")

app.add_page("Quick Project Summary", summary_page_body)
app.add_page("Visualizer", visualization_leaves_page_body)

app.run()