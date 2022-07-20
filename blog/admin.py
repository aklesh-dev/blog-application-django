from django.contrib import admin
from .models import Post, Comments

# Register your models here.
# admin.site.register(Post)

# Telling the Django adminstration site that model is registered in the site using custom class that
# inherites from Model.Admin.
# In this class we can include information about how to display the model in the site and how to interact with it.
# @admin.register() decorator perform the same function as the admin.site.register() function
# registering the ModelAdmin class that it decorates.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display attribute allows us to set the fields of the models that will display on the administration object list page.
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # list page includes a right sidebar,
    # that allows you to filter the results by the fields included in the list_filter attribute
    list_filter = ('status', 'create', 'publish', 'author')
    # A search bar appeared on the page, 
    # Defined a list of searchable fields using the search_fields attribute.
    search_fields = ('title', 'body') 
    # As we type the title of a new post, the slug field is filled in automatically.
    # Django will prepopulate the slug field with the input of the title field using the prepopulated_fields attribute
    prepopulated_fields = {'slug':('title',)}
    # The author field will display with a lookup widget that can scale much
    # better than a drop-down select input when you have thousands of users.
    # This is achieved with the raw_id_fields attribute.
    raw_id_fields = ('author',)
    # Below searchbar, there are navigation links to navigate through a date hierarchy;
    # this has been define by the date_hierarchy attribute
    date_hierarchy = 'publish'
    # The posts are ordered by STATUS and PUBLISH coulmns by default.
    # We have specified the default sorting criteria using the ordering attribute.
    ordering = ('status', 'publish')

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ( 'created', 'active', 'update')
    search_fields = ( 'name', 'email', 'body')