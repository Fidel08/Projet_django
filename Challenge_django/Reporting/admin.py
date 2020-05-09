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
		
# Intégration simultanée dans l'espace d'administration de django de reversion et import-export
from import_export.admin import ImportExportModelAdmin
from reversion.admin import VersionAdmin
class AgentAdmin(ImportExportModelAdmin,VersionAdmin):
    resource_class = AgentResource
admin.site.register(Agent, AgentAdmin)

# Intégration du model Categorie_Agent

class Categorie_AgentResource(resources.ModelResource):
    class Meta:
        model = Categorie_Agent
        import_id_fields = ('id_categorie_agent',)

class Categorie_AgentAdmin(ImportExportModelAdmin,VersionAdmin):
    resource_class = Categorie_AgentResource
admin.site.register(Categorie_Agent, Categorie_AgentAdmin)

# Intégration du model Type_Activite

class Type_ActiviteResource(resources.ModelResource):
    class Meta:
        model = Type_Activite
        import_id_fields = ('id_type_activite',)

class Type_ActiviteAdmin(ImportExportModelAdmin,VersionAdmin):
    resource_class = Type_ActiviteResource
admin.site.register(Type_Activite, Type_ActiviteAdmin)

# Intégration du model Activite

class ActiviteResource(resources.ModelResource):
    class Meta:
        model = Activite
        import_id_fields = ('id_activite',)

class ActiviteAdmin(ImportExportModelAdmin,VersionAdmin):
    resource_class = ActiviteResource
admin.site.register(Activite, ActiviteAdmin)

# Intégration du model Fact_Prestation

class Fact_PrestationResource(resources.ModelResource):
    class Meta:
        model = Fact_Prestation
        import_id_fields = ('id_fact_prestation',)

class Fact_PrestationAdmin(ImportExportModelAdmin,VersionAdmin):
    resource_class = Fact_Prestation
admin.site.register(Fact_Prestation, Fact_PrestationAdmin)

# Intégration du model Periodicite

class PeriodiciteResource(resources.ModelResource):
    class Meta:
        model = Periodicite
        import_id_fields = ('id_periodicite',)

class PeriodiciteAdmin(ImportExportModelAdmin,VersionAdmin):
    resource_class = Periodicite
admin.site.register(Periodicite, PeriodiciteAdmin)

# Intégration du model Periodes_Reporting

class Periodes_ReportingResource(resources.ModelResource):
    class Meta:
        model = Periodes_Reporting
        import_id_fields = ('id_periode_reporting',)

class Periodes_ReportingAdmin(ImportExportModelAdmin,VersionAdmin):
    resource_class = Periodes_Reporting
admin.site.register(Periodes_Reporting, Periodes_ReportingAdmin)

# Intégration du model Date

class DateResource(resources.ModelResource):
    class Meta:
        model = Date
        import_id_fields = ('date_key',)

class DateAdmin(ImportExportModelAdmin,VersionAdmin):
    resource_class = Date
admin.site.register(Date, DateAdmin)

