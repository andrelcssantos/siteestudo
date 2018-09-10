from django.contrib import admin
from .models import (
    Marca,
    Veiculo,
    Pessoa,
    Parametro,
    MovRotativo,
    Mensalista,
    MovMensalista,
)

#Personalizando grids
class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('id','veiculo','checkin','checkout','valor_hora','horas_total','total','pago')



class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista','dt_pgto','total')

    

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Mensalista)
admin.site.register(Parametro)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(MovMensalista, MovMensalistaAdmin)
# Register your models here.


