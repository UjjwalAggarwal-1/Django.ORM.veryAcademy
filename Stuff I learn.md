# terminal
<btn>ctrl</btn> + <btn>L</btn> will scroll up screen
ctrl + ` will pop up/ hide terminal

# extensions
SQLite

# models
auto_now_add for creation, auto_now for updates
verbose name for fields
help text for fields
renaming id by using BigAutoField (brand_id = models.BigAutoField(primary_key=True))
As currently implemented, setting auto_now or auto_now_add to True will cause the field to have editable=False and blank=True set.
I set up my timezone, the datetimefields data was corrected(updated) acc. to TZ, but neither date field nor time field. new ones are correct.
using fixtures for data population

## custom user model
User model is formed from AbstractUser, So inherit it in NewUer
add, override fields
i wanted non-uniqueness in username and i want email unique, so set USERNAME_FIELD as email in model
when i go to create super user from terminal, i get some error, i had to set username in required fields, didnt fully understand reason
also renamed the id thing to user_id,(set pk True and BigAutoField)
set AUTH_USER_MODEL as the new model in settings
in admin.py, to represent the new fields, add the fields anywhere in fieldsets and then register the model, and the admin class is how you link the fieldsets, and i'll try to use some decorator thingy which came out with Django 4

# User model
fields, methods 🤯

# migrations
easily readable

# indexing
A good rule, if you are going to order by, or filter by, it should be indexed.
models.CharField(db_index=True, max_length=100)
 
 class Meta:
    indexes = [models.Index(fields=['code0', 'code1']),]
**https://levelup.gitconnected.com/just-one-index-in-django-makes-your-app-15x-faster-742e2f13108e**
 
bulk_create
bulk_update
select_related
in_bulk
 https://levelup.gitconnected.com/optimizing-django-queries-28e96ad204de
