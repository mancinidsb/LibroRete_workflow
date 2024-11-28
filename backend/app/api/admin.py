from django.contrib import admin
from . import models as mdl

# Register your models here.
admin.site.register(mdl.Usuario)
admin.site.register(mdl.Perfil)
admin.site.register(mdl.Lista)
admin.site.register(mdl.Livro)