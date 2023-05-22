from django.contrib import admin

# Register your models here.
from .models import User,User_profile,Updates,Blocks,Items,Site,Settings,Language,Themas
# Register your models here.
admin.site.register(User)
admin.site.register(User_profile)
admin.site.register(Updates)
admin.site.register(Blocks)
admin.site.register(Items)
admin.site.register(Site)
admin.site.register(Settings)
admin.site.register(Language)
admin.site.register(Themas)
