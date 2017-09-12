from django.contrib import admin
from .models import Article, User, Catecory, Admin, Visiteur, Author
# Register your models here.


admin.site.register(Article)
admin.site.register(Catecory)
admin.site.register(Admin)
admin.site.register(Author)
admin.site.register(Visiteur)