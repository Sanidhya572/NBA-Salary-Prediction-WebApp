# import streamlit as st
# import pickle
# import sklearn
# import pandas as pd
# import numpy as np
# from PIL import Image
# model = pickle.load(open('model.sav', 'rb'))

# st.title('Player Salary Prediction')
# st.sidebar.header('Player Data')
# image = Image.open('bb.jpg')
# st.image(image, '')

# # FUNCTION
# def user_report():
#   rating = st.sidebar.slider('Rating', 50,100, 1 )
#   jersey = st.sidebar.slider('Jersey', 0,100, 1 )
#   team = st.sidebar.slider('Team', 0,30, 1 )
#   position = st.sidebar.slider('Position', 0,10, 1 )
#   country = st.sidebar.slider('Country', 0,3, 1 )
#   draft_year = st.sidebar.slider('Draft Year', 2000,2020, 2000)
#   draft_round = st.sidebar.slider('Draft Round', 1,10, 1)
#   draft_peak = st.sidebar.slider('Draft Peak', 1,30, 1)


#   user_report_data = {
#       'rating':rating,
#       'jersey':jersey,
#       'team':team,
#       'position':position,
#       'country':country,
#       'draft_year':draft_year,
#       'draft_round':draft_round,
#       'draft_peak':draft_peak
#   }
#   report_data = pd.DataFrame(user_report_data, index=[0])
#   return report_data

# user_data = user_report()
# st.header('Player Data')
# st.write(user_data)

# salary = model.predict(user_data)
# st.subheader('Player Salary')
# st.subheader('$'+str(np.round(salary[0], 2)))

# # Load custom CSS
# with open("style.css", "r") as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

# Load the pre-trained machine learning model
model = pickle.load(open('model.sav', 'rb'))

# Set up the Streamlit application
st.title('Player Salary Prediction')
st.sidebar.header('Player Data')

# Load and display an image
image = Image.open('bb.jpg')
st.image(image, '')

# Function to collect user input
def user_report():
    # Slider widgets for user input
    rating = st.sidebar.slider('Rating', 50, 100, 1)
    jersey = st.sidebar.slider('Jersey', 0, 100, 1)
    team = st.sidebar.slider('Team', 0, 30, 1)
    position = st.sidebar.slider('Position', 0, 10, 1)
    country = st.sidebar.slider('Country', 0, 3, 1)
    draft_year = st.sidebar.slider('Draft Year', 2000, 2020, 2000)
    draft_round = st.sidebar.slider('Draft Round', 1, 10, 1)
    draft_peak = st.sidebar.slider('Draft Peak', 1, 30, 1)

    # Store user input in a DataFrame
    user_report_data = {
        'rating': rating,
        'jersey': jersey,
        'team': team,
        'position': position,
        'country': country,
        'draft_year': draft_year,
        'draft_round': draft_round,
        'draft_peak': draft_peak
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

# Collect user data
user_data = user_report()

# Display user input
st.header('Player Data')
st.write(user_data)

# Predict player salary
salary = model.predict(user_data)
st.subheader('Player Salary')
st.subheader('$' + str(np.round(salary[0], 2)))

# Load custom CSS
with open("style.css", "r") as f:
    # Apply custom CSS styling
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Explanation of Streamlit functionality and usage
"""
Streamlit is a powerful tool for creating interactive web applications with just a few lines of Python code. Here's how it works:

1. Setting up the Application: Streamlit applications start with a title using the `st.title()` function, and additional components like sidebars and widgets can be added using functions like `st.sidebar.header()` and `st.sidebar.slider()`.

2. Collecting User Input: In this application, sliders are used to collect various player attributes such as rating, jersey number, team, etc. The `user_report()` function gathers this input and stores it in a DataFrame.

3. Displaying Data and Results: The collected user data is displayed using `st.write()`, and the predicted player salary is shown using `st.subheader()`. 

4. Custom Styling: Custom CSS styling can be applied to the application to enhance its appearance and user experience.

Streamlit simplifies the process of building data-driven web applications, allowing data scientists and developers to focus on the logic and analysis rather than the complexities of web development.
"""
