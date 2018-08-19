from django.contrib import admin
from .models import Genre,Language,Author,Book,BookInstance
from django.http import HttpResponse
from django.core import serializers
# Register your models here.

admin.site.register(Genre)
admin.site.register(Language)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth','date_of_death')
    search_fields = ('first_name','last_name')
    fields = ('first_name','last_name',('date_of_birth','date_of_death'))
    

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

def export_as_json(modeladmin,request,queryset):
    
    response = HttpResponse(content_type='application/json')
    serializers.serialize('json',queryset,stream=response)
    return response

export_as_json.short_description = 'Export selected  as json request'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    search_fields = ('title',)
    inlines = (BookInstanceInline,)
    ordering = ('-title',)
    filter_horizontal = ('genre','language')
    actions = (export_as_json,)

    def display_genre(self,obj):
        return ', '.join([genre.name for genre in obj.genre.all()[:3] ])
    
    display_genre.short_description = 'Genre'

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','due_back','status')
    list_filter = ('status','due_back')
    date_hierarchy =  'due_back'
    fieldsets = (
        (None,{
            'fields':('book','imprint')
        }),
        ('Availability',{
            'fields':('status','due_back'),
        })
    )
