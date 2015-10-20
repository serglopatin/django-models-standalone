import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "models_standalone.settings")
django.setup()

from models_standalone.models import SampleModel

if __name__=="__main__":

	print "SampleModel objects: " + str(len(SampleModel.objects.all()))
