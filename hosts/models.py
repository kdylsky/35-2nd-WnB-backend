from django.db      import models

from wnb.models    import TimeStampModel

class Host(TimeStampModel):
    user            = models.ForeignKey("users.User", on_delete = models.CASCADE)
    profile_img     = models.CharField(max_length = 200)
    
    class Meta:
        db_table    = 'hosts' 