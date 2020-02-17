import django_filters
from django_filters import CharFilter, DateFilter

from blogs.models import *

class BlogFilter(django_filters.FilterSet):
    title = CharFilter (field_name= 'title', lookup_expr = 'icontains' )
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['image','description','content', 'slug','Date' ]

class EnquiryFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name= 'Date', lookup_expr = 'gte' )
    end_date = DateFilter(field_name= 'Date', lookup_expr = 'lte' )

    class Meta:
        model = Enquiries
        fields = ['Date', 'service']
       