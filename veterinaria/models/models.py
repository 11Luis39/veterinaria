# -*- coding: utf-8 -*-

from odoo import models, fields, api
from urllib.parse import quote

class mascota(models.Model):
    _name = 'veterinaria.mascota'
    _description = 'mascota'

    name = fields.Char(string='name', required=True)
    edad = fields.Char(string='edad', required=True)
    color = fields.Char(string='color', required=True)
    type = fields.Selection([
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('otros', 'Otros')
    ], string='type', default="perro", required=True)



    partner_id = fields.Many2one(
        'res.partner',          # Relacionado con el modelo de cliente
        string='Dueño'
    )

    cartilla_ids = fields.One2many(
        'veterinaria.cartilla',  # Modelo relacionado
        'mascota_id',           # Campo inverso en el modelo cartilla
        string='Cartillas'
    )

    evento_ids = fields.One2many(
        'calendar.event',
        'mascota_id',  # Asegúrate de que este campo existe en 'calendar.event'
        string='Eventos Relacionados'
    )
    
    

class ResPartner(models.Model):
    _inherit = 'res.partner'

    mascota_ids = fields.One2many(
        'veterinaria.mascota',  # Nombre del modelo de mascota
        'partner_id',           # Campo inverso en el modelo de mascota
        string='Mascotas'
    )



class cartilla(models.Model):
    _name = 'veterinaria.cartilla'
    _description = 'cartilla'

    fecha = fields.Date(string='Fecha', required=True)
    notas = fields.Text(string='Notas')

    producto_tmpl_id = fields.Many2one(
        'product.template',
        string='Producto',
        help='Producto utilizado en esta cartilla (ej. vacuna, medicamento)'
    )

    mascota_id = fields.Many2one('veterinaria.mascota', string='Mascota', required=True)
    #nombre_mascota = fields.Char(string='Nombre de Mascota', related='mascota_id.name', readonly=True)

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    whatsapp_url = fields.Char(compute='_compute_whatsapp_url')

    mascota_id = fields.Many2one(
        'veterinaria.mascota',
        string='Mascota Relacionada'
    )
    dueno_telefono = fields.Char(string="Teléfono del Dueño", related="mascota_id.partner_id.phone", readonly=True)

    def _compute_whatsapp_url(self):
        base_url = "https://web.whatsapp.com/send?phone="
        for record in self:
            phone_number = record.dueno_telefono  # Utiliza el teléfono del dueño de la mascota
            if phone_number:
                message = "Recordatorio: {} , Tu proxima consulta es el dia {}".format(record.name, record.start.strftime("%Y-%m-%d %H:%M"))
                encoded_message = quote(message)
                record.whatsapp_url = "{}{}&text={}".format(base_url, phone_number, encoded_message)
            else:
                # Si no hay número de teléfono, deja la URL en blanco
                record.whatsapp_url = "no hay url"
