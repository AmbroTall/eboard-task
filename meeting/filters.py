import django_filters
from django_filters import CharFilter
from.models import *
from django import forms

class MeetingFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Meeting name')

    class Meta:
        Model = Meeting
        fields = ['name',]

