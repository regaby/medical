# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
{
    "name": "Create user from partner",
    "author": "Gabriela Rivero",
    "category": "Medical",
    "description": """
This module allows create a user from doctor (partner)
    """,
    "version": "1.0",
    "depends": [
        "medical",
        ],
    
    "init_xml": [],
    'data': [
	'wizard/create_user_from_partner_view.xml'        
    ],
    'demo_xml': [],
    'images': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}
