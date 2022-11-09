import streamlit as st
import matplotlib.pyplot as plt


def summary_page_body():
    st.title('Dataset summary')
    st.write(
        f"This dataset contains 2104 images"
    )
