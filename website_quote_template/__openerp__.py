# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2016 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Website Quotation Template',
    'version': '0.3',
    'category': 'Tools',
    'summary': 'Additional quote templates',
    'licence': 'AGPL-3',
    'description': """
Additional quotation templates with sepation of monthly costs and one time prices
""",
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['crm', 'website_quote', 'website_quote_multiple_templates'],
    'data': [
    #~ 'website_quote_table.xml',
    'website_quote_template.xml',
    'website_quote_data.xml',
    'product_view.xml',
    'sale_view.xml',
    ],
    'application': False,
    'installable': True,
    'demo': [],
}
# vim:expandtab:smartindent:tabstop=4s:softtabstop=4:shiftwidth=4:
