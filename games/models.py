from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name
    

class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_year = models.IntegerField(null=True, blank=True)
    company = models.ForeignKey(Company, related_name='games', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    
    def __str__(self):
        return self.title