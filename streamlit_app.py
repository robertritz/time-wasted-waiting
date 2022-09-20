import streamlit as st

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
from matplotlib.ticker import MaxNLocator

import functions

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.style.use("datafantic-right.mplstyle")

st.markdown("""# How much time have I wasted waiting for websites to load?
This calculator estimates the time you have wasted since you started using the internet waiting for websites to load. It also estimates how much time you will waste until you die. You can see the blog post that goes along with this app on [datafantic](https://datafantic.com/how-much-time-do-we-waste-waiting-for-websites-to-load).

The median time to wait for a website to become usable is **4 seconds**. Even worse, since 2010, the amount of time it takes a website to load **hasn't changed**. Our internet is faster, but we still wait. 

> Note: This app is for informational and entertainment purposes. It does not aim to estimate the precise amount of time you have or will waste.
---

""")

col1, col2 = st.columns(2)

with col1:
    age = st.slider(label="Your age", min_value=1, max_value=80, value=30)
    age_internet = st.slider(label="Your age when you started using the internet", min_value=1, max_value=80, value=13)
with col2:
    avg_webpages = st.slider(label="How many webpages do you visit per day?", min_value=10, max_value=500, value=50, step=10)
    waiting_seconds = st.slider(label="Seconds waiting per webpage", min_value=0.5, max_value=4.0, value=4.0, step=0.5)
calculate = st.button("Calculate my time wasted!")

if calculate:
    #
    # Make chart for wasted time up until today
    #
    x, y = functions.waiting_time(age, age_internet, avg_webpages, waiting_seconds)

    st.markdown(f"""
    #### You have wasted {round(y[-1], 2)} days of your life waiting for websites to load.
    
    """)

    fig = functions.plot_time_wasted(x, y, age, age_internet, waiting_seconds, avg_webpages)
    st.pyplot(fig)

    st.markdown("""---""")
    #
    # Make chart for wasted time until you die
    #
    life_expectancy = 80
    x_life, y_life = functions.waiting_time_life(age, life_expectancy, age, avg_webpages, waiting_seconds)
    st.markdown(f"""
    #### In the next {life_expectancy - age} years you will waste {round(y_life[-1], 2)} days waiting for websites to load.
    """)
    fig2 = functions.plot_lifetime_wasted(x_life, y_life, life_expectancy, age, waiting_seconds, avg_webpages)
    st.pyplot(fig2)

    #
    # Calculate time that could be saved
    #
    st.markdown(f"""
    ##### If webpage load times are lowered to 1 second on average, you could save {round(y_life[-1] * .25, 2)} days of your life. Let's speed up the net!
    """)
