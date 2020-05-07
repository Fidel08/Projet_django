from django.db import models

# Create your models here.

class Categorie_Agent(models.Model):
    id_categorie_agent = models.AutoField(primary_key=True)
    libelle_cat_agent=models.CharField('Libéllé',max_length=50)
    creation_time=models.DateTimeField()
    update_time=models.DateTimeField()


class Agent(models.Model):
    id_agent = models.AutoField(primary_key=True)
    code_agent=models.CharField('Code agent',max_length=10,unique=True)
    nom=models.CharField('Nom',max_length=50)
    prenom=models.CharField('Prénom',max_length=50)
    creation_time=models.DateTimeField()
    update_time=models.DateTimeField()
    id_categorie_agent=models.ForeignKey(Categorie_Agent,on_delete=models.CASCADE)

class Type_Activite(models.Model):
    id_type_activite=models.AutoField(primary_key=True)
    libelle_typ_activite=models.CharField('Libéllé',max_length=50)
    creation_time=models.DateTimeField()
    update_time=models.DateTimeField()

class Activite(models.Model):
    id_activite=models.AutoField(primary_key=True)
    libelle_activite=models.CharField('Libéllé',max_length=50)
    id_type_activite=models.ForeignKey(Type_Activite,on_delete=models.CASCADE)
    id_categorie_agent=models.ForeignKey(Categorie_Agent,on_delete=models.CASCADE)
    creation_time=models.DateTimeField()
    update_time=models.DateTimeField()


class Date(models.Model):
    date_key=models.CharField(max_length=10,primary_key=True)
    jour=models.IntegerField()
    semaine=models.IntegerField()
    mois=models.IntegerField()
    trimestre=models.IntegerField()
    semestre=models.IntegerField()
    annee=models.IntegerField()
    creation_time=models.DateTimeField()
    update_time=models.DateTimeField()

class Fact_Prestation(models.Model):
    id_fact_prestation=models.AutoField(primary_key=True)
    id_activite=models.ForeignKey(Activite,on_delete=models.CASCADE)
    date_key=models.ForeignKey(Date,on_delete=models.CASCADE)
    quantile=models.IntegerField()
    creation_time=models.DateTimeField()
    update_time=models.DateTimeField()

class Periodicite(models.Model):
    id_periodicite=models.AutoField(primary_key=True)
    libelle_periodicite=models.CharField(max_length=50)
    dim_date_column_name=models.CharField(max_length=20)
    creation_time=models.DateTimeField()
    update_time=models.DateTimeField()

class Periodes_Reporting(models.Model):
    id_periode_reporting=models.AutoField(primary_key=True)
    id_activite=models.ForeignKey(Activite,on_delete=models.CASCADE)
    id_periodicite=models.ForeignKey(Periodicite,on_delete=models.CASCADE)
    creation_time=models.DateTimeField()
    update_time=models.DateTimeField()