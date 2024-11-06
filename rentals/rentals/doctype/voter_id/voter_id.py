# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class VoterID(Document):
	def validate(self):
		if self.age <= 18:
			frappe.throw("You are not eligible for vote")
