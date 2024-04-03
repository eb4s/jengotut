# jengotut

## Step 1: Create A Project
-> python -m django startproject [project name]

## Step 2: Create An App
- python manage.py startapp [app name]

## Step 3: Run Web Server
- cd into the project folder where manage.py is located
- run `python manage.py runserver`

## Step 4: Build Database
-cd into folder with manage.py
- `python manage.py migrate`

## Step 5: Create Super
-cd into folder with manage.py
- `python manage.py createsuperuser`

## Step 6: Add App to Settings' Installed apps Dictionary
-`INSTALLED_APPS = [
-'...
-'app_name',
_`

## Step 7: Add Templates Folder
-`'DIRS': [BASE_DIR/'templates'],`
-Add template folder inside app folder.
