import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Participant Type", "fieldname": "participant_type", "fieldtype": "Data", "width": 120},
        {"label": "Participant", "fieldname": "participant", "fieldtype": "Data", "width": 160},
        {"label": "Department", "fieldname": "department", "fieldtype": "Data", "width": 150},
        {"label": "Event Name", "fieldname": "event_name", "fieldtype": "Data", "width": 200},
        {"label": "Category", "fieldname": "category", "fieldtype": "Data", "width": 120},
        {"label": "Event Date", "fieldname": "event_date", "fieldtype": "Date", "width": 110},
        {"label": "Certificate", "fieldname": "certificate", "fieldtype": "Data", "width": 100},
    ]
