from policyengine_us.model_api import *


class il_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "IL taxable income"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        return max_(
            0,
            tax_unit("il_base_income", period)
            - tax_unit("il_total_exemptions", period),
        )
