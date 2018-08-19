from django.contrib import admin
from .models import Genre,Language,Author,Book,BookInstance

# Register your models here.

admin.site.register(Genre)
admin.site.register(Language)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth','date_of_death')
    fields = ('first_name','last_name',('date_of_birth','date_of_death'))

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = (BookInstanceInline,)

    def display_genre(self,obj):
        return ', '.join([genre.name for genre in obj.genre.all()[:3] ])
    
    display_genre.short_description = 'Genre'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status','due_back')
    fieldsets = (
        (None,{
            'fields':('book','imprint')
        }),
        ('Availability',{
            'fields':('status','due_back'),
        })
    )
