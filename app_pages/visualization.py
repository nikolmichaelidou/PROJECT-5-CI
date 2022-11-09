import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def visualization_leaves_page_body():
    st.write("## Cherry Leaves Visualizer")


version = 'v1'
if st.checkbox("..."):
    
    avg_healthy=plt.imread(f"outputs/{version}/avg_var_Healthy.png")
    avg_mildew = plt.imread(f"outputs/{version}/avg_var_Mildew.png")