from django.db import models
import uuid
from django.core.validators import RegexValidator
# Create your models here.


class Department(models.Model):
    STATUS_TYPE = (
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('inactive', 'In Active')
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    department_name = models.CharField(max_length=200)
    department_description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=200, choices=STATUS_TYPE, null=True, blank=True)

    def __str__(self):
        return self.department_name


class Position(models.Model):
    STATUS_TYPE = (
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('inactive', 'In Active')
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    position_name = models.CharField(max_length=200)
    position_description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=200, choices=STATUS_TYPE, null=True, blank=True)

    def __str__(self):
        return self.position_name


class PaymentCurrency(models.Model):
    CURRENCY_TYPES = (
        ('etb', 'ETB'),
        ('usd', 'USD')
    )
    payment_currency = models.CharField(
        max_length=200, choices=CURRENCY_TYPES, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Payment Currencies'

    def __str__(self):
        return self.payment_currency


class Employee(models.Model):
    GENDER_TYPES = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    STATUS_TYPE = (
        ('active', 'Active'),
        ('inactive', 'In Active')
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(
        max_length=200, choices=GENDER_TYPES, null=True, blank=True)
    birthday = models.DateField(
        help_text="Employee's birthday", null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, blank=True)
    date_hired = models.DateField(
        help_text="Employee's date hired", null=True, blank=True)
    monthly_salary = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    payment_currency = models.ForeignKey(
        PaymentCurrency, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=200, choices=STATUS_TYPE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
