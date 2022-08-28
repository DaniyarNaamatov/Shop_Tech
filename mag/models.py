from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    price = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="media")
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



