from odoo import models, fields, api

class TutorLegal(models.Model):
    _name = 'instituto.tutor_legal'
    dni = fields.Char('DNI', required = True)
    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)

    def name_get(self):
        res = []

        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res