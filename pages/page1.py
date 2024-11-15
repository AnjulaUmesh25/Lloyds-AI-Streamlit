import streamlit as st
import pandas as pd
from functions.functions import states, zip_codes, state_to_abbreviation, find_missing, find_missing_values

###########################################################
###########################################################

mandatory_fields = {
    "broker_name":"Name",
    "broker_organization":"Organization",
    "broker_address":"Address",
    "broker_city":"City",
    # "broker_state":"State",
    # "broker_zipcode":"Zip Code",
    "broker_delegate":"Delegate",
}

###########################################################
###########################################################

def page(navigate_to):
    st.subheader("Broker Details")
    
    # Broker details form
    broker_name = st.text_input("Name", key="broker_name", 
                                value=st.session_state.form_data.get("broker", {}).get("name", None))
    
    broker_organization = st.text_input("Organization", key="broker_organization", 
                                        value=st.session_state.form_data.get("broker", {}).get("organization", None))
    broker_address = st.text_input("Address", key="broker_address", 
                                   value=st.session_state.form_data.get("broker", {}).get("address", None))
    broker_city = st.text_input("City", key="broker_city", 
                                value=st.session_state.form_data.get("broker", {}).get("city", None))

    broker_state = st.selectbox("State", states(), key="broker_state",
                                index=states().index(st.session_state.form_data.get("broker", {}).get("state", states()[0])))  # Example list of states
    
    # broker_zipcode = st.selectbox("Zip Code", zip_codes(), key="broker_zipcode")
    broker_zipcode = st.text_input("Zip Code", key="broker_zipcode",
                                   value=st.session_state.form_data.get("broker", {}).get("zipcode", None))

    broker_delegate = st.text_input("Delegate", key="broker_delegate",
                                    value=st.session_state.form_data.get("broker", {}).get("delegate", None))

    form_data = {
        'name': broker_name,
        'organization': broker_organization,
        'address': broker_address,
        'city': broker_city,
        'state': broker_state,
        'zipcode': str(broker_zipcode),
        'delegate': broker_delegate,
    }
    st.session_state.form_data["broker"] = form_data

    # Save broker data
    def go_to_next():

        if not all([form_data[field] for field in form_data]):
            st.warning(f"WARNING: Please fill these missing fields - {find_missing(mandatory_fields)}")
            return 
        
        if not broker_zipcode or not (broker_zipcode.isdigit() and len(broker_zipcode) == 5) :
            st.warning("WARNING: Invalid Zip Code format, Please enter a 5-digit numerical code.")
            return
        
        # missing_fields = find_missing_values(mandatory_fields, form_data)
        # if missing_fields:
        #     st.warning(f"WARNING: Please fill these missing fields - {missing_fields}")
        #     return
        # st.session_state.form_data["broker"] = form_data
        st.json(st.session_state.form_data)
        navigate_to("page2")

    def clear_form():
        # Reset the 'financial' form data
        st.session_state.form_data["broker"] = {}
        # for key in ["name", "organization", "address", 
        #             "city", "state", "zipcode", "delegate"]:
        #     if key in st.session_state.form_data["broker"]:
        #         del st.session_state.form_data["broker"][key]


    col1, col2 = st.columns(2)

    with col1:
        st.button("Next", on_click=go_to_next)
    with col2:
        st.button("Clear", on_click=clear_form) 
        


