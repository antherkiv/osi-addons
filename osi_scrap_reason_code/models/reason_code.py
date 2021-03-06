# Copyright (C) 2018 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ReasonCode(models.Model):
    _name = "reason.code"
    _description = "Reason Code"

    name = fields.Char("Code", required=True)
    description = fields.Text("Description")
    location_id = fields.Many2one(
        "stock.location",
        string="Scrap Location",
        domain="[('scrap_location', '=', True)]")
