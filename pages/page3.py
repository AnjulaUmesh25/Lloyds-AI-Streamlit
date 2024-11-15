import streamlit as st
import requests
import json

from functions.functions import find_missing, find_missing_values


###########################################################
###########################################################

mandatory_fields = {
    # "naml_eligible":"NAML Eligible?",
    "employee_count":"Total Employee Count",
    "revenue":"Most Recent Year End Revenue",
    "current_assets":"Most Recent Year End Current Assets",
    "current_liabilities":"Most Recent Year End Current Liabilities",
    "total_assets":"Most Recent Year End Total Assets",
    "total_liabilities":"Most Recent Year End Total Liabilities",
    "net_income_loss":"Most Recent Year Net Income/Loss",
    "coverage":"Coverage(s)",
    # "retained_earning":"Most Recent Year End Retained Earnings",
    # "end_ebit":"Most Recent Year End EBIT",
    # "total_claims":"Total Claims",
}

###########################################################
###########################################################

def page(navigate_to):
    st.subheader("Financial Details")

    # Financial details form
    # UNDEFINED_1 = "Unclear"
    # naml_eligible = st.selectbox("NAML Eligible?", 
    #                              ["Yes", "No", "Unclear"], 
    #                              key="naml_eligible")
    
    employee_count = st.number_input("Total Employee Count", 
                                     min_value=1, 
                                     key="employee_count", 
                                     step=1,
                                    #  )
                                     value=st.session_state.form_data.get("financial", {}).get("employee_count", None))
    
    revenue = st.number_input("Most Recent Year End Revenue", 
                              key="revenue", step=1, 
                            #   value=None )
                              value=st.session_state.form_data.get("financial", {}).get("revenue", None))
    
    current_assets = st.number_input("Most Recent Year End Current Assets", 
                                     key="current_assets", step=1, 
                                    #  value=None )
                                     value=st.session_state.form_data.get("financial", {}).get("current_assets", None),)
    
    current_liabilities = st.number_input("Most Recent Year End Current Liabilities", 
                                          key="current_liabilities", step=1, 
                                        #   value=None )
                                          value=st.session_state.form_data.get("financial", {}).get("current_liabilities", None))
    
    total_assets = st.number_input("Most Recent Year End Total Assets", 
                                   key="total_assets", step=1, 
                                #    value=None )
                                   value=st.session_state.form_data.get("financial", {}).get("total_assets", None))
    
    total_liabilities = st.number_input("Most Recent Year End Total Liabilities", 
                                        key="total_liabilities", step=1, 
                                        # value=None) 
                                        value=st.session_state.form_data.get("financial", {}).get("total_liabilities", None))
    
    net_income_loss = st.number_input("Most Recent Year Net Income/Loss", 
                                      key="net_income_loss", step=1, 
                                    #   value=None )
                                      value=st.session_state.form_data.get("financial", {}).get("net_income_loss", None),)
    
    coverage = st.multiselect("Coverage(s)", 
                              ["D", "E", "F"], 
                              key="coverage",
                                # )
                              default=st.session_state.form_data.get("financial", {}).get("coverage", []))
    
    retained_earning = st.number_input("Most Recent Year End Retained Earnings", 
                                       key="retained_earning", step=1, 
                                    #    value=None )
                                       value=st.session_state.form_data.get("financial", {}).get("retained_earning", None))
    
    end_ebit = st.number_input("Most Recent Year End EBIT", 
                               key="end_ebit", step=1, 
                            #    value=None )
                               value=st.session_state.form_data.get("financial", {}).get("end_ebit", None))
    
    total_claims = st.number_input("Total Claims", 
                                   key="total_claims", step=1, 
                                #    value=None )
                                   value=st.session_state.form_data.get("financial", {}).get("total_claims", None))

    form_data = {
            "NAML_eligible": "Yes", #naml_eligible ,
            "employee_count": employee_count,
            "revenue": revenue,
            "current_assets": current_assets,
            "current_liabilities": current_liabilities,
            "total_assets": total_assets,
            "total_liabilities": total_liabilities,
            "net_income_loss": net_income_loss,
            "coverage": coverage,
            "retained_earning": retained_earning,
            "end_ebit": end_ebit,
            "total_claims": total_claims,
        }
    st.session_state.form_data["financial"] = form_data

    def go_to_previous():
        navigate_to("page2")

    def submit_form():

        # if not all([employee_count, current_assets, current_liabilities, total_assets, total_liabilities,
        #             net_income_loss, coverage, naml_eligible]):
        #     st.warning(f"WARNING: Please fill these missing fields - {find_missing(mandatory_fields)}")
        #     return
        missing_fields = find_missing_values(mandatory_fields, form_data)
        if missing_fields:
                        
            st.warning(f"WARNING: Please fill these missing fields - {missing_fields}")
            return
        
        else:
            # st.session_state.form_data["financial"] = form_data
            st.session_state.form_data_complete = True
            st.json(st.session_state.form_data)
            # navigate_to("page1")

    # Clear form function to reset all session state inputs
    def clear_form():
        # Reset the 'financial' form data
        st.session_state.form_data["financial"] = {}
        # for key in ["NAML_eligible", "employee_count", "revenue", "current_assets", 
        #             "current_liabilities", "total_assets", "total_liabilities", 
        #             "net_income_loss", "coverage", 
        #             "retained_earning", "end_ebit", "total_claims"]:
        #     if key in st.session_state.form_data["financial"]:
        #         del st.session_state.form_data["financial"][key]

    def new_form():
        st.session_state.form_data = {}
        # st.rerun()
        navigate_to("page1")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.button("Previous", on_click=go_to_previous)
    with col2:
        st.button("Submit", on_click=submit_form)
    with col3:
        st.button("Clear", on_click=clear_form) 

    st.button("Start New ", on_click=new_form)