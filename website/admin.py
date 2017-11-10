from django.contrib import admin
from .models import Article, Person
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	"""docstring for ArticleAdmin"""
	list_display = ('title','pub_date','update_time',)
		
class PersonAdmin(admin.ModelAdmin):
	"""docstring for PersonAdmin"""
	list_display = ('full_name',)
		
admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)