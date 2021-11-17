from django.db import models


class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=500, null=False, blank=False)
    name_content = models.CharField(max_length=500, null=False, blank=False)
    resource = models.CharField(max_length=255, null=False, blank=False)
    id_format_content = models.PositiveIntegerField()
    url = models.CharField(max_length=500)
    success = models.IntegerField()
    success_data_update = models.IntegerField()
    acc_type = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'content'
        managed = False


# Create your models here.
