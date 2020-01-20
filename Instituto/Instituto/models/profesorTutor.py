from odoo import models, fields, api

class ProfesorTutor(models.Model):
    _name = 'instituto.profesor_tutor'
    dni = fields.Char('DNI', required = True)
    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)
    edad = fields.Integer('Edad', required = True)

    def name_get(self):
        res = []

        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res