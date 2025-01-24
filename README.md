# Distributed_Systems
# command to run the file
python manage.py makemigrations
python manage.py migrate --database=users_db
python manage.py migrate --database=products_db
python manage.py migrate --database=orders_db
python manage.py run_insertions

