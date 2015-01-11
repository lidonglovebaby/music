from django.contrib import admin

#regist our models to the backend in admin where we can manage it
from musicworld.models import User,UserAdmin,Article,ArticleAdmin,Comment,Periodical,Ptype,Pcomment,Music,Userinformation
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Periodical)
admin.site.register(Ptype)
admin.site.register(Pcomment)
admin.site.register(Music)
admin.site.register(Userinformation)