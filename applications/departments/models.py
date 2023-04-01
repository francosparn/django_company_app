from django.db import models


class Department(models.Model):
    name = models.CharField(
        'Name', 
        max_length=80
    )
    short_name = models.CharField(
        'Short name', 
        max_length=20, 
        unique=True
    )
    anulate = models.BooleanField(
        'Anulate', 
        default=False
    )
    avatar = models.ImageField(
        upload_to='company', 
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name_plural = 'Areas of the company'
        ordering = ['name']
        unique_together = ('name', 'short_name')
    
    def __str__(self):
        return self.name
