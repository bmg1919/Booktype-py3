#!/bin/bash

/usr/local/bin/python /code/mybook/manage_prod.py migrate
/usr/local/bin/python /code/mybook/manage_prod.py collectstatic --noinput
/usr/local/bin/python /code/mybook/manage_prod.py compress
echo 'from django.contrib.auth.models import User; User.objects.create_superuser("admin", "admin@admin.com", "admin")' | /usr/local/bin/python /code/mybook/manage_dev.py shell
/usr/local/bin/python /code/mybook/manage_prod.py update_permissions
/usr/local/bin/python /code/mybook/manage_prod.py update_default_roles