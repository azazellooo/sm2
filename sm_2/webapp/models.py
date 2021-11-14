from django.db import models


class Content(models.Model):
    project_name = models.CharField(max_length=500, null=False, blank=False, verbose_name='project name')
    name_content = models.CharField(max_length=500, null=False, blank=False, verbose_name='content name')
    resource = models.CharField(max_length=500, null=False, blank=False)
    id_format_content = models.PositiveIntegerField()
    url = models.CharField(max_length=500)
    success = models.IntegerField()
    success_data_update = models.IntegerField()
    acc_type = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)


# Create your models here.
