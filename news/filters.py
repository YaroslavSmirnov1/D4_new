from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Post, Author
import django.forms

# создаём фильтр
class PostFilter(FilterSet):
       time_created = DateFilter(field_name='dateCreation',
                                 lookup_expr='gt',
                                 label='Created after',
                                 widget=django.forms.DateInput(attrs={'type': 'date'}))
       title = CharFilter(lookup_expr='icontains')
       author = ModelChoiceFilter(queryset=Author.objects.all())
       time_created.field.error_messages = {'invalid': 'Enter date in the following format DD.MM.YYYY. Example: 31.12.2020'}
       time_created.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}

       class Meta:
           model = Post
           fields = ['time_created', 'title', 'categoryType']
