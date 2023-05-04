from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES =(
        ("Male", "Male"),
        ("Female", "Female"),
    )
    MEDICATION_HISTORY_CHOICES = (
        ('Cholesterol', 'Cholesterol'),
        ('HBP', 'HBP'),
        ('Diabetes', 'Diabetes'),
        ('Asthma', 'Asthma'),
        ('Osteoporosis', 'Osteoporosis'),
        ('Arthritis', 'Arthritis'),
        ('HA', 'HA'),
        ('BS', 'BS'),
        ('Hemoglobin', 'Hemoglobin'),
        ('Cancer', 'Cancer'),
        ('Breast', 'Breast'),
        ('other', 'other'),
    )
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    medication_history = models.CharField(choices=MEDICATION_HISTORY_CHOICES, max_length=100)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    email_verification_token = models.CharField(max_length=200, null=True, blank=True)
    forget_password_token = models.CharField(max_length=200, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def name(self):
        return f'{self.first_name} {self.last_name}' 
    
    def __str__(self) -> str:
        return self.email