{
	'name' : 'Alfresco Odoo Mapper',
	'version' : '1.0',
	'author' : "Cogito srl",
	'website' : 'http://www.cogitoweb.it/',
	'category' : 'Tools',
	'depends' : ['base', 'project'],
	'description' : """Alfresco Odoo Mapper for customers and projects
    
complete the module functionality installing LocalLinks extension for Chrome 
  https://chrome.google.com/webstore/detail/locallinks/jllpkdkcdjndhggodimiphkghogcpida
or Firefox
  https://addons.mozilla.org/en-US/firefox/addon/locallink/

    """,
	'data': [
        	'view/project.xml',
        	'view/res_partner.xml',
        	'view/res_config_view.xml',
    	],
	'installable': True
}
