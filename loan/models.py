from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin


class Profile(models.Model):
    membership_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    dob = models.DateField
    home_address = models.CharField(max_length=100)
    office_phone = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    pin_number = models.TextField
    email = models.EmailField
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('created_at',)
        db_table = 'profiles'


class Address(models.Model):
    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('O', 'Other'),
    )
    TYPE_OF_STAY = (
        ('R', 'Rented'),
        ('O', 'Owner'),
    )

    town = models.CharField(max_length=100)
    estate = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    duration_of_stay = models.IntegerField
    type_of_stay = models.CharField(choices=TYPE_OF_STAY, max_length=1)
    marital_status = models.CharField(choices=MARITAL_STATUS, max_length=50)
    dependants = models.TextField
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.town

    class Meta:
        db_table = "addresses"


class Employment(models.Model):
    EMPLOYMENT_TERMS = (
        ('P', 'Parmanent'),
        ('C', 'Casual'),
        ('TR', 'Contract'),
        ('O', 'Other'),
    )
    employer = models.CharField(max_length=200)
    physical_address = models.CharField(max_length=200)
    postal_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    designation = models.CharField(max_length=200)
    staff_number = models.CharField(max_length=100)
    employment_terms = models.CharField(
        choices=EMPLOYMENT_TERMS, max_length=200)
    bussiness_type = models.TextField
    years_of_operation = models.IntegerField
    bussiness_income = models.DecimalField(max_digits=15, decimal_places=2)
    rental_income = models.DecimalField(max_digits=15, decimal_places=2)
    other_incomes = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.town

    class Meta:
        db_table = 'employments'


class Bank(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'banks'


class Branch(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "branches"


class User_Bank(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_banks"


class Loan(models.Model):
    LOAN_TYPE = (
        (0, "Normal Loan"),
        (1, "development Loan"),
        (2, "Emergency Loan"),
    )
    purpose = models.PositiveSmallIntegerField(choices=LOAN_TYPE)
    amount_requested = models.DecimalField(decimal_places=4, max_digits=12)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount_requested)

    class Meta:
        db_table = 'loans'


class Other_Loan(models.Model):
    institution = models.CharField(max_length=200)
    amount_advanced = models.DecimalField(decimal_places=4, max_digits=12)
    repayment_period = models.IntegerField
    outstanding_balance = models.DecimalField(decimal_places=4, max_digits=12)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount_requested

    class Meta:
        db_table = "other_loans"


# Register models under admin
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Employment)
admin.site.register(Bank)
admin.site.register(Branch)
admin.site.register(User_Bank)
admin.site.register(Loan)
admin.site.register(Other_Loan)
