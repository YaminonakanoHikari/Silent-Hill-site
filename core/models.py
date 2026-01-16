from django.db import models

class Artifact(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    
    # Картинки для двух миров
    image_normal = models.ImageField(upload_to='artifacts/normal/', verbose_name="Обычное фото")
    image_dark = models.ImageField(upload_to='artifacts/dark/', verbose_name="Жуткое фото")
    
    # Описания для двух миров
    description_normal = models.TextField(verbose_name="Обычное описание")
    description_dark = models.TextField(verbose_name="Истинная суть")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title