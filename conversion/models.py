from django.db import models
import random
import string

class ConversionModel():

	def __init__(self):
		super(ConversionModel, self).__init__()

	def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))