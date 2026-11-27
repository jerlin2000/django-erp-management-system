# Django ERP Management System

An AI-assisted educational ERP project built using Python and Django.

## Features
- Inventory management
- Purchase and sales tracking
- Staff authentication
- Inventory dashboard

## Dashboard languages

Use the language picker on the inventory dashboard to switch between English
and 25 translations. The selected language is saved in a browser cookie.
Django also uses its available translations for the built-in admin screens.

The dashboard catalogs are in `inventory/locale`. After editing a `.po`
catalog, run `python manage.py compilemessages` with GNU gettext installed and
commit the updated `.mo` catalog so the new text is available at runtime.

## Technologies
- Python
- Django
- SQL

## Installation
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Project Status
Development prototype. Runtime testing pending.
