# -*- coding: utf-8 -*-
# Copyright 2016 Ursa Information Systems <http://ursainfosystems.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    caloric_intake = fields.Float("Calories")
    caloric_intake_uom = fields.Many2one(
        "product.uom", "Calories UoM",
        domain=lambda self: [('category_id', '=',
                              self.env.ref(
                                  'product_uom.product_category_energy').id)]
    )
    carbohydrate_intake = fields.Float("Carbohydrate")
    carbohydrate_intake_uom = fields.Many2one(
        "product.uom", "Carbohydrate UoM",
        domain=lambda self: [('category_id', '=',
                              self.env.ref('product.product_uom_categ_kgm').id)
                             ]
    )
    fat_intake = fields.Float("Fat")
    fat_intake_uom = fields.Many2one(
        "product.uom", "Fat UoM",
        domain=lambda self: [('category_id', '=',
                              self.env.ref('product.product_uom_categ_kgm').id)
                             ]
    )
    protein_intake = fields.Float("Protein")
    protein_intake_uom = fields.Many2one(
        "product.uom", "Protein UoM",
        domain=lambda self: [('category_id', '=',
                              self.env.ref('product.product_uom_categ_kgm').id)
                             ]
    )
