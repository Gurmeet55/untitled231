from django.contrib import admin

# Register your models here.



from myapp.models import tb_registration
from myapp.models import tb_emp


admin.site.register(tb_registration)
admin.site.register(tb_emp)
