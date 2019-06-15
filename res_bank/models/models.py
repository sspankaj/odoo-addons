# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResBank(models.Model):

    _inherit = "res.bank"

    nuban = fields.Boolean(string="NUBAN")
