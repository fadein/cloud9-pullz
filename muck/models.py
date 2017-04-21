from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    last = models.CharField(max_length=30)
    first = models.CharField(max_length=15)
    middle = models.CharField(max_length=15)
    JR = 'Jr'
    SR = 'Sr'
    III = 'III'
    MD = "MD"
    PHD = "PhD"
    ESQ = "Esq"
    NOPE = ""

    SUFFIXES = (
                (NOPE, "-No Suffix-"),
                (JR, 'Junior'),
                (SR, "Senior"),
                (III, "The Third"),
                (MD, "Medical Doctor"),
                (PHD, "Doctor of Philosophy"),
                (ESQ, "Esquire"),
            )
    suffix = models.CharField(max_length=2, choices=SUFFIXES, default=NOPE )
    dob = models.DateField()

class IDTyp(models.Model):
    """Fixed table of acceptable types of identification"""
    abbr = models.CharField('ID abbreviation', max_length = 3)
    desc = models.CharField('ID type description', max_length = 30)

class IDNum(models.Model):
    """ID record affixed to a person"""
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    idtype = models.ForeignKey(IDTyp, on_delete=models.CASCADE)
    number = models.CharField('ID number', max_length=40)
    issued = models.DateField('ID number issue date')

class Skill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    desc   = models.CharField('Skill description', max_length=50)
