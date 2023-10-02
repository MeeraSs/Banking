from django.db import models
from django.urls import reverse
# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def get_url(self):
        return reverse('banking_app:branches_by_districts',args=[self.slug])

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def get_url(self):
        return reverse('banking_app:branchDistrictDetail', args=[self.District.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def __str__(self):
        return self.name

class Details(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    ACCOUNT_CHOICES =[
        ('savings', 'savings'),
        ('current', 'current'),
    ]
    name = models.CharField(max_length=250, null=False)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField(max_length=100)
    address = models.TextField(max_length=350)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    account = models.CharField(max_length=10, choices=ACCOUNT_CHOICES)
    materials_provide = models.ManyToManyField(Material)
    def __str__(self):
        return self.name

