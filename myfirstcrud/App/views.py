from django.shortcuts import render
from App.models import Labo
from App.models import Perso
from App.models import Pat
from django.http import HttpResponseRedirect
from datetime import datetime

#Home
def home(request):
    all_Labo = Labo.objects.all().order_by('id')
    return render(request,'home.html',{"Labos" : all_Labo})

def accueil(request):
    return render(request,'accueil.html')

def persoHome(request):
    all_Perso = Perso.objects.all().order_by('id')
    return render(request,'perso.html',{"Persos" : all_Perso})

def patHome(request):
    all_Pat = Pat.objects.all().order_by('id')
    return render(request,'pat.html',{"Pats" : all_Pat})

#add 
def add_Labo(request):
    if request.method == "POST":
      if request.POST.get('nom') \
         and request.POST.get('employeeMax') \
         and request.POST.get('address') \
         and request.POST.get('ville') \
         and request.POST.get('codepostal') :
         labo = Labo()
         labo.nom = request.POST.get('nom')
         labo.employeeMax = request.POST.get('employeeMax')
         labo.address = request.POST.get('address')
         labo.ville = request.POST.get('ville')
         labo.codepostal = request.POST.get('codepostal')
         labo.tel = request.POST.get('tel')
         labo.email = request.POST.get('email')
         labo.domaine = request.POST.get('domaine')
         labo.dateCreation = request.POST.get('dateCreation')
         
         responsable_id = request.POST.get('responsable')
         if responsable_id != None :
           responsable = Perso.objects.get(id = responsable_id)
           labo.responsable = responsable
          
         labo.save()
         return HttpResponseRedirect('/laboHome')
    else:
         all_Perso = Perso.objects.all().order_by('id')
         return render(request,'add.html',{"Persos" : all_Perso})

def add_Perso(request):
    if request.method == "POST":
      if request.POST.get('nom') \
         and request.POST.get('dateEmb') \
         and request.POST.get('address') \
         and request.POST.get('ville') \
         and request.POST.get('codepostal') :
         perso = Perso()
         perso.nom = request.POST.get('nom')
         perso.address = request.POST.get('address')
         perso.ville = request.POST.get('ville')
         perso.codepostal = request.POST.get('codepostal')
         perso.tel = request.POST.get('tel')
         perso.email = request.POST.get('email')
         perso.dateEmb = request.POST.get('dateEmb')
         perso.fonction = request.POST.get('fonction')
         perso.salaire = request.POST.get('salaire')

         laboratoire_id = request.POST.get('laboratoire')
         if laboratoire_id != None and laboratoire_id != '-1' :
           laboratoire = Labo.objects.get(id = laboratoire_id)
           perso.laboratoire = laboratoire

         perso.save()
         return HttpResponseRedirect('/persoHome')
    else:
         all_Labo = Labo.objects.all().order_by('id')
         return render(request,'addPerso.html',{"Labos" : all_Labo})

def add_Pat(request):
    if request.method == "POST":
      if request.POST.get('nom') \
         and request.POST.get('dateAdm') \
         and request.POST.get('address') \
         and request.POST.get('ville') \
         and request.POST.get('codepostal') :
         pat = Pat()
         pat.nom = request.POST.get('nom')
         pat.address = request.POST.get('address')
         pat.ville = request.POST.get('ville')
         pat.codepostal = request.POST.get('codepostal')
         pat.tel = request.POST.get('tel')
         pat.email = request.POST.get('email')
         pat.dateAdm = request.POST.get('dateAdm')
         pat.sex = request.POST.get('sex')
         pat.dateNai = request.POST.get('dateNai')
         

         laboratoire_id = request.POST.get('laboratoire')
         if laboratoire_id != None and laboratoire_id != '-1' :
           laboratoire = Labo.objects.get(id = laboratoire_id)
           pat.laboratoire = laboratoire

         pat.save()
         return HttpResponseRedirect('/patHome')
    else:
         all_Labo = Labo.objects.all().order_by('id')
         return render(request,'addPat.html',{"Labos" : all_Labo})

# single 

