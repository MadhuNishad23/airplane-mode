# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Products(Document):
	def validate(self):
		for name in self.names:
			if name.price < 0:
				frappe.throw("Price cannot be negative")

	def before_save(self):
		self.caculate_totals()
	
	def calculate_totals(self):
		total_amount = 0

		for name in self.names:
			total_amount += name.quantity * name.price

		discount = self.discount 
		payable_amount = total_amount - (total_amount * (discount / 100))

		self.total_amount = total_amount
		self.payable_amount = payable_amount
		