
mandatory_fields = { 
    "naml_eligible": "NAML Eligible?",
    "employee_count": "Total Employee Count",
    "current_assets": "Most Recent Year End Current Assets",
    "current_liabilities": "Most Recent Year End Current Liabilities",
    "total_assets": "Most Recent Year End Total Assets",
    "total_liabilities": "Most Recent Year End Total Liabilities",
    "net_income_loss": "Most Recent Year Net Income/Loss",
    "coverage": "Coverage(s)"
}

def find_missing(mandatory_fields, form_data):
    missing_fields = []
    for field, name in mandatory_fields.items():
        value = form_data.get(field)
        if value in (None, "", []):
            missing_fields.append(name)
    return missing_fields

form_data = {
    "naml_eligible": None,
    "employee_count": 1,
    "revenue": 1,
    "current_assets": None,
    "current_liabilities": 1,
    "total_assets": 1,
    "total_liabilities": 1,
    "net_income_loss": 1,
    "coverage": 1,
    "retained_earning": 1,
    "end_ebit": 1,
    "total_claims": None,
}

missing_fields = find_missing(mandatory_fields, form_data)
if missing_fields:
    print(missing_fields)

else:
    print("ok")