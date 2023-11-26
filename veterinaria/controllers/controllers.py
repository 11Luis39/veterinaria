# -*- coding: utf-8 -*-
# from odoo import http


# class Veterinaria(http.Controller):
#     @http.route('/veterinaria/veterinaria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/veterinaria/veterinaria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('veterinaria.listing', {
#             'root': '/veterinaria/veterinaria',
#             'objects': http.request.env['veterinaria.veterinaria'].search([]),
#         })

#     @http.route('/veterinaria/veterinaria/objects/<model("veterinaria.veterinaria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('veterinaria.object', {
#             'object': obj
#         })
