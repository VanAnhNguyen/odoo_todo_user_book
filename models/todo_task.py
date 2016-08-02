from openerp import models, fields, api

class TodoTask(models.Model):
    _inherit = 'todo.task'
    user_id = fields.Many2one('res.users', 'User_id')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="What needs to be done?")

    @api.one
    def do_toggle_done(self,):
        return super(TodoTask, self).do_toggle_done()

    @api.multi
    def do_clear_done(self,context):
        domain = [('is_done', '=', True),
                    '|', ('user_id', '=', self.env.uid),('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': context['cond']})
        return True