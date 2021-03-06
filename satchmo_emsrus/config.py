# -*- coding: utf-8 -*-
u"""Админские настройки для EMS-доставки"""

from decimal import Decimal
from django.utils.translation import ugettext_lazy as _
from livesettings import *

SHIP_MODULES = config_get('SHIPPING', 'MODULES')
SHIP_MODULES.add_choice(('satchmo_emsrus', 'EMS Russia'))

SHIPPING_GROUP = ConfigurationGroup('satchmo_emsrus',
    _('EMS Russia Shipping Settings'),
    requires = SHIP_MODULES,
    ordering = 101)

config_register_list(
    StringValue(SHIPPING_GROUP,
        'CITY_FROM',
        description=_("Origin city"),
        help_text=_("City of origin for parcels."),
        default=u""),

    DecimalValue(SHIPPING_GROUP,
        'HANDLING_FEE',
        description=_("Handling Fee"),
        help_text=_("The cost of packaging and taking order to post office"),
        default=Decimal('0.00')),

    DecimalValue(SHIPPING_GROUP,
        'MIN_WEIGHT',
        description=_("Minimal weight"),
        help_text=_("Used if total order weight below this value (kg)"),
        default=Decimal('0.50')),

    DecimalValue(SHIPPING_GROUP,
        'DEFAULT_FEE',
        description=_("Default Fee"),
        help_text=_("Used then fee calculation failed if set"),
        default=Decimal('0.00')),

)
