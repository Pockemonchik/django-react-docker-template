from django.db import models


class LogEntry(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10,null=True,blank=True)
    user = models.CharField(max_length=10,null=True,blank=True)
    action_type = models.CharField(max_length=30,null=True,blank=True)
    url = models.CharField(max_length=60,null=True,blank=True)
    data = models.TextField(null=True,blank=True)
    query = models.TextField(null=True,blank=True)
    description = models.CharField(max_length=30,null=True,blank=True)
    object = models.CharField(max_length=30,null=True,blank=True)

    class Meta:
        verbose_name = "Действия пользователей"
        verbose_name_plural = "Действия пользователей "
        ordering = ["time"]
    
        
    def save(self, *args, **kwargs):
   
        super().save(*args, **kwargs)