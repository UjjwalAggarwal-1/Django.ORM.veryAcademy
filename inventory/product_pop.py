import os
import sys

import django


sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from inventory.models import Product, Category, Brand
from users.models import NewUser
import random
# create some categories
while True:
    cat1 = Category.objects.create(name="Electronics")
    cat2 = Category.objects.create(name="Clothing")
    cat3 = Category.objects.create(name="Food")
    cat4 = Category.objects.create(name="Toys")
    cat5 = Category.objects.create(name="Books")
    cat6 = Category.objects.create(name="Furniture")
    cat7 = Category.objects.create(name="Sports")
    cat8 = Category.objects.create(name="Tools")
    cat11 = Category.objects.create(name="Health")
    cat12 = Category.objects.create(name="Beauty")
    cat13 = Category.objects.create(name="Jewelry")
    cat14 = Category.objects.create(name="Music")
    cat15 = Category.objects.create(name="Movies")
    cat16 = Category.objects.create(name="Games")
    cat20 = Category.objects.create(name="Office")
    cat21 = Category.objects.create(name="Industrial")
    cat22 = Category.objects.create(name="Luggage")
    cat23 = Category.objects.create(name="Grocery")
    cat24 = Category.objects.create(name="Outdoors")
    cat25 = Category.objects.create(name="Shoes")
    cat26 = Category.objects.create(name="Handmade")
    cat40 = Category.objects.create(name="Computers")
    cat41 = Category.objects.create(name="Photography")
    break

# create some products
for i in range(1, 50):
    p=Product.objects.create(the_name=f"Product {i}", age=i, )
    p.category.add(random.choice(Category.objects.all().values_list("id", flat=True)))

# create some users
for i in range(1, 10):
    NewUser.objects.create(username=f"User {i}", email=f"{i}@abc.com", password="testPassWorD321")