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
import urllib
import re

from openerp import api, SUPERUSER_ID
from openerp.tools.config import config
from openerp.tools.translate import _
from openerp.exceptions import Warning
from openerp.http import request

from werkzeug.useragents import UserAgent

_logger = logging.getLogger(__name__)
_alfr_result_obj = None

###
### retrieve config settings
###
def retrieve_config_settings(s):

    #    <field name="default_alfr_mapper_username" />
    #    <field name="default_alfr_mapper_password" />
    #    <field name="default_alfr_mapper_public_url" />
    #    <field name="default_alfr_mapper_private_url" />
    #    <field name="default_alfr_mapper_base_path" />
    #    <field name="default_alfr_mapper_base_fs_path" />
    #    <field name="default_alfr_mapper_account_path" />
    #    <field name="default_alfr_mapper_project_path" />

    if(s._alfr_result_obj):
        return s._alfr_result_obj

    ## SUPERUSER_ID instead of _s._uid
    _ids = s.pool.get('alfresco_odoo_mapper.config.settings').search(s._cr, SUPERUSER_ID, [], order='id desc', limit=1)
    if(len(_ids) < 1):
        raise Warning(_('Alfresco options not configured'))

    s._alfr_result_obj = s.pool.get('alfresco_odoo_mapper.config.settings').browse(s._cr, SUPERUSER_ID, _ids[0])
    return s._alfr_result_obj

def is_private_network(s):

    _hostpart = request.httprequest.environ['HTTP_HOST'].split('.')[0]
    return _hostpart.isdigit()

def normalize_path(s):
    # no slash, then clean 
    
    _f = s.replace('/', '_')
    _keep = ('_', '-', ' '); 
    
    return "".join(c for c in _f if c.isalnum() or c in _keep).rstrip()

def map_to_path(url):
    
    mapped = url.replace('file://','//')
    ua = UserAgent(request.httprequest.environ['HTTP_USER_AGENT'])
    
    _logger.info('UA ' + ua.platform)
    
    if(ua.platform == 'windows'):
        return mapped.replace('/','\\')
    
    return mapped
        



