import os
import django
from models_standalone import reset_db_connection, settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "models_standalone.settings")
django.setup()

from models_standalone.models import SampleModel

if __name__=="__main__":


	"""
	This is sample application that uses django models.
	When DEBUG is True, we must manually reset db connection  after each query.
	"""

	for i in range(3):

		print "SampleModel objects: " + str(len(SampleModel.objects.all()))

		if settings.DEBUG:
			reset_db_connection()

