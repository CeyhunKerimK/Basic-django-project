from django.contrib import admin

from .models import Movie

  

# Register your models here.

  

class MovieAdmin(admin.ModelAdmin):

    list_display = ('id','name','created_date','IsPublished','duration')
    list_display_links = ('id','name')
    list_filter = ('created_date','movie_type')
    list_editable = ('IsPublished',)
    search_fiels = ('name','description','movie_type')

admin.site.register(Movie,MovieAdmin)