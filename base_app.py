"""

    Simple Streamlit webserver application for serving developed classification
    models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Plase follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
    application. You are expected to extend the functionality of this script
    as part of your predict project.

    For further help with the Streamlit framework, see:

    https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os
from PIL import Image

# Data dependencies
import pandas as pd

# Load pipeline model

model = joblib.load('resources/lscv_model.pkl')

# Load your raw data
raw = pd.read_csv("resources/train.csv")

# Function to load images
# Images
def load_images(file_name):
	img = Image.open(file_name)
	return st.image(img,width=100)

# The main function where we will build the actual app
def main():
    """Tweet Classifier App with Streamlit """

    # Creates a main title and subheader on your page -
    # these are static across all pages
    # st.title("Climate Change Belief Predictor")
    # st.subheader("Predict if a person believes in climate change based on thier tweet")
    
    html_temp = """
	<div style="background-color:lightblue;padding:10px">
	<h2 style="color:white;text-align:center;">Climate Change Belief Predictor </h2>
	</div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    st.subheader("Predict if a person believes in climate change based on thier tweet")
    
    # Creating sidebar with selection box -
    # you can create multiple pages this way
    options = ["Prediction", "Information"]
    selection = st.sidebar.selectbox("Choose Option", options)

    # Building out the "Information" page
    if selection == "Information":
        st.info("General Information")
        # You can read a markdown file from supporting resources folder
        st.markdown("Some information here")

        st.subheader("Raw Twitter data and label")
        if st.checkbox('Show raw data'): # data is hidden if box is unchecked
            st.write(raw[['sentiment', 'message']]) # will write the df to the page

    # Building out the predication page
    if selection == "Prediction":
        #st.info("Prediction with ML Models")
        # Creating a text box for user input
        tweet_text = st.text_area("Enter Tweet")

        if st.button("Classify"):
                  
            # Transforming user input with vectorizer
            vect_text = [tweet_text]
            prediction = model.predict(vect_text)
              
            if prediction[0] == 0:
                prediction = 'Neutral'
                c_img = 'neutral.png'

            elif prediction[0] == 1:
                prediction = 'PRO Climate Change'
                c_img = 'pro.png'

            elif prediction[0] == 2:
                prediction = 'Factual News'
                c_img = 'news.png'

            else:
                prediction = 'ANTI Climate Change'
                c_img = 'anti.png'
  

            # When model has successfully run, will print prediction
            # You can use a dictionary or similar structure to make this output
            # more human interpretable.
            st.success("This Tweet is : {}".format(prediction))
            load_images(c_img)
            

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()
