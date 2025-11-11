from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=222)
    image=models.ImageField(upload_to='images')
    description=models.TextField()
    date=models.DateTimeField()
    slug=models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(f'{self.date}-{self.title[:7]}')
        super().save(*args, **kwargs)