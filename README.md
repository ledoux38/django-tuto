## README

### Installation
#### Window:
#### Linux:

1. Création d'un environement virtuel:

   ```virtualenv -p python3 env```

2. Lancer Environement virtuel

3. Creation/Mise a jour du requirements.txt:

```pip freeze > requirements.txt```

4. Installation des dépandances:
   
```pip install -r requirements.txt```

#### Autres

1. Lancer Environement:

```source env/bin/activate```

2. Lancer Application

```cd mysite```

```python manage.py runserver```

3. migration

``` python manage.py migrate```

4. Creation super user

```python manage.py createsuperuser```