from django.db import models

# Create your models here.

class Utente(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    S_Level = models.IntegerField()

    def __str__(self):
        return self.username + " " + self.password + " " + self.S_Level

class Testata(models.Model):
    codice = models.IntegerField()
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=20)
    giorno_uscita = models.CharField(max_length=15)
    cod_giorno = models.IntegerField()

    def __str__(self):
        return self.sigla + " " + self.nome

class Vendita(models.Model):
    anno = models.IntegerField()
    N_settimana = models.IntegerField()
    data_uscita = models.DateField(auto_now=False, auto_now_add=False)
    V_attuale = models.IntegerField()
    V_precedente = models.IntegerField()
    V_anno_prec = models.IntegerField()
    giornale = models.ForeignKey(Testata, on_delete=models.CASCADE, related_name="vendite")

    def __str__(self):
        return "vendita copie anno " + self.anno 


#https://stackoverflow.com/questions/50970188/did-you-install-mysqlclient/54200666