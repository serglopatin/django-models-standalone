# django-models-standalone 

This is just wrapper package on top of django framework, which creates django project with only standalone modules included.

## Howto
**1.** install django-models-standalone: 

`python setup.py install`

**2.** create standalone django models project:

```
cd ~
django-models-standalone startproject myproject
cd ~\myproject
```

**3.** migrate

```
python manage.py migrate
```

**4.** run application with standalone django models:

```
python example.py
```

## TODO

Need to add django dependency check to setup.py
