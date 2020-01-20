from odoo import models, fields, api

class Provincia(models.Model):
    _name = 'instituto.provincia'
    nombre = fields.Char('Nombre', required = True)
    numeroHabitantes = fields.Integer('Número de habitantes', required = True)
    comunidadAutonoma = fields.Many2one('instituto.comunidad_autonoma', 'Comunidad autónoma')

    def name_get(self):
        res = []

        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res