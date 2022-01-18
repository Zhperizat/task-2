from django.contrib import admin
from service.models import Category, Books, Comment
# Register your models here.
admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Comment)
