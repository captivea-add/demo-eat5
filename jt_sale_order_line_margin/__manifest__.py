# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-Today Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
	'name': 'Sale Order Line Margin',
	'summary': 'Sale Order Line Margin',
	'version': '15.0.1.0',
	'category': 'Sale',
	'author': 'Jupical Technologies Pvt. Ltd.',
	'maintainer': 'Jupical Technologies Pvt. Ltd.',
	'website': 'http://www.jupical.com',
	'depends': ['sale_margin'],
	'data': [
		'views/sale_order_line_margin.xml',
	],
        'license': 'AGPL-3',
	'application': True,
	'installable': True,
	'auto_install': False,   
        'images': ['static/description/poster_image.png'],
}
