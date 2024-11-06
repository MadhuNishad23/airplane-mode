import frappe

def execute():
    vehicles = frappe.db.get_all("Vehicles")
    for v in vehicles:
        vehicle = frappe.get_doc("Vehicles", v)
        vehicle.set_title()
        vehicle.save()

    frappe.db.commit()