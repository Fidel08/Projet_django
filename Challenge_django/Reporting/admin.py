from django.contrib import admin
from .models import Categorie_Agent, Agent, Type_Activite, Activite, Fact_Prestation, Periodicite, Periodes_Reporting, Date
#from import_export.admin import ImportExportModelAdmin
# Register your models here


# création de la ressource d'import export
from import_export import resources
class AgentResource(resources.ModelResource):
    class Meta:
        model = Agent
        import_id_fields = ('id_agent',)
		
# Intégration dans l'espace d'administration de django
from import_export.admin import ImportExportModelAdmin
class AgentAdmin(ImportExportModelAdmin):
    resource_class = AgentResource

admin.site.register(Agent, AgentAdmin)

admin.site.register(Categorie_Agent)
admin.site.register(Agent)
admin.site.register(Type_Activite)
admin.site.register(Activite)
admin.site.register(Fact_Prestation)
admin.site.register(Periodicite)
admin.site.register(Periodes_Reporting)
admin.site.register(Date)