#Import statements
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
import numpy as np

#Reading in data

access = pd.read_csv('/archive/access.csv')

#Data cleaning for access csv

county_counts = {'California': 58, 'Georgia': 159, 'Illinois': 102, 'Washington': 39,  'Colorado': 64, 'Kansas': 105, 
                 'New York': 62, 'Texas': 254, 'Pennsylvania': 67, 'Massachusetts': 14}

# Map county counts to states
access['County Count Per State'] = df_new['State'].map(county_counts)

# baseline % of county without clinic to determine high/low access

baseline = access['(%) Counties without Clinic'].mean()
stdev = access['(%) Counties without Clinic'].std()

print(baseline) #On average, the majority (71%) of counties in a state do not have a clinic.
print(stdev) #On average, this differs by 24 %

#Considering the mean is 71.8, avg access is 47-71, low access is 71-95, high access = <0-47
#Shade background red based on low, yellow based on avg, and green based on high?

# Check if a score is within the high access range

input_state = 'Kansas'

def get_score_by_state(input_state):
    # Check if the input_state is in the DataFrame
    if input_state in access['State'].values:
        
        # Get the row from the DataFrame for the matching state
        state_row = access[access['State'] == input_state]
        # Extract the accessibility score for this state
        return state_row['(%) Counties without Clinic'].iloc[0]
    else:
        return None


# Get the score for the input state
score = get_score_by_state(input_state)

def categorize_access(score):
    avg_access_range = (48, 72)
    low_access_range = (72, max(access['(%) Counties without Clinic']))
    high_access_range = (0, 47)
    
    if high_access_range[0] <= score <= high_access_range[1]:
        return 'High', 'green'
    elif avg_access_range[0] <= score <= avg_access_range[1]:
        return 'Average', 'yellow'
    elif low_access_range[0] <= score <= low_access_range[1]:
        return 'Low', 'red'
    else:
        return 'Undefined', 'grey'

access_level = categorize_access(score)
print(f"The access level is {access_level} for a score of {score}.")

import plotly.graph_objs as go

# Function to draw the gauge chart
def draw_gauge_chart(score, title="Clinic Accessibility"):
    # Get the access level and color based on the percentage
    access_level, color = categorize_access(score)
    
    # Draw the gauge chart using Plotly
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode = "gauge+number",
        value = score,
        title = {'text': title},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': color}, # the bar color
            'steps' : [
                {'range': [score, 100], 'color': 'lightgray', 
                    'thickness': 0.5},
            ],
        }
    ))
    
    # note to make it dependent on input
    
    caption = go.layout.Annotation(
    text=f"% of counties without abortion clinics",
    showarrow=False,
    xref="paper",
    yref="paper",
    x=0,
    y=-0.2,
    font=dict(size=24),
    align='center',
   )

    fig.update_layout(annotations=[caption])
    fig.show()

# Example usage:
input_state = 'Kansas'  # Replace with the actual state name
score = get_score_by_state(input_state)
if score is not None:
    draw_gauge_chart(score)
else:
    print(f"No data available for {input_state}.")
