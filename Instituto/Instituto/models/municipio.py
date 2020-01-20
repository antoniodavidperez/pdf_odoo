from odoo import models, fields, api

class Municipio(models.Model):
    _name = 'instituto.municipio'
    nombre = fields.Char('Nombre', required = True)
    numeroHabitantes = fields.Integer('Número de habitantes', required = True)
    provincia = fields.Many2one('instituto.provincia', 'Provincia')