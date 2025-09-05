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

## How to run study

First page specify username for the observer and software being observed, then specify institution and trail number.
Lastly specify number of subjects being observed and identifiers for each. Now the trail is ready.

If you like, you can prepare the trail up to this point and share the link with the observer.
*In case you have multiple observers, you will have to setup a trail of each observer.*

When ready, the observer clicks start recording which leads to the record screen.
The record screen shows which subject should be observed, a timer to show time since last observation (in case there is a performance requirement), then two drop down menus which the observer should fill out.

First is behavior, which indicates what the subject is observed doing (see BROMP for more details). 
Second is affect, which is based on the Model of Affect Dynamics (see BROMP for more).

Observer should then click Save and continue as long as the recoding is going on. 
Note that the subject will change every time. 
Use the skip button to skip a subject.
The last three recordings are shown in a list in the bottom and the observer can flag an observation for later. 
For example is a value is wrong or the observer wants to elaborate on what was observed.

Once the trial is ended, click the save and finish button to go to summary. 
On the summary screen the observer can see a list of all observations. 
The observer can flag observations, delete or comment.

### Administrating
You can see a list of all studies by accessing `<domain>/studies`.
For example `127.0.0.1:8000/studies` when running locally. 
This page requires login of a superuser. 
This page provides a list of all studies, ready, running and done. 
When a trial is ready, the link can be shared with observers, who can then start a recording. 
When running the recording screen can be access via a link. 
When done, the summary page can be access and the data can be exported to CSV following the format from BROMP.

As a superuser, you can access the Django system by accessing the `<domain>/admin` page. 
For example: `127.0.0.1:8000/admin` when running locally. 
From here you can add users and access the data.

## Dependency notice

The file `static\HARTSchemas.xml` is a direct copy from https://github.com/pcla-code/HART/blob/main/HARTSchemas.xml and the owners of the repository retain the copyright of the file and its contents.
