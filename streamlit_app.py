import streamlit as st
import pandas as pd
import math
import numpy as np
import random
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Dinner Spinner',
    page_icon=':pizza:', # This is an emoji shortcode. Could be a URL too.
)


'''
# :pizza: Dinner Spinner 

browse ur meals n eat for reals 
'''

data = ["m12", "m23", "m47", "m6", "m52", "m19"]


st.write(f"winner winner, {random.choice(data)} for dinner")







