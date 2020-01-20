from odoo import models, fields, api

class ComunidadAutonoma(models.Model):
    _name = 'instituto.comunidad_autonoma'
    nombre = fields.Char('Nombre', required = True)
    numeroHabitantes = fields.Integer('Número de habitantes', required = True)

    def name_get(self):
        res = []

        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res