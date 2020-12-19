from django.contrib import admin
from .models import Academic_Projects, Business_Works, Templ_Services, Templ_Technologies, User_Login,User_Updates

# Register your models here.

admin.site.register(User_Login)
admin.site.register(User_Updates)
admin.register(Templ_Technologies)
admin.register(Templ_Services)
admin.register(Academic_Projects)
admin.register(Business_Works)



 
