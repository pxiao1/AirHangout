from django.db import models

class singleFlightRecord(models.Model):
    carrier = models.CharField(max_length=4)
    flight = models.CharField(max_length=6)
    date = models.DateTimeField()
    depCity = models.CharField(max_length=30)
    arrCity = models.CharField(max_length=30)
    distance = models.IntegerField()
    shareCode = models.IntegerField()
    clientsID = models.IntegerField()
    def __unicode__(self):
        return self.carrier+self.flight

class currentData(models.Model):
    record = models.ForeignKey(singleFlightRecord,related_name='currenRecordData')

class client(models.Model):
    name = models.CharField(max_length=50)
    gender = models.BooleanField()
    age = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    milesInTotal = models.IntegerField()
    def __unicode__(self):
        return self.name