from django.db import models

class Labo (models.Model):

    id = models.AutoField(primary_key = True)
    employeeMax = models.IntegerField()
    nom = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    ville = models.CharField(max_length=20)
    codepostal = models.CharField(max_length=10)
    tel = models.CharField(max_length=17)
    email = models.EmailField(max_length=40,default = "_")
    domaine = models.CharField(max_length = 40, default ="_")
    dateCreation = models.DateField(default = "1999-12-31")
    responsable = models.ForeignKey('Perso', on_delete=models.SET_NULL,null = True)

    def __str__(self):
        return self.nom

class Perso (models.Model):
  
   id = models.AutoField(primary_key = True)
   nom = models.CharField(max_length=40)
   address = models.CharField(max_length=100)
   ville = models.CharField(max_length=20)
   codepostal = models.CharField(max_length=10)
   tel = models.CharField(max_length=17)
   email = models.EmailField(max_length=40,default = "_")
   dateEmb = models.DateField(default = "1999-12-31")
   fonction = models.CharField(max_length=30 , null = True)
   salaire = models.FloatField(max_length=30 , null = True)
   laboratoire = models.ForeignKey('Labo', on_delete=models.SET_NULL,null = True)

   def __str__(self):
        return self.nom


class Pat (models.Model):
  
   id = models.AutoField(primary_key = True)
   nom = models.CharField(max_length=40)
   address = models.CharField(max_length=100)
   ville = models.CharField(max_length=20)
   codepostal = models.CharField(max_length=10)
   tel = models.CharField(max_length=17)
   email = models.EmailField(max_length=40,default = "_")
   dateAdm = models.DateField(default = "1999-12-31")
   dateNai = models.DateField(default = "1999-12-31")
   sex = models.CharField(max_length=10 , null = True)
   laboratoire = models.ForeignKey('Labo', on_delete=models.SET_NULL,null = True)

   def __str__(self):
        return self.nom