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

    def __str__(self):
        return "%s %s %s %s" % (self.first, self.middle, self.last, self.suffix)

class IDTyp(models.Model):
    """Fixed table of acceptable types of identification"""
    abbr = models.CharField('ID abbreviation', max_length = 3)
    desc = models.CharField('ID type description', max_length = 30)

    def __str__(self):
        return "%s = %s" % (self.abbr, self.desc)

class IDNum(models.Model):
    """ID record affixed to a person"""
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    idtype = models.ForeignKey(IDTyp, on_delete=models.CASCADE)
    number = models.CharField('ID number', max_length=40)
    issued = models.DateField('ID number issue date')

    def __str__(self):
        return "%s = %s" % (self.idtype, self.issued)

class Skill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    desc   = models.CharField('Skill description', max_length=50)

    def __str__(self):
        return "%s = %s" % (self.person, self.desc)

class ContactTyp(models.Model):
    """Fixed table of acceptable means of contact"""
    abbr = models.CharField('Contact abbreviation', max_length = 5)
    desc = models.CharField('Contact description', max_length=50)

    def __str__(self):
        return "%s = %s" % (self.abbr, self.desc)

class Contact(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    contyp = models.ForeignKey(ContactTyp, on_delete=models.CASCADE)
    detail = models.CharField('Contact detail', max_length=50)

    def __str__(self):
        return "(%s) %s = %s" % (self.person, self.contyp, self.detail)

