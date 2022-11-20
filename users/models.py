from django.db      import models

from wnb.models    import TimeStampModel

class User(TimeStampModel):
    first_name          = models.CharField(max_length = 50, null=True)
    last_name           = models.CharField(max_length = 50, null=True)
    email               = models.CharField(max_length = 50)
    phone_number        = models.CharField(max_length = 50, null=True)
    birth_day           = models.CharField(max_length = 50, null=True)
    password            = models.CharField(max_length = 300)

    class Meta:
        db_table = 'users'