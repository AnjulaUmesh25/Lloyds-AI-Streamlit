import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import importlib


from functions.functions import get_access_token
from requests.auth import HTTPBasicAuth


#####################################
#####################################
st.title("Lloyd's AI Predictor")


# Set up session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

if 'response_data' not in st.session_state:
    st.session_state.response_data = None  # To store the API response

# Navigation function
def navigate_to(page):
    st.session_state.page = page

# Main app layout
if st.session_state.page == 'page1':
    page1 = importlib.import_module('pages.page1')
    page1.page(navigate_to)

elif st.session_state.page == 'page2':
    page2 = importlib.import_module('pages.page2')
    page2.page(navigate_to)

elif st.session_state.page == 'page3':
    page3 = importlib.import_module('pages.page3')
    page3.page(navigate_to)

# Display the final form data after submission
if st.session_state.get('form_data_complete'):

    final_form = st.session_state.form_data
    st.success("Data successfully submitted!")

    st.write("Response:")
    # print(final_form)

    token = get_access_token()
    if token:
        try:
            # Make the API request with Bearer token in headers
            headers = {"Authorization": f"Bearer {token}"}
            res = requests.post(
                url="http://127.0.0.1:8000/risk",
                data=json.dumps(final_form),
                headers=headers
            )
            # Raise an error for bad status
            res.raise_for_status()
            res_json = res.json()
            st.json(res_json)
            print(res_json)
            st.session_state.form_data_complete = False
            # Delete all the items in Session state
            # st.session_state.form_data = {}
            # for key in st.session_state.keys():
            #     del st.session_state.form_data[key]

            # st.session_state.response_data = res_json

        except requests.exceptions.HTTPError as http_err:
            # Display specific HTTP error message
            st.error(f"HTTP error occurred: {http_err}")
            # Display the error response from the server
            st.error(f"Error details: {res.text}")

        except requests.exceptions.RequestException as req_err:
            # Display generic request error message
            st.error(f"Request failed: {req_err}")

        except ValueError:
            # Display an error if JSON decoding fails
            st.error("ERROR: Invalid JSON response from server.")