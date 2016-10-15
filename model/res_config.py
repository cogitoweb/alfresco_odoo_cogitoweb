# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (C) 2004-2012 OpenERP S.A. (<http://openerp.com>).
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

import logging

from openerp import models,fields, api
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class hd_config_settings(models.TransientModel):
    _name = 'alfresco_odoo_mapper.config.settings'
    _inherit = 'res.config.settings'

    default_alfr_mapper_username = fields.Char(
        string='Afresco username',
        required=True,
        help="username afresco account",
        default_model='alfresco_odoo_mapper.config.settings',
        translate=True,
    )
    
    default_alfr_mapper_password = fields.Char(
        string='Afresco password',
        required=True,
        help="password afresco account",
        default_model='alfresco_odoo_mapper.config.settings',
        translate=True,
    )
    
    default_alfr_mapper_public_url = fields.Char(
        string='Afresco public url',
        required=True,
        help="public host",
        default_model='alfresco_odoo_mapper.config.settings',
        translate=True,
    )
    
    default_alfr_mapper_private_url = fields.Char(
        string='Afresco private url',
        required=True,
        help="ip for local access",
        default_model='alfresco_odoo_mapper.config.settings',
        translate=True,
    )
    
    default_alfr_mapper_base_path = fields.Char(
        string='Afresco base path',
        required=True,
        help="base path for doc lib",
        default_model='alfresco_odoo_mapper.config.settings',
        translate=True,
    )
    
    default_alfr_mapper_account_path = fields.Char(
        string='Afresco customer path',
        required=True,
        help="relative customer path",
        default_model='alfresco_odoo_mapper.config.settings',
        translate=True,
    )
    
    default_alfr_mapper_project_path = fields.Char(
        string='Afresco project path',
        required=True,
        help="relative project path under cutomers",
        default_model='alfresco_odoo_mapper.config.settings',
        translate=True,
    )







