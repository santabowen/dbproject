import datetime

from django.db import models
from django.utils import timezone


class Population(models.Model):
    state = models.CharField(max_length=3)
    year = models.IntegerField(default=2010)
    age0_5 = models.IntegerField(default=0)
    age6_17 = models.IntegerField(default=0)
    age18_64 = models.IntegerField(default=0)
    age65 = models.IntegerField(default=0)
    agetotal = models.IntegerField(default=0)

    def __str__(self):
        return self.state
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Population._meta.fields]

class StateCode(models.Model):
    state_name = models.CharField(max_length=30)
    alpha_code = models.CharField(max_length=3)
    numeric_code = models.CharField(max_length=3)
    def __str__(self):
        return self.state_name

class Sex(models.Model):
    state = models.CharField(max_length=3)
    year = models.IntegerField(default=2010)
    male = models.FloatField(default=0)
    female = models.FloatField(default=0)

    def __str__(self):
        return self.state
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Sex._meta.fields]

class Race(models.Model):
    state = models.CharField(max_length=3)
    year = models.IntegerField(default=2010)
    white = models.IntegerField(default=0)
    black = models.IntegerField(default=0)
    asian = models.IntegerField(default=0)
    native_american = models.IntegerField(default=0)
    other = models.IntegerField(default=0)

    def __str__(self):
        return self.state
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Race._meta.fields]

class Economy(models.Model):
    state = models.CharField(max_length=3)
    year = models.IntegerField(default=2010)
    gdp = models.IntegerField(default=0)

    def __str__(self):
        return self.state
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Economy._meta.fields]


class Business(models.Model):
    state = models.CharField(max_length=3)
    year = models.IntegerField(default=2010)
    num_firms = models.IntegerField(default=0)
    num_employees = models.IntegerField(default=0)
    payroll = models.IntegerField(default=0)

    def __str__(self):
        return self.state
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Business._meta.fields]


class Employment(models.Model):
    state = models.CharField(max_length=3)
    year = models.IntegerField(default=2010)
    unemployment = models.FloatField(default=0)

    def __str__(self):
        return self.state
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Employment._meta.fields]


class HealthInsurance(models.Model):
    state = models.CharField(max_length=3)
    year = models.IntegerField(default=2010)
    uninsured_rate = models.FloatField(default=0)

    def __str__(self):
        return self.state
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in HealthInsurance._meta.fields]


class Housing(models.Model):
    state = models.CharField(max_length=3)
    year = models.IntegerField(default=2010)
    homeownership_rate = models.FloatField(default=0)

    def __str__(self):
        return self.state
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Housing._meta.fields]


class Income(models.Model):
    state = models.CharField(max_length=3)
    year = models.IntegerField(default=2010)
    median_hhincome = models.IntegerField(default=0)
    poverty_rate = models.FloatField(default=0)

    def __str__(self):
        return self.state
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Income._meta.fields]


