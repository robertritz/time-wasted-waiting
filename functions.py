import numpy as np

import matplotlib.pyplot as plt
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
from matplotlib.ticker import MaxNLocator

## Convenience functions
def waiting_time(age, internet, avg_webpages, waiting_seconds):
    seconds_year = avg_webpages * 365 * waiting_seconds
    days_year = seconds_year / 60 / 60 / 25
    x = np.arange(0, age + 1, 1)
    
    y = []
    total = 0 
    for item in x:
        if item < internet:
            y.append(0)
        else:
            total += days_year
            y.append(total)
    return x, y

def waiting_time_life(age, life_expectancy, internet, avg_webpages, waiting_seconds):
    seconds_year = avg_webpages * 365 * waiting_seconds
    days_year = seconds_year / 60 / 60 / 25
    x_life = np.arange(age+1, life_expectancy + 1, 1)
    
    y_life = []
    total_life = 0
    for item in x_life:
        total_life += days_year
        y_life.append(total_life)
    return x_life, y_life

## Plotting functions
def plot_time_wasted(x, y, age, age_internet, waiting_seconds, avg_webpages):
    fig, ax = plt.subplots()
    ax.bar(x, y)

    # Add in title and subtitle
    ax.set_title("""Ain't nobody got time for that""")
    ax.text(x=.08, y=.87, 
            s=f"Your estimated number of days waiting for websites to load, ages {age_internet}-{age}.", 
            transform=fig.transFigure, 
            ha='left', 
            fontsize=18, 
            alpha=.8)
    ax.text(x=.08, y=.84, 
            s=f"Assumes viewing {avg_webpages} webpages per day & {waiting_seconds} seconds wait per page.", 
            transform=fig.transFigure, 
            ha='left', 
            fontsize=18, 
            alpha=.8)

    ax.set_ylim(0, round(y[-1]) + 2)
    ax.set_xlim(age_internet-1, age+2)

    ax.set_xlabel('Age')
    ax.set_ylabel('Days Waiting')
    ax.yaxis.set_label_position("right")

    ax.yaxis.set_major_locator(MaxNLocator(min_n_ticks=5, prune='upper', integer=True))

    # Set the logo
    logo = plt.imread('images/datafantic.png')
    imagebox = OffsetImage(logo, zoom=.22)
    ab = AnnotationBbox(imagebox, xy=(1,1.08), xycoords='axes fraction', box_alignment=(1,1), frameon = False)
    ax.add_artist(ab)
    return fig


def plot_lifetime_wasted(x_life, y_life, life_expectancy, age, waiting_seconds, avg_webpages):
    fig, ax = plt.subplots()
    ax.bar(x_life, y_life)

    # Add in title and subtitle
    ax.set_title("""A lifetime of waiting""")
    ax.text(x=.08, y=.87, 
            s=f"Your estimated number of days waiting for websites to load, ages {age}-{life_expectancy}.", 
            transform=fig.transFigure, 
            ha='left', 
            fontsize=18, 
            alpha=.8)
    ax.text(x=.08, y=.84, 
            s=f"Assumes viewing {avg_webpages} webpages per day & {waiting_seconds} seconds wait per page.", 
            transform=fig.transFigure, 
            ha='left', 
            fontsize=18, 
            alpha=.8)

    ax.set_ylim(0, round(y_life[-1]) + 3)
    ax.set_xlim(age, life_expectancy+4)

    ax.set_xlabel('Age')
    ax.set_ylabel('Days Waiting')
    ax.yaxis.set_label_position("right")

    ax.yaxis.set_major_locator(MaxNLocator(min_n_ticks=5, prune='upper', integer=True))

    # Set the logo
    logo = plt.imread('images/datafantic.png')
    imagebox = OffsetImage(logo, zoom=.22)
    ab = AnnotationBbox(imagebox, xy=(1,1.08), xycoords='axes fraction', box_alignment=(1,1), frameon = False)
    ax.add_artist(ab)