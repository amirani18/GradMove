#Import statements
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
import numpy as np

#Reading in data

cost = pd.read_csv('archive/cost.csv')

#Data cleaning and preparation
baseline = cost['No. of abortion providers'].median()

# func
def abs_dev():
    #Data cleaning and preparation
    baseline = cost['No. of abortion providers'].median()

    #Standard deviation:
    copy = cost.copy()
    data = copy['No. of abortion providers']
    outliers = [419, 252]
    copy = [x for x in data if x not in outliers]
    absolute_deviations = [abs(x - baseline) for x in copy]
    variance = np.mean(np.square(absolute_deviations))
    std_based_on_median = np.sqrt(variance)
    return std_based_on_median

#Determine access intervals 
#On average, tech hubs differ by 15 in terms of abortion providers
#High access to providers: 56+
#Low access to providers: 0-26
#Avg access to providers: 41-56

# Visual

def provider_by_state(input_state):
    # Check if the input_state is in the DataFrame
    if input_state in cost['State'].values:
        
        # Get the row from the DataFrame for the matching state
        state_row = cost[cost['State'] == input_state]
        # Extract the accessibility score for this state
        return state_row['No. of abortion providers'].iloc[0]
    else:
        return None

# Get the provider count for the input state
def count_var(input_state):
    count = provider_by_state(input_state)
    return count

#High access to providers: 56+
#Low access to providers: 0-26
#Avg access to providers: 41-56

def categorize_access(count):
    avg_access = (41, 56)
    low_access = (0, 26)
    high_access = (56, max(cost['No. of abortion providers']))
    
    if high_access[0] <= count <= high_access[1]:
        return 'High'
    elif avg_access[0] <= count <= avg_access[1]:
        return 'Average'
    elif low_access[0] <= count <= low_access[1]:
        return 'Low'
    else:
        return 'Undefined'

def access_lvl_category(count):
    access_level = categorize_access(count)
    return access_level
    
# Visual for Annual Abortion Cost Saved Through Effective Contraceptives
title_x = cost[['State', 'Abortion Costs Saved at Title X Funded Centers']]
public = cost[['State', 'Abortion Costs Saved at Publicly Funded Family Planning Centers']]


def generate_chart(input_state):
    count = provider_by_state(input_state)
    if count is not None:
        access_level = categorize_access(count)
        
        # Filter the data for the given state
        state_data = cost[cost['State'] == input_state]
        title_x = state_data['Abortion Costs Saved at Title X Funded Centers'].iloc[0]
        public = state_data['Abortion Costs Saved at Publicly Funded Family Planning Centers'].iloc[0]
        
        # Check if costs saved in either Title X or public are less than $5
        if title_x < 5 and public < 5:
            st.write(f"Due to limited abortion options, the abortion costs via Title X are {title_x}.")
            st.write(f"Due to limited abortion options, the abortion costs via public centers are {public}.")
            
            
        elif title_x < 5 or public < 5:
            st.write(f"Due to limited abortion options, the abortion costs ($) via Title X are {title_x}")
            st.write(f"Due to limited abortion options, the abortion costs ($) via public centers are {public}")
            
        else:
            if access_level == "Low":
                fig, ax = plt.subplots(figsize=(8, 6))
                bar_width = 0.35
                ax.bar(0, title_x, color='skyblue', width=bar_width, edgecolor='grey', label='Title X Funded Centers')
                ax.bar(1, public, color='salmon', width=bar_width, edgecolor='grey', label='Publicly Funded Centers')
                ax.set_xlabel('Funding Source', fontsize=12, fontweight='bold')
                ax.set_ylabel('Cost ($)', fontsize=12, fontweight='bold')
                ax.set_title(f"Average Abortion Costs Saved in {input_state}", fontsize=14, fontweight='bold')
                ax.set_xticks([0, 1])
                ax.set_xticklabels(['Title X', 'Public'])
                ax.legend()
                plt.tight_layout()
                st.pyplot(fig)
            elif access_level == "Avg":
                fig, ax = plt.subplots(figsize=(8, 6))
                bar_width = 0.35
                ax.bar(0, title_x, color='skyblue', width=bar_width, edgecolor='grey', label='Title X Funded Centers')
                ax.bar(1, public, color='salmon', width=bar_width, edgecolor='grey', label='Publicly Funded Centers')
                ax.set_xlabel('Funding Source', fontsize=12, fontweight='bold')
                ax.set_ylabel('Cost ($)', fontsize=12, fontweight='bold')
                ax.set_title(f"Average Abortion Costs Saved in {input_state}", fontsize=14, fontweight='bold')
                ax.set_xticks([0, 1])
                ax.set_xticklabels(['Title X', 'Public'])
                ax.legend()
                plt.tight_layout()
                st.pyplot(fig)
            else:
                fig, ax = plt.subplots(figsize=(8, 6))
                bar_width = 0.35
                ax.bar(0, title_x, color='skyblue', width=bar_width, edgecolor='grey', label='Title X Funded Centers')
                ax.bar(1, public, color='salmon', width=bar_width, edgecolor='grey', label='Publicly Funded Centers')
                ax.set_xlabel('Funding Source', fontsize=12, fontweight='bold')
                ax.set_ylabel('Cost ($)', fontsize=12, fontweight='bold')
                ax.set_title(f"Average Abortion Costs Saved in {input_state}", fontsize=14, fontweight='bold')
                ax.set_xticks([0, 1])
                ax.set_xticklabels(['Title X', 'Public'])
                ax.legend()
                plt.tight_layout()
                st.pyplot(fig)
                

