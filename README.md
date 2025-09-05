# OSTHAR
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17062039.svg)](https://doi.org/10.5281/zenodo.17062039)
Open Source Tool for Human Affect Recording inspired by Human Affect Recording Tool - Implemented with Django for most compatibility

## Getting started

1. Clone project and enter folder.
2. Install dependencies.
```bash
pip install -r requirements.txt
```
3. Migrate.
```bash
python manage.py migrate
```
4. Create admin user.
```bash
python manage.py createsuperuser
```
5. Run server.
```bash
python manage.py runserver
```

## Dependency notice

The file `static\HARTSchemas.xml` is a direct copy from https://github.com/pcla-code/HART/blob/main/HARTSchemas.xml and the owners of the repository retain the copyright of the file and its contents.
