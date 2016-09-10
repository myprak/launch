Basic steps to get this up and running
---

- Install requirements.txt, `pip -r install requirements.txt`
- Create/migrate db `python manage.py migrate`
- Load initial fixtures (needed for social apps) `python manage.py loaddata fixtures/socialapps.json`
- Run server! `python manage.py runserver`

*(Note: Commands assume you are on project's root path)*
