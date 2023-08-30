from django.db import models

# Create your models here.
class CustomerTable(models.Model):
    logi_user_id = models.AutoField(primary_key=True)
    logi_user_user = models.CharField(default='userId', max_length=45)
    logi_user_company = models.CharField(default='Doshi', max_length=45)
    logi_user_firstname = models.CharField(max_length=45)
    logi_user_diasplayname = models.CharField(default='displayname', max_length=45)
    logi_user_middlename = models.CharField(max_length=45)
    logi_user_familyname = models.CharField(max_length=45)
    logi_user_email = models.CharField(max_length=45)
    logi_user_mobile = models.CharField(max_length=45)