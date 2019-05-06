# Django Full Course for Beginners

# Setting up environment
Installation of MySQL Server followed by creating virtual environment
```sh
virtual env --python=/usr/bin/python3 venv-django
source venv-django/bin/activate
pip install django mysqlclient
```

### Check installation

```
pip freeze
```

output:

```
Django==2.2.1
mysqlclient==1.4.2.post1
pkg-resources==0.0.0
pytz==2019.1
sqlparse==0.3.0
```

# Creating django project
```
django-admin startproject django_freecodecamp
```

# Create a super user
```
python manage.py createsuperuser
```

# Create a products app
```
python manage.py startapp products
```

# Add a simple model for products, migrate and register model in admin.py
```
# Note always run these two commands when making changes to database models
python manage.py makemigrations
python manage.py migrate
```

# Using database from django shell
View records from database
Create new records
```
python manage.py shell
from models.products import Product
Product.objects.all()
Product.objects.create(title='Small Licorice Raspberry Bar',description='Candy bar with licorice',price='0.40')
```