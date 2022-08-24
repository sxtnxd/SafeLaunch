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
    Contact = models.ForeignKey(ProviderContact, null=True, blank=True, on_delete=models.CASCADE)
    Group = models.ForeignKey(ProviderGroup, null=True, blank=True,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"
        
    def __str__(self):
        return self.Name
#------------------------------------Projeto---------------------------------
class Product(models.Model):
    Product = models.CharField(max_length=30, unique=True)
    Description = models.CharField(max_length=280)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
    def __str__(self):
        return self.Product
        
    
class Project_Especification(models.Model):
    Diameter  = models.CharField(max_length=10, unique=True)
    Length = models.CharField(max_length=10, unique=True)
    
    class Meta:
        verbose_name = "Project Especification"
        verbose_name_plural = "Projects Especifications"
        
    def __str__(self):
        return self.Diameter
    
class Project_Data(models.Model):
    especification = models.ForeignKey(Project_Especification, null=True, blank=True, on_delete=models.CASCADE)
    systemDate = models.DateField(null=True, blank=True)
    ProductionDate = models.DateField(null=True, blank=True)
    BatchTracking = models.CharField(max_length=60, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=None)
    class Meta:
        verbose_name = "Project Data"
        verbose_name_plural = "Projects Data"
    
    def __str__(self):
        return self.BatchTracking
    
class Project(models.Model):
    Project = models.CharField(max_length=30, unique=True)
    Provider = models.ForeignKey(Provider, null=True, blank=True, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    Data = models.ForeignKey(Project_Data, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        
    def __str__(self):
        return self.Project
    
#----------------------------------------------------Collaborator--------------------------------------------    
role_options = [('ADM', 'Admin'), ('DEV','Developer'),('CMM','Comum')]

class Role(models.Model):
    Role = models.CharField(max_length=3, choices=role_options, default='CLR')
    
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        
    def __str__(self):
        return self.Role 
    
class Collaborator(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    EDV = models.CharField(max_length=10, unique=True)
    Email = models.EmailField()
    Role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)
    Username = models.CharField(max_length=10, blank=True)
    class Meta:
        verbose_name = "Collaborator"
        verbose_name_plural = "Collaborators"
        
    def __str__(self):
        return self.FirstName + " " + self.LastName
#----------------------------------------------------ACCESS--------------------------------------------
