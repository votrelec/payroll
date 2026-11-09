# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).
from odoo import api, models


class PayrollAccountChildGuard(models.AbstractModel):
    _name = 'payroll.account.child.guard'
    _description = 'Accounted Payroll Child Guard'

    _accounting_parent_field = None
    _accounting_protected_fields = frozenset()

    @api.model_create_multi
    def create(self, values_list):
        self.check_access('create')
        field = self._accounting_parent_field
        parents = [values.get(field, self.env.context.get('default_'+field)) for values in values_list]
        self.env['hr.payslip'].browse([value for value in parents if value])._check_no_accounting_entry()
        return super().create(values_list)

    def write(self, values):
        self.check_access('write')
        if self._accounting_protected_fields.intersection(values):
            parents = self.mapped(self._accounting_parent_field)
            parents |= self.env['hr.payslip'].browse(values.get(self._accounting_parent_field))
            parents._check_no_accounting_entry()
        return super().write(values)

    def unlink(self):
        self.check_access('unlink')
        self.mapped(self._accounting_parent_field)._check_no_accounting_entry()
        return super().unlink()


class PayrollInput(models.Model):
    _name = 'hr.payslip.input'
    _inherit = ['hr.payslip.input', 'payroll.account.child.guard']
    _accounting_parent_field = 'payslip_id'
    _accounting_protected_fields = frozenset(('payslip_id', 'contract_id', 'code', 'amount'))


class PayrollWorkedDays(models.Model):
    _name = 'hr.payslip.worked_days'
    _inherit = ['hr.payslip.worked_days', 'payroll.account.child.guard']
    _accounting_parent_field = 'payslip_id'
    _accounting_protected_fields = frozenset(('payslip_id', 'contract_id', 'code', 'number_of_days', 'number_of_hours'))
