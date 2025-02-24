import streamlit as st
import pandas as pd
import math
import numpy as np
import random

from pathlib import Path


st.set_page_config(
    page_title='Dinner Spinner',
    page_icon=':pizza:', # This is an emoji shortcode. Could be a URL too.
)


'''
# :pizza: Dinner Spinner 

browse ur meals n eat for reals 
'''
foodytoody = {"burger": ":hamburger:",
              "Burrito": ":burrito:",
              "Tacos": ":taco:",
              "Fancy callan rice": ":rice:",
              "Noods n dumps": ":ramen:"}
st.write(foodytoody)

st.write(f"{foodytoody}")
st.write(random.choice(foodytoody))

data = ["Burrito", ":hamburger: burgers", "Pasta", "Rissotto", "Stir-Fry", "Yiros"]
st.write(f"{data}")

st.write(f"winner winner, {random.choice(foodytoody)} for dinner")







