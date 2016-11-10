from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import bcrypt, re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

	def validate_inputs(self, request):
		errors = []
		if len(request.POST["first_name"]) < 2 or len(request.POST["last_name"]) < 2:
			errors.append("First name and last name must have at least 2 characters")
		if not EMAIL_REGEX.match(request.POST["email"]):
			errors.append("Invalid Email")
		if len(request.POST["password"]) < 8:
			errors.append("Password must have at least 8 characters")

		return errors

	def validate_registration(self, request):
		errors = self.validate_inputs(request)

		if len(errors) > 0:
			return (False, errors)

		user = self.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
		return (True, user)
		

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	password = models.CharField(max_length=45)

	objects = UserManager()