from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'instituto.alumno'
    numeroMatricula = fields.Integer('Numero de matrícula', required = True)
    nombre = fields.Char('Nombre', required = True)
    apellidos = fields.Char('Apellidos', required = True)
    edad = fields.Integer('Edad', required = True)
    curso = fields.Char('Curso', required = True)
    dNIProfesorTutor = fields.Many2one('instituto.profesor_tutor', 'DNI profesor tutor')
    dNITutorLegal = fields.Many2one('instituto.tutor_legal', 'DNI tutor legal')