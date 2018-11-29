from django.contrib import admin

from money.models import Money
from stock.models import Clothes

admin.site.register(Money)
admin.site.register(Clothes)