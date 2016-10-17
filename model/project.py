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

from ..lib import utils

_logger = logging.getLogger(__name__)


class alfresco_odoo_mapper_project(models.Model):
    _inherit = 'project.project'
    
    _alfr_result_obj = None

         
    @api.multi
    def popup_alfresco_fileexplorer(self):
        
        self._alfr_result_obj = utils.retrieve_config_settings(self)
        
        fileurl = re.sub('^(https?)://', 'file://', self._alfr_result_obj.default_alfr_mapper_private_url)
        
        fileurl += '/' + self._alfr_result_obj.default_alfr_mapper_base_fs_path
        fileurl += '/' + self._alfr_result_obj.default_alfr_mapper_account_path
        fileurl += '/' + utils.normalize_path(self.partner_id.name)
        fileurl += '/' + self._alfr_result_obj.default_alfr_mapper_project_path
        fileurl += '/' + utils.normalize_path(self.name)
        
        path = utils.map_to_path(fileurl)
        
        raise Warning(_('Open file explorer with path %s') % path)

        ## no way
        return {
            'type': 'ir.actions.act_url',
            'url': fileurl,
            'nodestroy': True,
            'target': 'new' 
            }
    
    @api.multi
    def popup_alfresco_web(self):
        
        self._alfr_result_obj = utils.retrieve_config_settings(self)
        
        rel_url = 'path|/' + self._alfr_result_obj.default_alfr_mapper_account_path
        rel_url += '/' + utils.normalize_path(self.partner_id.name)
        rel_url += '/' + self._alfr_result_obj.default_alfr_mapper_project_path + '/' + utils.normalize_path(self.name)
        url = self._alfr_result_obj.default_alfr_mapper_private_url if utils.is_private_network(self) else self._alfr_result_obj.default_alfr_mapper_public_url
        
        url += '/' + self._alfr_result_obj.default_alfr_mapper_base_path
        url += '#filter=' + urllib.quote_plus(rel_url);
        
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'nodestroy': True,
            'target': 'new' 
            }
    
    





