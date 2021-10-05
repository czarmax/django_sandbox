from django_filters.views import FilterView
from django_filters import FilterSet
from django_tables2.views import SingleTableMixin  # ???
from django_tables2 import tables
from .models import Customer


class CustomersTable(tables.Table):
    class Meta:
        model = Customer


class CustomerFilter(FilterSet):
    class Meta:
        model = Customer
        fields = {"name": ["exact", "contains"], "surname": ["exact", "contains"]}


