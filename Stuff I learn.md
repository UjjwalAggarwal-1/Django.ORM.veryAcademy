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

# User model
fields, methods 🤯

# migrations
easily readable
