from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
# Create your models here.
class Asset(models.Model):
    asset_name  = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    asset_price = models.IntegerField()
    purchase_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True )
    depreciation_percent = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.asset_name

@receiver(pre_save, sender=Asset)
def asset_pre_save(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.asset_name)