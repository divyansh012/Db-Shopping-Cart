from django.db import models

class Product(models.Model):

    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")



    def __str__(self):
        return self.product_name

class Contact(models.Model):

    cd_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")




    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=3000)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=70, default="")
    city = models.CharField(max_length=70, default="")
    state = models.CharField(max_length=70, default="")
    zip_code = models.CharField(max_length=70, default="")



class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=2000)
    timestamp = models.DateField(auto_now_add=True)




