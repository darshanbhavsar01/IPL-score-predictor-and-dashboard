web: gunicorn ipl_dashboard.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
