import pandas as pd
import requests
import streamlit as st


state_to_abbreviation = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
    'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
    'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY', 'Washington, D.C.': 'DC'
}

@st.cache_data
def zip_codes():
  zip_code_df = pd.read_csv('functions/zcta_place_rel_10.txt', sep=',')
  return zip_code_df['ZCTA5'].to_list()

@st.cache_data
def states():
  return list(state_to_abbreviation.keys())

###########################################################
###########################################################

def find_missing(mandatory_fields):
    missing_fields = []
    for field, name in mandatory_fields.items():
        value = st.session_state.get(field)  
        if value in (None, "", []):  
            missing_fields.append(name)

    return missing_fields

def find_missing_values(mandatory_fields, form_data):
    missing_fields = []
    for field, name in mandatory_fields.items():
        value = form_data.get(field)
        if value in (None, "", []):
            missing_fields.append(name)
    return missing_fields

###########################################################
###########################################################

def validate_naics_code(code):
    """Validates a NAICS code to ensure it's 6 digits long."""
    try:
        int(code)
        return len(code) == 6
    except ValueError:
        return False
    
###########################################################
###########################################################

token_url = "http://127.0.0.1:8000/token"
username = "anjula"
password = "anjulalloyeds2025"

# Function to get access token using password grant type
@st.cache_data
def get_access_token():
    response = requests.post(
        token_url,
        data={
            "grant_type": "password",
            "username": username,
            "password": password,
        }
    )
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        st.error(f"ERROR: Failed to retrieve access token: {response.status_code} - {response.text}")
        return None
    

###########################################################
###########################################################


