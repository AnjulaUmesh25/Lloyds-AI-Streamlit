import streamlit as st
import pandas as pd
# from data_list import zip_codes, states
from functions.functions import states, validate_naics_code, find_missing, find_missing_values, zip_codes


###########################################################
###########################################################

mandatory_fields = {
    "applicant_name":"Name",
    "applicant_address":"Address",
    "applicant_city":"City",
    # "applicant_state":"State",
    # "applicant_zipcode":"Zip Code",
    "applicant_naics":"NAICS/NOPS",
}


###########################################################
###########################################################


def page(navigate_to):
    st.subheader("Applicant Details")
    
    # Applicant details form
    applicant_name = st.text_input("Name", key="applicant_name",
                                   value=st.session_state.form_data.get("applicant", {}).get("name", None))
    
    applicant_address = st.text_input("Address", key="applicant_address",
                                      value=st.session_state.form_data.get("applicant", {}).get("address", None))
    
    applicant_city = st.text_input("City", key="applicant_city",
                                   value=st.session_state.form_data.get("applicant", {}).get("city", None))
    
    applicant_state = st.selectbox("State", states(), key="applicant_state",
                                   index=states().index(st.session_state.form_data.get("applicant", {}).get("state", states()[0])))
    
    # applicant_zipcode = st.selectbox("Zip Code", zip_codes(), key="applicant_zipcode")
    applicant_zipcode = st.text_input("Zip Code", key="applicant_zipcode",
                                      value=st.session_state.form_data.get("applicant", {}).get("zipcode", None))
    
    applicant_naics = st.text_input("NAICS/NOPS", key="applicant_naics",
                                    value=st.session_state.form_data.get("applicant", {}).get("naics", None))

    form_data = {
                "name": applicant_name,
                "address": applicant_address,
                "city": applicant_city,
                "state": applicant_state,
                "zipcode": str(applicant_zipcode),
                "naics": str(applicant_naics),
            }
    st.session_state.form_data["applicant"] = form_data

    def go_to_previous():
        navigate_to("page1")

    def go_to_next():
                
        if not all([form_data[field] for field in form_data]):
            st.warning(f"WARNING: Please fill these missing fields - {find_missing(mandatory_fields)}")
            return
        # missing_fields = find_missing_values(mandatory_fields, form_data)
        # if missing_fields:
        #     st.warning(f"WARNING: Please fill these missing fields - {missing_fields}")
        #     return

        if not applicant_naics or not (applicant_naics.isdigit() and len(applicant_naics) == 6) :
            st.warning("WARNING: Invalid NAICS/NOPS Code, Please enter a 6-digit numerical code.")
            return
        if not applicant_zipcode or not (applicant_zipcode.isdigit() and len(applicant_zipcode) == 5) :
            st.warning("WARNING: Invalid Zip Code format, Please enter a 5-digit numerical code.")
            return

        else:
            # st.session_state.form_data["applicant"] = form_data
            st.json(st.session_state.form_data)
            navigate_to("page3")

    def clear_form():
        # Reset the 'applicant' form data
        st.session_state.form_data["applicant"] = {}
        # for key in ["name", "address", "city",
        #             "state", "zipcode", "naics"]:
        #     if key in st.session_state.form_data["applicant"]:
        #         del st.session_state.form_data["applicant"][key]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("Previous", on_click=go_to_previous)
    with col2:
        st.button("Next", on_click=go_to_next)
    with col3:
        st.button("Clear", on_click=clear_form) 