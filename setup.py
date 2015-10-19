from setuptools import setup, find_packages

EXCLUDE_FROM_PACKAGES = [
	'django_models_standalone.conf.project_template',
]

setup(
	name='django_models_standalone',
	version='0.1.0',
	description='Django models as standalone app.',
	long_description='Django models as standalone app.',
	author='Sergey Lopatin',
	author_email='lopatin.sergei@gmail.com',
	license='BSD',
	packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
	entry_points={'console_scripts': [
		'django-models-standalone = django_models_standalone:execute_from_command_line',
	]},
	url='http://github.com/serglopatin/django-models-standalone',
	include_package_data=True,
	classifiers=[
		"Programming Language :: Python",
		"License :: OSI Approved :: BSD License",
		"Development Status :: Beta",
		"Operating System :: OS Independent",
		"Framework :: Django",
		"Intended Audience :: Developers",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
	],
	zip_safe=False,


)
