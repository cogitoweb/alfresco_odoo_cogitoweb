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

from openerp import models,fields, api
from openerp.tools.config import config
from openerp.tools.translate import _
from openerp.exceptions import Warning
from openerp.http import request

_logger = logging.getLogger(__name__)


class alfresco_odoo_mapper_res_partner(models.Model):
    _inherit = 'res.partner'
    
    _alfr_result_obj = None

    ###
    ### retrieve config settings
    ###
    def _retrieve_config_settings(self):
        
        #    <field name="default_alfr_mapper_username" />
        #    <field name="default_alfr_mapper_password" />
        #    <field name="default_alfr_mapper_public_url" />
        #    <field name="default_alfr_mapper_private_url" />
        #    <field name="default_alfr_mapper_base_path" />
        #    <field name="default_alfr_mapper_account_path" />
        #    <field name="default_alfr_mapper_project_path" />
        
        if(self._alfr_result_obj):
            return self._alfr_result_obj
        
        _ids = self.pool.get('alfresco_odoo_mapper.config.settings').search(self._cr, self._uid, [], order='id desc', limit=1)
        if(len(_ids) < 1):
            raise Warning(_('Alfresco options not configured'))
            
        self._alfr_result_obj = self.pool.get('alfresco_odoo_mapper.config.settings').browse(self._cr, self._uid, _ids[0])
        return self._alfr_result_obj
    
    def _is_private_network(self):
        
        _hostpart = request.httprequest.environ['HTTP_HOST'].split('.')[0]
        return _hostpart.isdigit()

         
    @api.multi
    def popup_alfresco_fileexplorer(self):
        
        self._retrieve_config_settings()
        
        fileurl = re.sub('^(https?)://', 'file://', self._alfr_result_obj.default_alfr_mapper_private_url)
        
        fileurl += '/' + self._alfr_result_obj.default_alfr_mapper_base_path
        fileurl += '/' + self._alfr_result_obj.default_alfr_mapper_account_path
        fileurl += '/' + self.name 

        return {
            'type': 'ir.actions.act_url',
            'url': fileurl,
            'nodestroy': True,
            'target': 'new' 
            }
    
    @api.multi
    def popup_alfresco_web(self):
        
        self._retrieve_config_settings()
        
        rel_url = 'path|/' + self._alfr_result_obj.default_alfr_mapper_account_path + '/' + self.name       
        url = self._alfr_result_obj.default_alfr_mapper_private_url if self._is_private_network() else self._alfr_result_obj.default_alfr_mapper_public_url
        
        url += '/' + self._alfr_result_obj.default_alfr_mapper_base_path
        url += '#filter=' + urllib.quote_plus(rel_url);
        
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'nodestroy': True,
            'target': 'new' 
            }
    
    





