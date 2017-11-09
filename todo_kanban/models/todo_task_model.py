from odoo import models, fields, api


class TodoTask(models.Model):
    _inherit = 'todo.task'
    color = fields.Integer('Color Index')
    priority = fields.Selection(
            [('0', 'Low'),
             ('1', 'Normal'),
             ('2', 'High')],
            'Priority', default="1"
            )
    kanban_state = fields.Selection(
            [('normal', 'In Progress'),
             ('blocked', 'Blocked'),
             ('done', 'Read for next stage')],
            'Kanban State', default='normal'
            )
