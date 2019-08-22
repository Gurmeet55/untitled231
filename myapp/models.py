from django.db import models

# Create your models here.
class web2(models.Model):
    news_head=models.CharField(max_length=225)
    news_web = models.CharField(max_length=225)
    news_img = models.ImageField()
    date=models.DateField()


class News(models.Model):
    title = models.CharField(max_length=225)
    authors = models.CharField(max_length=225)
    publisher=models.ForeignKey(web2,on_delete=models.PROTECT)



class tb_registration(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    password = models.CharField(max_length=225)

class tb_emp(models.Model):
    e_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)

    jobtitle = models.CharField(max_length=225)
    specialization = models.CharField(max_length=225)
    Experince = models.CharField(max_length=225)
    #publisher = models.ForeignKey(tb_registration, on_delete=models.PROTECT)



