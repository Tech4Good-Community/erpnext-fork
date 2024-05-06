# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TaskUtilisation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		naming_series: DF.Literal["TASK-UTIL-"]
		project: DF.Link | None
		task: DF.Link | None
		task_budget: DF.Currency
		utilisation_value: DF.Currency
	# end: auto-generated types

     
