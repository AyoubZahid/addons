# -*- coding: utf-8 -*-
from odoo import http

# class DarkTheme(http.Controller):
#     @http.route('/dark_theme/dark_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dark_theme/dark_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dark_theme.listing', {
#             'root': '/dark_theme/dark_theme',
#             'objects': http.request.env['dark_theme.dark_theme'].search([]),
#         })

#     @http.route('/dark_theme/dark_theme/objects/<model("dark_theme.dark_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dark_theme.object', {
#             'object': obj
#         })