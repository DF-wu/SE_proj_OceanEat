from django.db import models
from django_mysql.models import JSONField

class SearchIndex(models.Model):
    search_index = JSONField()
    class Meta():
        managed = True
        db_table = 'search_index'