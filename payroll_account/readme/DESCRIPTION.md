Generic Payroll system Integrated with Accounting.

This module is a backport from Odoo SA and as such, it is not included
in the OCA CLA. That means we do not have a copy of the copyright on it
like all other OCA modules.

An existing accounting entry prevents a direct reset or recalculation of the
payslip. Use the payroll cancellation or correction workflow first so salary
lines cannot silently diverge from the journal entry. Payslips without an
accounting entry can still be reset and calculated normally.

Accounted salary lines, worked time and inputs cannot be added, removed,
reassigned or financially changed independently of their journal entry.
Payroll identity, state and the accounting link follow the same check.
Descriptions remain editable, and draft calculation, cancellation and the
native refund workflow remain available.
