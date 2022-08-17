from contextlib import ContextDecorator
from tabnanny import verbose
from django.db import models

# ----------------------------FORNECEDORES---------------------------
class ProviderGroup(models.Model):
    Group = models.CharField(max_length=30)
    Country = models.CharField(max_length=40)
    Abbreviation = models.CharField(max_length=15)
    
    class Meta:
        verbose_name = "Provider Group"
        verbose_name_plural = "Providers Groups"
        
        def __str__(self):
            return self.Group
        
class ProviderContact(models.Model):
    PrimaryEmail = models.EmailField()
    SecondaryEmail = models.EmailField()
    PrimaryPhone = models.CharField(max_length=16)
    SecondaryPhone = models.CharField(max_length=16)
    
    class Meta:
        verbose_name = "Provider Group"
        verbose_name_plural = "Providers Groups"
        
        def __str__(self):
            return self.PrimaryEmail
        
class Provider(models.Model):
    Name = models.CharField(max_length=255, unique=True)
    CNPJ = models.CharField(max_length=20)
    Initials = models.CharField(max_length=15)
    Contact = models.ForeignKey(ProviderContact, null=True, blank=True)
    Group = models.ForeignKey(ProviderGroup, null=True, blank=True)
#------------------------------------Projeto---------------------------------