def labo(request, labo_id):
    labo = Labo.objects.get(id=labo_id)
    all_Perso = Perso.objects.all().order_by('id')
    if labo is not None:
        formatted_date = labo.dateCreation.strftime('%Y-%m-%d')
        return render(request, "edit.html", {'labo': labo, 'Persos': all_Perso, 'formatted_date': formatted_date})


def perso(request,perso_id):
    perso = Perso.objects.get(id = perso_id)
    all_Labos = Labo.objects.all().order_by('id')
    if perso is not None:
      formatted_date = perso.dateEmb.strftime('%Y-%m-%d')
      return render(request, "editPerso.html" , {'perso':perso ,'Labos' : all_Labos, 'formatted_date': formatted_date} )

def pat(request,pat_id):
    pat = Pat.objects.get(id = pat_id)
    all_Labos = Labo.objects.all().order_by('id')
    if pat is not None:
      formatted_date = pat.dateAdm.strftime('%Y-%m-%d')
      formatted_date2 = pat.dateNai.strftime('%Y-%m-%d')
      return render(request, "editPat.html" , {'pat':pat ,'Labos' : all_Labos, 'formatted_date': formatted_date, 'formatted_date2': formatted_date2} )


#edit 
def edit_Labo(request):
    if request.method == "POST":
        labo = Labo.objects.get(id = request.POST.get('id'))
        if labo != None :
         labo.nom = request.POST.get('nom')
         labo.employeeMax = request.POST.get('employeeMax')
         labo.address = request.POST.get('address')
         labo.ville = request.POST.get('ville')
         labo.codepostal = request.POST.get('codepostal')
         labo.tel = request.POST.get('tel')
         labo.email = request.POST.get('email')
         labo.domaine = request.POST.get('domaine')
         labo.dateCreation = request.POST.get('dateCreation')
         
         responsable_id = request.POST.get('responsable')
         if responsable_id != None :
           responsable = Perso.objects.get(id = responsable_id)
           labo.responsable = responsable
           
         labo.save()
         return HttpResponseRedirect('/laboHome')

def edit_Perso(request):
    if request.method == "POST":
        perso = Perso.objects.get(id = request.POST.get('id'))
        if perso != None :
         perso.nom = request.POST.get('nom')
         perso.address = request.POST.get('address')
         perso.ville = request.POST.get('ville')
         perso.codepostal = request.POST.get('codepostal')
         perso.tel = request.POST.get('tel')
         perso.email = request.POST.get('email')
         perso.dateEmb = request.POST.get('dateEmb')
         perso.fonction = request.POST.get('fonction')
         perso.salaire = request.POST.get('salaire')

         laboratoire_id = request.POST.get('laboratoire')
         if laboratoire_id != None and laboratoire_id != '-1' :
           laboratoire = Labo.objects.get(id = laboratoire_id)
           perso.laboratoire = laboratoire

         perso.save()
         return HttpResponseRedirect('/persoHome')

def edit_Pat(request):
    if request.method == "POST":
        pat = Pat.objects.get(id = request.POST.get('id'))
        if pat != None :
         pat.nom = request.POST.get('nom')
         pat.address = request.POST.get('address')
         pat.ville = request.POST.get('ville')
         pat.codepostal = request.POST.get('codepostal')
         pat.tel = request.POST.get('tel')
         pat.email = request.POST.get('email')
         pat.dateAdm = request.POST.get('dateAdm')
         pat.sex = request.POST.get('sex')
         pat.dateNai = request.POST.get('dateNai')

         laboratoire_id = request.POST.get('laboratoire')
         if laboratoire_id != None and laboratoire_id != '-1':
           laboratoire = Labo.objects.get(id = laboratoire_id)
           pat.laboratoire = laboratoire

         pat.save()
         return HttpResponseRedirect('/patHome')

# delete labo

def delete_Labo(request , labo_id):
  labo = Labo.objects.get(id = labo_id)
  labo.delete()
  return HttpResponseRedirect('/laboHome')

def delete_Perso(request , perso_id):
  perso = Perso.objects.get(id = perso_id)
  perso.delete()
  return HttpResponseRedirect('/persoHome')

def delete_Pat(request , pat_id):
  pat = Pat.objects.get(id = pat_id)
  pat.delete()
  return HttpResponseRedirect('/patHome')